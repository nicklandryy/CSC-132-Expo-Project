import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import datetime
from random import randint
import time
import RPi.GPIO as GPIO
from hx711 import HX711  # import the class HX711

global WEIGHTS
WEIGHTS = {}

try:
    #setup GPIO
    GPIO.setmode(GPIO.BCM)
    DOOR_SENSOR_PIN =18



    GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    ################# GUI #########################

    #This class basically allows for the change in GUI pages.
    class SeaofBTCapp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand = True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            #Inializing all pages
            self.frames = {}
            for F in (StartPage, PageOne, RecordW):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            #Starting it off with the Main page
            self.show_frame(StartPage)

        #Allowing for the pages to move to the front of the screen.
        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

    #This is the Main page of the GUI, It holds 4 buttons.
    class StartPage(tk.Frame):

        def __init__(self, parent, controller):

            #initalizing Frame Class
            tk.Frame.__init__(self,parent)

            #main frame of GUI
            frame = tk.Frame(self)

            #This is what creates the background and Title of the Main page of the GUI
            label = tk.Label(self, text="SECURE BOX", width="100")
            label.configure(
                anchor="nw", font="{Yu Gothic Light} 48 {}", justify="left", takefocus=False
            )
            label.place(relx="0.03", rely="0.06", x="0", y="0")

            #This button will make the sensor record a weight, while also updating the page after initalization.
            takew = tk.Button(self, text="Take Weight",
                                command=lambda:[controller.frames[RecordW].add_data()])
            takew.place(
                relheight="0.17", relwidth="0.34", relx="0.09", rely="0.27", y="0"
            )

            #This button will display all current stored data for weight
            recw = tk.Button(self, text="Recorded Weights",
                                command=lambda: controller.show_frame(RecordW))
            recw.place(
                relheight=".17", relwidth=".34", relx="0.56", rely="0.27", x="0", y="0"
            )

            #This button, when pressed, uses the camera to take an image
            takei = tk.Button(self, text="Take Image")
            takei.place(
                relheight=".17", relwidth=".34", relx=".09", rely="0.56", x="0", y="0"
            )

            #This button, when pressed, shows all currently stores images
            reci = tk.Button(self, text="Image Storage",
                                command=lambda: controller.show_frame(PageOne))
            reci.place(
                anchor="nw", relheight=".17", relwidth="0.34", relx=".56", rely=".56", y="0"
            )

            frame.configure(height="500", width="700")
            frame.pack(side="top")


    #IGNORE FOR NOW
    class PageOne(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Recorded Images", font="{Yu Gothic Light} 24 {}")
            label.pack(pady=10,padx=10)

            #The Back Button
            back = tk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            back.place(
                anchor="nw", relwidth="0.17", relx="0.77", rely="0.91", x="0", y="0"
            )


    #The Page for the Recorded Weights and their Time
    class RecordW(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Recorded Weights", font="{Yu Gothic Light} 24 {}")
            label.pack(pady=10,padx=10)


            #The Back Button
            back = tk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
            back.place(
                anchor="nw", relwidth="0.17", relx="0.77", rely="0.91", x="0", y="0"
            )

        #Displays an updated list of the data
        def add_data(self):
            
            #key is in place of the weight
            key = str(hx.get_weight_mean(1)) + 'g'

            #dictionary to hold date and time of the weight taken
            WEIGHTS[key] = str(datetime.datetime.now())

            #creating the textbox
            textb = ScrolledText(self)
            for keys in WEIGHTS:
                textb.insert(tk.END, str(WEIGHTS[keys])+ ": "+str(keys) + "\n")
            textb['state'] = tk.DISABLED
            textb.place(anchor="nw", height="390", width="800", x="0", y="0")


    #################### Weight sensor ###########################
    hx = HX711(dout_pin=5, pd_sck_pin=6,  select_channel='B')
    err = hx.reset()  # Before we start, reset the hx711 ( not necessary)
    if err:  # you can check if the reset was successful
        print('not ready')
    else:
        print('Ready to use')

    hx.select_channel(
        channel='B')  # Select desired channel. Either 'A' or 'B' at any time.

    # Read data several, or only one, time and return mean value
    # argument "readings" is not required default value is 30
    data = hx.get_raw_data_mean(readings=30)

    if data:  # always check if you get correct value or only False
        print('Raw data:', data)
    else:
        print('invalid data')

    # measure tare and save the value as offset for current channel
    # and gain selected. That means channel A and gain 64
    result = hx.zero(readings=30)

    # Read data several, or only one, time and return mean value.
    # It subtracts offset value for particular channel from the mean value.
    # This value is still just a number from HX711 without any conversion
    # to units such as grams or kg.
    data = hx.get_data_mean(readings=30)

    # In order to calculate the conversion ratio to some units, in my case I want grams,
    # you must have known weight.
    input('Put known weight on the scale and then press Enter')
    data = hx.get_data_mean(readings=30)
    if data:
        print('Mean value from HX711 subtracted by offset:', data)
        known_weight_grams = input(
            'Write how many grams it was and press Enter: ')

        value = float(known_weight_grams)

    ratio = data / value  # calculate the ratio for channel A and gain 64
    hx.set_scale_ratio(ratio)  # set ratio for current channel
    print('Ratio is set.')

    print('Current weight on the scale in grams is: ')
    print(hx.get_weight_mean(30), 'g')

    for i in range(40):
        # the value will vary because it is only one immediate reading.
        # the default speed for hx711 is 10 samples per second
        print(hx.get_weight_mean(readings=1), 'g')

    
    #constructing GUI
    app = SeaofBTCapp()

    #Because we do not know if it is closed or open at the beginning
    isOpen = False
    oldIsOpen = None

    # Because there is no While loop that works with tkinter, used the .after() function
    #recursively, so that while the GUI is running, every .1 second, the sensor is checked
    def task():
        #tells tkinter to look for a global variable, since it doesnt work like normal
        global isOpen
        global oldIsOpen

        #get new inputs
        oldIsOpen = isOpen
        isOpen = GPIO.input(DOOR_SENSOR_PIN)

        #Checks for changes in sensor, only prints when there is.
        if(isOpen and (isOpen != oldIsOpen)):
            print("Space is unoccupied")
        elif(isOpen != oldIsOpen):
            print("Space is occupied")
            #adds weight and updates frame.
            app.frames[RecordW].add_data()

        #schedules the task to run again in .1 second
        app.after(100,task)
            

    app.after(100,task)
    app.mainloop()

#to end code
except (KeyboardInterrupt, SystemExit):
    print("Shutting Down... Please Wait...")
finally:
    GPIO.cleanup()
    #this force closes the GUI
    app.destroy()



    

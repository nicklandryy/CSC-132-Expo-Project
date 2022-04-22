import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import datetime
from random import randint

global WEIGHTS
WEIGHTS = {}

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
        key = randint(1,1000)

        #dictionary to hold date and time of the weight taken
        WEIGHTS[key] = str(datetime.datetime.now())

        #creating the textbox
        textb = ScrolledText(self)
        for keys in WEIGHTS:
            textb.insert(tk.END, str(WEIGHTS[keys])+ ": "+str(keys) + "\n")
        textb['state'] = tk.DISABLED
        textb.place(anchor="nw", height="390", width="800", x="0", y="0")


#################### Weight sensor ###########################







app = SeaofBTCapp()
app.mainloop()



    

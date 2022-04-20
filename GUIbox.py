import tkinter as tk

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

        #This button will make the sensor record a weight
        takew = tk.Button(self, text="Take Weight")
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

        frame.configure(height="600", width="800")
        frame.pack(side="top")


#IGNORE
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font="{Yu Gothic Light} 24 {}")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(RecordW))
        button2.pack()

#The Page for the Recorded Weights and their Time
class RecordW(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Recorded Weights", font="{Yu Gothic Light} 24 {}")
        label.pack(pady=10,padx=10)

        #The Text Box
        text1 = tk.Text(self, state=tk.DISABLED)
        text1.configure(height="10", width="50")
        text1.place(anchor="nw", height="520", width="800", x="0", y="0")

        #The Back Button
        back = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        back.place(
            anchor="nw", relwidth="0.17", relx="0.77", rely="0.91", x="0", y="0"
        )

        

app = SeaofBTCapp()
app.mainloop()



    
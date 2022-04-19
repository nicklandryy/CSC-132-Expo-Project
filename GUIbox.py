#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class MainScreen:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame1 = ttk.Frame(self.toplevel1)
        self.label2 = ttk.Label(self.frame1)
        self.label2.configure(
            anchor="nw", font="{Yu Gothic Light} 48 {}", justify="left", takefocus=False
        )
        self.label2.configure(text="SECURE BOX", width="100")
        self.label2.place(relx="0.03", rely="0.06", x="0", y="0")
        self.takew = ttk.Button(self.frame1)
        self.takew.configure(takefocus=False, text="Take Weight")
        self.takew.place(
            relheight="0.17", relwidth="0.34", relx="0.09", rely="0.27", y="0"
        )
        self.recw = ttk.Button(self.frame1)
        self.recw.configure(text="Recorded Weights")
        self.recw.place(
            relheight=".17", relwidth=".34", relx="0.56", rely="0.27", x="0", y="0"
        )
        self.takei = ttk.Button(self.frame1)
        self.takei.configure(text="Take Image")
        self.takei.place(
            relheight=".17", relwidth=".34", relx=".09", rely="0.56", x="0", y="0"
        )
        self.reci = ttk.Button(self.frame1)
        self.reci.configure(text="Image Storage")
        self.reci.place(
            anchor="nw", relheight=".17", relwidth="0.34", relx=".56", rely=".56", y="0"
        )
        self.frame1.configure(height="600", width="800")
        self.frame1.pack(side="top")
        self.toplevel1.configure(height="800", width="600")

        # Main widget
        self.mainwindow = self.toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = TheScreen()
    app.run()


    
from tkinter import *
root = Tk()
root.title("Classes in Tkinter")
root.geometry("500x500")


class Circle:
    import math
    my_results = StringVar()
    def __init__(self, master):
        # Label 1
        self.lab1 = Label(master, text="Please enter radius")
        self.lab1.place(x=5, y=5)
        # Entry
        self.my_entry = Entry(master)
        self.my_entry.place(x=150, y=5)
        # Label 2- Answer [Answer is referred to as my_results within a text variable]
        self.lab2 = Label(master, text="", width="50", textvariable=self.my_results, bg='#fff', fg='#f00')
        self.lab2.place(x=20, y=50)
        # Button
        self.btn_area = Button(master, text="calculate Area", command=self.area_of_circle, )
        self.btn_area.place(x=100, y=100)
        self.btn_clear = Button(master, text="Clear",command=self.clear)
        self.btn_clear.place(x=150, y=100)

    def clear(self):
        self.my_entry.delete()

    def area_of_circle(self):
        results =self.math.pi * int(self.my_entry.get()) * int(self.my_entry.get())
        self.my_results.set(results.__round__(2))

# End Of Circle

# Start of Rectangle


width = StringVar()
height = StringVar()

class Rectangle:
    my_results = StringVar()

    def __init__(self, master):
        #Labels
        self.label1 = Label(master, text="Please Enter width")
        self.label2 = Label(master, text="Please Enter height")
        self.label1.place(x=5, y=200)
        self.lable2.place(x=5, y=250)
        self.area_of_rectangle = Label(master, textvariable=self.my_results)
        #Entries
        self.entry_width = Entry(master, textvariable=width)
        self.entry_height = Entry(master, textvariable=height)
        self.entry_width.place(x=150, y=200)
        self.entry_height.place(x=150, y=250)
        #Buttons
        self.button_area = Button(master, text="Area", command=self.area_of_rectangle)

    def area_of_rectangle(self):
        results = self.entry_width.get() * self.entry_height.get()
        self.my_results.set(results)

Circle(root)
root.mainloop()


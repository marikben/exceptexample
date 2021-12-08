from tkinter import *

root = Tk()
root.geometry("250x150")
root.resizable(0,0) #doesn't let the content of the window to resize it

def checkYear(event):
    checkable = year.get()
    try:
        intCheck = int(checkable)
        if len(checkable) == 4:
            answer["text"] = "The year you entered is valid!"
        else:
            raise ValueError
    except ValueError:
        answer["text"] = "Please only enter a four digit value"
    except Exception as e:
        answer["text"] = e
       
mainframe = Frame(root, height=120, width=200, bg="#add8e6")
mainframe.pack_propagate(0) #doesn't let the content of the frame to resize it
mainframe.pack()

heading = Label(mainframe,text="Check if a year is valid", font=("Arial", 15))
heading.pack(side=TOP)

answer = Label(mainframe,text="", bg="#add8e6")
answer.pack(side=TOP,pady=5)

year = Entry(mainframe, width=20, bg="white")
year.pack()

btn = Button(mainframe, text="Check it!")
btn.pack(side=BOTTOM, pady=5)
btn.bind("<Button-1>", checkYear)

root.mainloop()

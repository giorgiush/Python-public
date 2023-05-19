import tkinter

window = tkinter.Tk()
window.title("Some Title")
window.minsize(width=400, height=200)
#window.config(padx=100, pady=100)



a_label = tkinter.Label(text="Hello there", font=("Arial", 20, "italic"))
#a_label.place(x=70, y=120)
a_label.grid(column=0, row=0)
#a_label.config(padx=50, pady=30)


def click():
    print("clicked")
    user_input = an_input.get()
    a_label["text"] = user_input

a_button = tkinter.Button(text="Click here", command=click)
#a_button.place(x=50, y=100)
a_button.grid(column=1, row=1)



an_input = tkinter.Entry(width=15)
print(an_input.get())
#an_input.place(x=50, y=100)
an_input.grid(column=2, row=2)


# #Text
# text = tkinter.Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(tkinter.END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", tkinter.END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = tkinter.IntVar()
# checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = tkinter.IntVar()
# radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = tkinter.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


window.mainloop()



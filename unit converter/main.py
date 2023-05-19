import tkinter


window = tkinter.Tk()
window.title("Converter")
window.config(padx=10, pady=10)


entry = tkinter.Entry(width=20)
entry.grid(row=0, column=1)


label_1=tkinter.Label(text="")
label_1.grid(row=0, column=2)

label_2=tkinter.Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3=tkinter.Label(text="0")
label_3.grid(row=1, column=1)


label_4=tkinter.Label(text="")
label_4.grid(row=1, column=3)


def listbox_used(event):
   
    if listbox.get(listbox.curselection()) == options[0]:
        label_1.config(text="Miles")
        label_4.config(text="Km")
        label_3.config(text=str(round(int(entry.get())*1.609344, 2)))
    elif listbox.get(listbox.curselection()) == options[1]:
        label_1.config(text="Km")
        label_4.config(text="Miles")
        label_3.config(text=str(round(int(entry.get())/1.609344, 2)))
    elif listbox.get(listbox.curselection()) == options[2]:
        label_1.config(text="Pounds")
        label_4.config(text="Kg")
        label_3.config(text=str(round(int(entry.get())*0.45359237, 2)))
    elif listbox.get(listbox.curselection()) == options[3]:
        label_1.config(text="Kg")
        label_4.config(text="Pounds")
        label_3.config(text=str(round(int(entry.get())/0.45359237, 2)))

listbox = tkinter.Listbox(height=4, width=12)
options = ["Miles to Km", "Km to Miles", "Pounds to Kg", "Kg to Pounds"]
for item in options:
    listbox.insert(options.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=3, column=1)




window.mainloop()



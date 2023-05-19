import tkinter
import random
import pandas
import random

AQUA = "#33FFFF"
AQUA_DARK = "#14b7b8"
KNOWN = []

#----------------------- DATA -----------------------#


#GOT THE ENCODING "CP932" with this below
# with open(file="./day_31_flashcards/words.csv") as file:
#     file.read()
#     print(file)

data = pandas.read_csv("./day_31_flashcards/words.csv", encoding = 'cp932')
words = {index:{"EN":row.English, "JP":row.Japanese} for (index, row) in data.iterrows()}
print(words)
INDEX = random.randint(0, len(words)-1)


#----------------------- CHECK -----------------------#


def check():
    global INDEX
    global KNOWN
    if len(KNOWN) == len(words)-1:
        KNOWN = []
    KNOWN.append(INDEX)
    while INDEX in KNOWN:
        INDEX = random.randint(0, len(words)-1)
    label.config(text=f"{words[INDEX]['JP']}")
    print(KNOWN)
    countdown(3, INDEX)


#----------------------- CROSS -----------------------#


def cross():
    global INDEX
    global KNOWN
    INDEX = random.randint(0, len(words)-1)
    while INDEX in KNOWN:
        INDEX = random.randint(0, len(words)-1)
    label.config(text=f"{words[INDEX]['JP']}")
    countdown(3, INDEX)


#----------------------- UI SETUP -----------------------#


window = tkinter.Tk()
window.title("Do you know this word?")
window.minsize(width=500, height=200)
window.config(background=AQUA, padx=50, pady=50)

label = tkinter.Label(text=f"{words[INDEX]['JP']}", background=AQUA_DARK, width=13, height=3, font=("Courier", 40))
label.grid(row=1, column=0, columnspan=3)


cross_image = tkinter.PhotoImage(file="./day_31_flashcards/cross.png")
cross_image = cross_image.subsample(5)
cross = tkinter.Button(image=cross_image, border=0, background=AQUA, activebackground=AQUA, command=cross)
cross.grid(row=2, column=0)

check_image = tkinter.PhotoImage(file="./day_31_flashcards/check.png")
check_image = check_image.subsample(5)
check = tkinter.Button(image=check_image, border=0, background=AQUA, activebackground=AQUA, command=check)
check.grid(row=2, column=2)

# flashcard = tkinter.Canvas(width=500, height=224, background=AQUA_DARK, highlightthickness=0)
# flashcard.create_text(100, 128, font=("Courier", 39, "bold"), fill="white", text="00:00")
# flashcard.grid(row=1, column=0, columnspan=3)


#----------------------- COUNTDOWN -----------------------#


timer = tkinter.Label(font=("Courier", 40), background=AQUA)
timer.grid(row=2, column=1)

def countdown(count, num):   
    timer.config(text=count)
    if count > 0:
        window.after(1000, countdown, count -1, num)
    if count == 0:
        label.config(text=f"{words[num]['EN']}")
countdown(3, INDEX)


window.mainloop()
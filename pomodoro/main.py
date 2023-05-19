import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
checkmarks = []
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps
    global checkmarks 
    checkmarks = []
    reps = 0
    window.after_cancel(timer)
    checkmark.config(text="")
    header.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(clock, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():   
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        header.config(text="Break", foreground=RED)
        checkmarks.append("✔")
        checkmark.config(text='.'.join(checkmarks))
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        header.config(text="Break", foreground=PINK)
        checkmarks.append("✔")
        checkmark.config(text='.'.join(checkmarks))
    elif reps % 2 != 0:
        countdown(WORK_MIN * 60)
        header.config(text="Work", foreground=GREEN)

        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    global timer
    mins = count // 60
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    if count >= 0:
        canvas.itemconfig(clock, text=f"{mins}:{secs}")
        timer = window.after(1000, countdown, count -1)
    else:
        start()


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, background=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
pic = tkinter.PhotoImage(file="./day_28_pomodoro/tomato.png")
canvas.create_image(100, 112, image=pic)
clock = canvas.create_text(100, 128, font=(FONT_NAME, 39, "bold"), fill="white", text="00:00")
canvas.grid(row=1, column=1)


header = tkinter.Label(text="Timer", font=(FONT_NAME, 39, "bold"), foreground=GREEN, background=YELLOW)
header.grid(row=0, column=1)


checkmark = tkinter.Label(text=" ", background=YELLOW, foreground=GREEN)
checkmark.grid(row=3, column=1)


start_button = tkinter.Button(foreground="blue", text="Start", command=start)
start_button.grid(row=2, column=0)


reset_button = tkinter.Button(foreground="blue", text="Reset", command=reset)
reset_button.grid(row=2, column=3)


window.mainloop()
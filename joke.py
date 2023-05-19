import requests
import tkinter

def generate():
    response = requests.get(url="https://official-joke-api.appspot.com/random_joke")
    response.raise_for_status()
    joke = response.json()
    button.config(text=f"{joke['setup']}\n{joke['punchline']}")

window = tkinter.Tk("RANDOM JOKE")
window.minsize(width=500, height=200)
window.config(padx=50, pady=50, background="pink")

button = tkinter.Button(width=40, height=5, background="aqua", command=generate)
button.pack()

window.mainloop()


x = 12
if x == 1:
    print("aaa")
    raise Exception("huh")
    print("uuu")
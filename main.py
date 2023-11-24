from tkinter import *
import requests


def get_quote():
    response = requests.get(url="http://api.quotable.io/quotes/random?author=AlbertEinstein&maxLength=125")
    response.raise_for_status()
    data = response.json()
    quote = data[0]["content"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Albert Einstein Said...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Einstein Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

einstein_img = PhotoImage(file="einstein.png")
einstein_button = Button(image=einstein_img, highlightthickness=0, command=get_quote)
einstein_button.grid(row=1, column=0)
get_quote()

window.mainloop()

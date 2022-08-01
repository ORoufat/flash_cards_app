import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

'''We created a variable named data to read the csv file.
Then converted the csv into a dictionary called "to_learn" because it is easier to work with dictionary'''
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:

    '''Setting orient to records, allows to view each column's values as a list.
    Ex: [{'French'}: 'historie, 'English': 'history}]'''
    to_learn = data.to_dict(orient="records")

'''Creating an empty dictionary to store randomly chosen words in here temporarily '''


'''Creating Next Function to go to the next card'''
def next():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    '''This line counts 3 seconds and triggers the flip function'''
    flip_timer = window.after(3000, func=flip)


'''This function allows to flip the card and get English meaning of the word'''
def flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)
canvas = Canvas(width=800, height=526)

'''Path to the button images'''
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthicknes=0)
canvas.grid(row=0, column=0, columnspan=2)

'''Displays the Button Icon - Image and triggers next function'''
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthicknes=0, command=next)
unknown_button.grid(row=1, column=0)

'''Displays the Button Icon - Image and triggers next function'''
check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, highlightthicknes=0, command=known)
know_button.grid(row=1, column=1)

next()

window.mainloop()

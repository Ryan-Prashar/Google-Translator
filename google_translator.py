from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
from googletrans import LANGUAGES

def change(text="type", src="english", dest="hindi"):
    try:
        translator = GoogleTranslator(source=src, target=dest)
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return f"Error: {e}"

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_text.get(1.0, END)
    textget = change(text=msg, src = s, dest = d)
    dest_text.delete(1.0, END)
    dest_text.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='blue')

lab_text = Label(root, text="Translator", font=("Times New Roman", 50, "bold"), bg="Grey")
lab_text.place(x=100, y=40, height=100, width=300)

lab_text = Label(root, text="Enter Source Text", font=("Times New Roman", 20, "bold"), fg="Black")
lab_text.place(x=100, y=160, height=30, width=300)

Sor_text = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_text.place(x=10, y=200, height=150, width=480)

languages_dict = GoogleTranslator().get_supported_languages(as_dict=True)
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, value=list_text)
comb_sor.place(x=10, y=370, height=40, width=150)
comb_sor.set("english")

button_change = Button(root, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=370, height=40, width=150)

comb_dest = ttk.Combobox(root, value=list_text)
comb_dest.place(x=330, y=370, height=40, width=150)
comb_dest.set("hindi")

lab_text = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), fg="Black")
lab_text.place(x=100, y=450, height=40, width=300)

dest_text = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_text.place(x=10, y=500, height=150, width=480)

root.mainloop()

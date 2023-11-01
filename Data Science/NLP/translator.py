import tkinter as tk
from translate import Translator

window =tk.Tk()

window.title('Adem Translator')

window.geometry('1200x800')

label = tk.Label(window, text='Click the button to translate')
font = 'Calibri 15 bold'
label.pack(pady=20)

T = tk.Text(window, height='30', width='35')
T.pack(pady=20)

langs = ['tr', 'jp', 'fr', 'en', 'de']
variable = tk.StringVar(window)
variable.set("tr")
menu = tk.OptionMenu(window, variable, 'tr', 'jp', 'fr', 'en', 'de')
menu.pack()

#source = tk.Entry(window)
#source.pack()
def on_click_btn():
    
    translator = Translator(to_lang='tr')
    
    label2 = tk.Label(window, text= translator.translate(T.get(1.0, 'end-1c')))
    label2.pack()   


btn = tk.Button(window, text='Translate', command=on_click_btn)
btn.pack(pady=10)

window.mainloop()
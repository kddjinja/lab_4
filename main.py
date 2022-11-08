from tkinter import *
from playsound import playsound
import random
from tkinter import messagebox, Label
from tkinter.ttk import *


def Slide():
    import time
    Progress_Bar['value'] = 25
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 50
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 75
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 100


def play():
    playsound('8-Bit_Universe_-_Numb_73206306.mp3')


def clicked():
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u',
               'i', 'o', 'p', 'a', 's', 'd', 'f',
               'g', 'h', 'j', 'k', 'l', 'z', 'x',
               'c', 'v', 'b', 'n', 'm']
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    res = txt.get()
    if (len(res) != 5):
        messagebox.showinfo(title='Ошибка!', message='Введите не более 5 символов!')
    elif ((str(res)[i] not in symbols) for i in range(len(res))):
        messagebox.showinfo(title='Ошибка!', message='Формат ввода не соответствует системе счисления')
    else:
        code = ''
        # numbers = ''
        code += str(int(res, 16))[0]
        for i in range(4):
            code += str(random.randint(0, 9))
        code += '-'
        code += str(int(res, 16))[1]
        for i in range(4):
            code += str(random.randint(0, 9))
        code += '-'
        code += str(int(res, 16))[2]
        for i in range(4):
            code += str(random.randint(0, 9))
        code += str(int(res, 16))[len(res) - 2]
        code += str(int(res, 16))[len(res) - 1]
        # code += ''.join((random.choice(res)) for x in range(3)).upper()
        # code += '-'
        # for i in range(len(res)):
        #     if (ord(str(res[i]).upper()) - 64 >= 20):
        #         numbers += str(ord(str(res[i]).upper()) - 84)
        #     elif (ord(str(res[i]).upper()) - 64 >= 10):
        #         numbers += str(ord(str(res[i]).upper()) - 74)
        #     else:
        #         numbers += str(ord(str(res[i]).upper()) - 64)
        # code += ''.join((random.choice(numbers)) for x in range(6))
        # code += '-'
        # code += ''.join((random.choice(res)) for x in range(3)).upper()
        Slide()

        play()
        messagebox.showinfo(title='Ключ: ', message=code)


window = Tk()
window.title("Key Making")
window.geometry('700x352')
window.image = PhotoImage(file='pic.gif')
bg_logo: Label = Label(window, image=window.image)
bg_logo.grid(row=0, column=0)

lbl = Label(window, text='Введите 5-значное число в 16-ричной системе ')
lbl.place(relx=.5, rely=.1, anchor="c")

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.place(relx=.5, rely=.2, anchor="c")
Progress_Bar = Progressbar(window, orient=HORIZONTAL, length=250, mode='determinate')
Progress_Bar.place(relx=.5, rely=.2, anchor="c")
Progress_Bar.grid(row=0, column=0)

btn = Button(window, text="Сгенерировать ключ", command=clicked)
btn.place(relx=.5, rely=.7, anchor="c")

# Button(window,text='Run',command=Slide).pack(pady=10)


window.mainloop()

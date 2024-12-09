import tkinter as tk
from tkinter import messagebox
import random

#function to generate password:

def generate_password():
    try:
        user_input = int(input('Enter the length of password: '))
        if user_input <=0:
            raise ValueError('Enter the correct length of password')
        smalltext = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        capitaltext = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"]
        symbol = ["!", "#", "$", "^", "@"]

        charcters = smalltext + capitaltext + numbers + symbol
        random.shuffle(charcters)
        password = ''.join(random.choices(charcters, k=user_input))
        #for showing result in GUI:
        result_label.config(text = f' Generated Password: {password}')
    except ValueError as e:
        messagebox.showerror(f'Error.Invalid input {e}')

#creating a main window:
root = tk.Tk()# building a foundation
root.title('Password Generators')



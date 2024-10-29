import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

win = ctk.CTk()
win.title('AnteaterDev')
win.geometry('500x300')
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

titulo = ctk.CTkLabel(master=win, text='GoySys-V-0.1', font=('Roboto', 10))
titulo.pack()

user_entry = ctk.CTkEntry(master=win, width=300, font=('Robot', 14),
placeholder_text='Nome do usuário')
user_entry.pack()

password_entry = ctk.CTkEntry(master=win, width=300, font=('Robot', 14),
placeholder_text='Senha do usuário', show='*')
password_entry.pack()

btn_login = ctk.CTkButton(master=win, width=300, text='Login',
font=('Robot', 14))
btn_login.pack()

win.mainloop()
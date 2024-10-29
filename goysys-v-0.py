import customtkinter as ctk 
from tkinter import *
import hashlib
import sqlite3


win0 = ctk.CTk()

class application():
    def __init__(self):
        self.win0 = win0
        self.tema()
        self.tela()
        self.tela_login()
        win0.mainloop()

    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def tela(self):
        win0.geometry('700x400')
        win0.title('LlBpSystem')
        #win0.iconbitmap('i.png')
        win0.resizable(False, False)

    def tela_login(self):
        img = PhotoImage(file='g.png')
        label_img = ctk.CTkLabel(master=win0, image=img)
        label_img.place(x=10, y=35)

        login_frame = ctk.CTkFrame(master=win0, width=350, height=396)
        login_frame.pack(side=RIGHT)

        label = ctk.CTkLabel(master=login_frame, text='GoySys-V-0', font=('Roboto', 20))
        label.place(x=120, y=5)

        self.username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome do Usuário", width=300,
        font=('Roboto', 14))
        self.username_entry.place(x=25, y=85)
        username_labe1 = ctk.CTkLabel(master=login_frame, text='*O campo nome do usuário é obrigatório',
        text_color='green', font=('Roboto', 12)).place(x=25, y=115)

        self.password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha do Usuário", width=300,
        font=('Roboto', 14), show='*')
        self.password_entry.place(x=25, y=165)
        password_labe = ctk.CTkLabel(master=login_frame, text='*O campo senha do usuário é obrigatório',
        text_color='green', font=('Roboto', 12)).place(x=25, y=195)

        chekbox = ctk.CTkCheckBox(master=login_frame, text='Lembrar usuário e senha').place(x=25, y=245)

        self.login_window = ctk.CTkToplevel(self.win0)

        def verificar_login():
            username = self.username_entry.get()
            password = self.password_entry.get()
            
            usuario_correto = 'admin'
            senha_correta = 'admin'

            if username == usuario_correto and password == senha_correta:
                self.abrir_proxima_tela()
                #self.login_window.quit()
                
                                            
            else:
                print('Usuário ou Senha invalidos.')
        
        button = ctk.CTkButton(master=login_frame, text='LOGIN', width=300, command=verificar_login)
        button.place(x=25, y=305)
    
    def abrir_proxima_tela(self):
        nova_tela = ctk.CTkToplevel(self.win0)
        nova_tela.title("Tela Principal")

        # Conteúdo da nova tela (exemplo)
        label = ctk.CTkLabel(nova_tela, text="Bem-vindo à tela principal!", font=("Roboto", 20))
        label.pack(pady=20)
        

       
application()

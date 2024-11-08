
import customtkinter as ctk
from tkinter import *

# Inicializa a janela de login
win0 = ctk.CTk()

class Application:
    def __init__(self):
        self.win0 = win0
        self.tema()
        self.tela()
        self.tela_login()
        #self.tela_principal = None #processo de retorno para tele de login
        win0.mainloop()

    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def tela(self):
        win0.geometry('700x400')
        win0.title('anteater.dev')
        win0.resizable(False, False)

    def tela_login(self):
        img = PhotoImage(file='goytaca-logo-original.png')
        label_img = ctk.CTkLabel(master=win0, image=img)
        label_img.place(x=10, y=35)

        login_frame = ctk.CTkFrame(master=win0, width=350, height=396)
        login_frame.pack(side=RIGHT)

        label = ctk.CTkLabel(master=login_frame, text='GoySys-V-0', font=('Roboto', 20))
        label.place(x=120, y=5)

        self.username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome do Usuário", width=300,
        font=('Roboto', 14))
        self.username_entry.place(x=25, y=85)
        username_label = ctk.CTkLabel(master=login_frame, text='*O campo nome do usuário é obrigatório',
        text_color='green', font=('Roboto', 12)).place(x=25, y=115)
        self.username_entry.bind('<Return>', lambda event: verificar_login())
        #self.username_entry.focus_set()

        self.password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha do Usuário", width=300,
        font=('Roboto', 14), show='*')
        self.password_entry.place(x=25, y=165)
        password_label = ctk.CTkLabel(master=login_frame, text='*O campo senha do usuário é obrigatório',
        text_color='green', font=('Roboto', 12)).place(x=25, y=195)
        self.password_entry.bind('<Return>', lambda event: verificar_login())

        ctk.CTkCheckBox(master=login_frame, text='Lembrar usuário e senha').place(x=25, y=245)

        def verificar_login():
            username = self.username_entry.get()
            password = self.password_entry.get()

            usuario_correto = 'admin'
            senha_correta = 'admin'

            if username == usuario_correto and password == senha_correta:
                self.win0.destroy()  # Fechar a janela de login
                self.abrir_proxima_tela()  # Abrir a tela inicial
            else:
                self.message_label = ctk.CTkLabel(master=login_frame, text="Usúario ou Senha inválidos", text_color="red", 
                font=("Roboto", 12))
                self.message_label.place(x=100, y=350)

        button = ctk.CTkButton(master=login_frame, text='LOGIN', width=300, command=verificar_login)
        button.place(x=25, y=305)

        # Tela principal
    
    def abrir_proxima_tela(self):
        # Cria uma nova janela principal após o login
        nova_tela = ctk.CTk()
        nova_tela.geometry("700x400")
        nova_tela.title("GoySys-V-0")
        nova_tela.resizable(False, False)

        img = PhotoImage(file='goytaca-logo-originalt.png')
        label_img = ctk.CTkLabel(master=nova_tela, image=img)
        label_img.place(x=180, y=55)

        # Conteúdo da nova tela principal
        label = ctk.CTkLabel(nova_tela, text="Bem-vindo ao Sistema Goytacá!", font=("Roboto", 20))
        label.pack(pady=20)

        button_cadastro = ctk.CTkButton(master=nova_tela, text='CADASTRO', font=('Roboto', 15), width=300, height=50)
        button_cadastro.place(x=25, y=85)

        button_consulta = ctk.CTkButton(master=nova_tela, text='CONSULTA', font=('Roboto', 15), width=300, height=50)
        button_consulta.place(x=370, y=85)

        button_estoque = ctk.CTkButton(master=nova_tela, text='ESTOUE', font=('Roboto', 15), width=300, height=50)
        button_estoque.place(x=25, y=175)

        button_relatorio = ctk.CTkButton(master=nova_tela, text='RELATÓRIO', font=('Roboto', 15), width=300, height=50)
        button_relatorio.place(x=370, y=175)

        button = ctk.CTkButton(master=nova_tela, text='CADASTRO', font=('Roboto', 15), width=300, height=50)
        button.place(x=25, y=265)

        button = ctk.CTkButton(master=nova_tela, text='CONSULTA', font=('Roboto', 15), width=300, height=50)
        button.place(x=370, y=265)

        # processo para retorno para tela de login
        #self.tela_principal = nova_tela
        #nova_tela.after_cancel(all) 

        button_troca_usuario = ctk.CTkButton(master=nova_tela, text='TROCAR USUÁRIO', font=('Roboto', 12), width=150, 
        fg_color=('gray20'), hover_color='green', command=self.voltar_tela_login)
        button_troca_usuario.place(x=100, y=345)

        button_sair = ctk.CTkButton(master=nova_tela, text='SAIR', font=('Roboto', 12), width=150, fg_color=('gray20'),
        hover_color='green', command=nova_tela.quit)
        button_sair.place(x=445, y=345)

        # Exibe a nova janela principal
        #nova_tela.mainloop()

    # processo para retorno para tela de login
    #def voltar_tela_login(self):
        #self.tela_principal.destroy()  # Destrói a tela principal atual
        #self.tela_login() # Chama a função tela_login novamente


# Inicializa a aplicação
Application()
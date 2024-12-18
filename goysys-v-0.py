
import customtkinter as ctk
from tkinter import *
from PIL import Image


# Inicializa a janela de login
win0 = ctk.CTk()

class Application:
    def __init__(self):
        self.win0 = win0
        self.tema()
        self.tela()
        self.tela_login()
        self.nova_tela = None #processo de retorno para tele de login
        win0.mainloop()

    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def tela(self):
        win0.geometry('700x400')
        win0.title('anteater.dev')
        win0.resizable(False, False)

    def tela_login(self):
        self.img_login = ctk.CTkImage(Image.open('goytaca-logo-original.png'), size=(320, 320))
        label_img = ctk.CTkLabel(master=win0, image=self.img_login)
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
                self.win0.withdraw()  # Fechar a janela de login
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
        self.nova_tela = ctk.CTk()
        self.nova_tela.geometry("700x400")
        self.nova_tela.title("GoySys-V-0")
        self.nova_tela.resizable(False, False)

        #self.img_login = ctk.CTkImage(Image.open('goytaca-logo-original.png'), size=(320, 320))
        #label_img = ctk.CTkLabel(master=nova_tela, image=self.img_login)
        #label_img.place(x=10, y=35)

        
        # Conteúdo da nova tela principal
        label = ctk.CTkLabel(self.nova_tela, text="Bem-vindo ao Sistema Goytacá!", font=("Roboto", 20))
        label.pack(pady=20)

        button_cadastro = ctk.CTkButton(master=self.nova_tela, text='CADASTRO', font=('Roboto', 15), width=300, height=50,
        command=self.janela_cadastro)
        button_cadastro.place(x=25, y=85)
                
        button_vigilantes = ctk.CTkButton(master=self.nova_tela, text='VIGILANTES', font=('Roboto', 15), width=300, height=50,
        command=self.janela_vigilantes)
        button_vigilantes.place(x=370, y=85)

        button_clientes = ctk.CTkButton(master=self.nova_tela, text='CLIENTES', font=('Roboto', 15), width=300, height=50,
        command=self.janela_clientes)
        button_clientes.place(x=25, y=175)

        button_financ = ctk.CTkButton(master=self.nova_tela, text='FINANCEIRO', font=('Roboto', 15), width=300, height=50,
        command=self.janela_financ)
        button_financ.place(x=370, y=175)

        button_sistema = ctk.CTkButton(master=self.nova_tela, text='SISTEMA', font=('Roboto', 15), width=300, height=50,
        command=self.janela_sistema)
        button_sistema.place(x=25, y=265)

        button_estoque = ctk.CTkButton(master=self.nova_tela, text='ESTOQUE', font=('Roboto', 15), width=300, height=50,
        command=self.janela_estoque)
        button_estoque.place(x=370, y=265)

        button_troca_usuario = ctk.CTkButton(master=self.nova_tela, text='TROCAR USUÁRIO', font=('Roboto', 12), width=150, 
        fg_color=('gray20'), hover_color='green', command=self.voltar_login) 
        button_troca_usuario.place(x=100, y=345)

        button_sair = ctk.CTkButton(master=self.nova_tela, text='SAIR', font=('Roboto', 12), width=150, fg_color=('gray20'),
        hover_color='green', command=self.nova_tela.quit)
        button_sair.place(x=445, y=345)

        self.nova_tela.mainloop()

    def voltar_login(self):
        if self.nova_tela is not None:
            self.nova_tela.withdraw()
        self.win0.deiconify()
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
    
    # Janela Cadastro
    def janela_cadastro(self):
        self.nova_tela.withdraw()
        nova_janela = ctk.CTk()
        nova_janela.title('GoySys-V-0')
        nova_janela.geometry('800x500')
        nova_janela.resizable(False, False)

        label = ctk.CTkLabel(nova_janela, text="Sistema de Cadastro", font=("Roboto", 20))
        label.pack(pady=20)

        def voltar_principal():
            nova_janela.withdraw()
            self.nova_tela.deiconify()
        
        button_voltar = ctk.CTkButton(master=nova_janela, text='Voltar', font=('Roboto', 12), width=150, fg_color=('gray20'),
        hover_color='green', command=voltar_principal)
        button_voltar.place(x=325, y=445)

        nova_janela.mainloop()
    
    # Janela Vigilantes
    def janela_vigilantes(self):
        self.nova_tela.withdraw()
        nova_janela = ctk.CTk()
        nova_janela.title('GoySys-V-0')
        nova_janela.geometry('800x500')
        nova_janela.resizable(False, False)

        label = ctk.CTkLabel(nova_janela, text="Sistema de Vigilantes", font=("Roboto", 20))
        label.pack(pady=20)

        def voltar_principal():
            nova_janela.withdraw()
            self.nova_tela.deiconify()
        
        button_voltar = ctk.CTkButton(master=nova_janela, text='Voltar', font=('Roboto', 12), width=150, fg_color=('gray20'),
        hover_color='green', command=voltar_principal)
        button_voltar.place(x=325, y=445)

        nova_janela.mainloop()

    # Janela Clientes
    def janela_clientes(self):
        self.nova_tela.withdraw()
        nova_janela = ctk.CTk()
        nova_janela.title('GoySys-V-0')
        nova_janela.geometry('800x500')
        nova_janela.resizable(False, False)

        label = ctk.CTkLabel(nova_janela, text="Sistema de Clientes", font=("Roboto", 20))
        label.pack(pady=20)

        def voltar_principal():
            nova_janela.withdraw()
            self.nova_tela.deiconify()
        
        button_voltar = ctk.CTkButton(master=nova_janela, text='Voltar', font=('Roboto', 12), width=150, fg_color=('gray20'),
        hover_color='green', command=voltar_principal)
        button_voltar.place(x=325, y=445)

        nova_janela.mainloop()
    
    # Janela Financeiro
    def janela_financ(self):
        self.nova_tela.withdraw()
        nova_janela = ctk.CTk()
        nova_janela.title('GoySys-V-0')
        nova_janela.geometry('800x500')
        nova_janela.resizable(False, False)

        label = ctk.CTkLabel(nova_janela, text="Sistema Financeiro", font=("Roboto", 20))
        label.pack(pady=20)

        def voltar_principal():
            nova_janela.withdraw()
            self.nova_tela.deiconify()
        
        button_voltar = ctk.CTkButton(master=nova_janela, text='Voltar', font=('Roboto', 12), width=150, fg_color=('gray20'),
        hover_color='green', command=voltar_principal)
        button_voltar.place(x=325, y=445)
    
    # Janela Sistema
    def janela_sistema(self):
        self.nova_tela.withdraw()
        nova_janela = ctk.CTk()
        nova_janela.title('GoySys-V-0')
        nova_janela.geometry('800x500')
        nova_janela.resizable(False, False)

        label = ctk.CTkLabel(nova_janela, text="Sistema", font=("Roboto", 20))
        label.pack(pady=20)

        def voltar_principal():
            nova_janela.withdraw()
            self.nova_tela.deiconify()
        
        button_voltar = ctk.CTkButton(master=nova_janela, text='Voltar', font=('Roboto', 12), width=150, fg_color=('gray20'),
        hover_color='green', command=voltar_principal)
        button_voltar.place(x=325, y=445)

    # Janela Estoque
    def janela_estoque(self):
        self.nova_tela.withdraw()
        nova_janela = ctk.CTk()
        nova_janela.title('GoySys-V-0')
        nova_janela.geometry('800x500')
        nova_janela.resizable(False, False)

        label = ctk.CTkLabel(nova_janela, text="Sistema de Estoque", font=("Roboto", 20))
        label.pack(pady=20)

        def voltar_principal():
            nova_janela.withdraw()
            self.nova_tela.deiconify()
        
        button_voltar = ctk.CTkButton(master=nova_janela, text='Voltar', font=('Roboto', 12), width=150, fg_color=('gray20'),
        hover_color='green', command=voltar_principal)
        button_voltar.place(x=325, y=445)

        nova_janela.mainloop()
       
       

# Inicializa a aplicação
Application()
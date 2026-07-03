"""
Módulo principal do sistema TVFEI-Python.
Este arquivo gerencia a inicialização do sistema, criação do usuário admin
e o loop principal de login e cadastro.
"""

import os
from admin import *
from favoritos import *
from usuarios import *
from videos import *
from menu import *

def main():
    """
    Função principal que executa o loop de entrada do sistema.
    Permite ao usuário se cadastrar, fazer login ou sair.
    """
    while True:
        print("\n1.Cadastrar")
        print("2.Login")
        print("3.Sair")

        op = input("Escolha: ")

        if op == "1":
            # Chama a função de cadastro de novo usuário
            cadastrar_usuario()
        elif op == "2":
            # Realiza o login e identifica o tipo de usuário (admin ou user)
            user, tipo = login()
            if user:
                if tipo == "admin":
                    menu_admin() # Menu para administradores
                else:
                    menu_usuario(user) # Menu para usuários comuns
        elif op == "3":
            # Encerra o programa
            break

def criar_admin():
    """
    Verifica se o arquivo de usuários existe e se o usuário admin padrão está criado.
    Caso não exista, cria o arquivo e adiciona o admin.
    """
    # Garante que o arquivo de usuários exista
    if not os.path.exists("usuarios.txt"):
        open("usuarios.txt", "w").close()

    # Verifica se o admin já está cadastrado (formato: nome;senha;tipo)
    with open("usuarios.txt", "r") as f:
        if not any("admin;admin;admin" in linha for linha in f):
            with open("usuarios.txt", "a") as f2:
                f2.write("admin;admin;admin\n")


# Inicializa o administrador padrão se necessário
criar_admin()

if __name__ == "__main__":
    # Inicia a execução do programa
    main()
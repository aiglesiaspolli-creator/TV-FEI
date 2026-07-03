"""
Módulo de gerenciamento de usuários do sistema TVFEI-Python.
Responsável pelo cadastro de novos usuários e autenticação (login).
"""

import os

def cadastrar_usuario():
    """
    Realiza o cadastro de um novo usuário comum.
    Verifica se o nome de usuário já existe antes de salvar.
    """
    nome = input("Nome: ")
    
    # Verifica duplicidade de usuário
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                if partes[0] == nome:
                    print("Usuário já existente!")
                    return

    senha = input("Senha: ")

    # Salva o novo usuário com o tipo 'user'
    with open("usuarios.txt", "a") as f:
        f.write(f"{nome};{senha};user\n")

    print("Usuário cadastrado!")


def login():
    """
    Autentica um usuário comparando nome e senha com os dados no arquivo.
    Retorna o nome e o tipo do usuário (admin ou user) se bem-sucedido.
    """
    nome = input("Nome: ")
    senha = input("Senha: ")

    if not os.path.exists("usuarios.txt"):
        print("Nenhum usuário cadastrado.")
        return None, None

    with open("usuarios.txt", "r") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                n, s, tipo = partes
                if n == nome and s == senha:
                    print("Login realizado!")
                    return nome, tipo

    print("Login inválido")
    return None, None
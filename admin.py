"""
Módulo de funções administrativas do sistema TVFEI-Python.
"""

import os

def listar_usuarios():
    """
    Lê o arquivo de usuários e exibe o nome e o tipo de cada um.
    """
    print("Usuários:")
    if not os.path.exists("usuarios.txt"):
        print("Nenhum usuário cadastrado.")
        return

    with open("usuarios.txt", "r") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                nome, _, tipo = partes
                print(f"{nome} ({tipo})")


def estatisticas():
    """
    Exibe estatísticas gerais do sistema, como total de usuários,
    total de vídeos e o ranking dos vídeos com mais curtidas.
    """
    # Conta total de usuários e vídeos
    total_usuarios = sum(1 for _ in open("usuarios.txt")) if os.path.exists("usuarios.txt") else 0
    total_videos = sum(1 for _ in open("videos.txt")) if os.path.exists("videos.txt") else 0

    print("Total de usuários:", total_usuarios)
    print("Total de vídeos:", total_videos)

    if total_videos == 0:
        print("Não há vídeos postados.")
        return

    videos = []
    # Coleta nome e curtidas de cada vídeo
    with open("videos.txt", "r") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) >= 2:
                nome = partes[0]
                likes = int(partes[1])
                videos.append((nome, likes))

    # Ordena os vídeos pelo número de curtidas (decrescente)
    videos.sort(key=lambda x: x[1], reverse=True)

    # Exibe os 5 vídeos mais curtidos
    print("\nTop 5 vídeos:")
    for v in videos[:5]:
        print(v[0], "-", v[1], "likes")

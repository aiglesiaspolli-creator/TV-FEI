"""
Módulo de gestão de vídeos favoritos do sistema TVFEI-Python.
"""

import os

def adicionar_favorito(usuario, video):
    """
    Adiciona um vídeo à lista de favoritos de um usuário.
    Garante que o mesmo vídeo não seja adicionado mais de uma vez para o mesmo usuário.
    """
    # Verifica se o vídeo já está nos favoritos
    if os.path.exists("favoritos.txt"):
        with open("favoritos.txt", "r") as f:
            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) == 2:
                    u, v = partes
                    if u == usuario and v == video:
                        print("Este vídeo já foi favoritado!")
                        return

    # Salva a relação usuário;vídeo
    with open("favoritos.txt", "a") as f:
        f.write(f"{usuario};{video}\n")

    print("Adicionado aos favoritos!")


def remover_favorito(usuario, video):
    """
    Remove um vídeo específico da lista de favoritos do usuário logado.
    """
    linhas = []
    # Lê todos os favoritos e filtra o que deve ser removido
    with open("favoritos.txt", "r") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 2:
                u, v = partes
                # Mantém na lista apenas o que NÃO é o alvo da remoção
                if not (u == usuario and v == video):
                    linhas.append(linha)

    # Re-escreve o arquivo com os favoritos restantes
    with open("favoritos.txt", "w") as f:
        f.writelines(linhas)

    print("Removido dos favoritos!")


def listar_favoritos(usuario):
    """
    Exibe no terminal todos os vídeos que o usuário favoritou.
    Retorna uma lista com os nomes dos vídeos encontrados.
    """
    print("Seus favoritos:")
    encontrados = []
    
    if not os.path.exists("favoritos.txt"):
        print("Nenhum favorito encontrado.")
        return encontrados

    with open("favoritos.txt", "r") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 2:
                u, v = partes
                if u == usuario:
                    print("-", v)
                    encontrados.append(v)
    
    if not encontrados:
        print("Nenhum favorito encontrado.")
    
    return encontrados

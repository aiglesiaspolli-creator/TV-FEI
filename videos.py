"""
Módulo de gerenciamento de vídeos do sistema TVFEI-Python.
Responsável pelas operações de CRUD (Criar, Ler, Atualizar, Deletar) de vídeos
e persistência em arquivo texto.
"""

import os

def cadastrar_video():
    """
    Solicita o nome de um vídeo e o salva no arquivo 'videos.txt'
    com valores iniciais de curtidas, descurtidas e visualizações zerados.
    """
    nome = input("Nome do vídeo: ")

    # Abre o arquivo em modo append ('a') para adicionar o novo vídeo
    with open("videos.txt", "a") as f:
        # Formato: nome;likes;dislikes;views
        f.write(f"{nome};0;0;0\n")

    print("Vídeo cadastrado!")


def excluir_video():
    """
    Remove um vídeo do sistema baseado no nome fornecido.
    Lida com a verificação de existência do arquivo e do vídeo.
    """
    tem_video = False
    # Verifica se existem vídeos cadastrados
    if os.path.exists("videos.txt"):
        with open("videos.txt", "r") as f:
            for linha in f:
                if linha.strip():
                    tem_video = True
                    continue
    
    if not tem_video:
        print("Não há vídeos postados")
        return

    nome_video = input("Nome do vídeo para excluir: ")

    linhas = []
    # Lê todos os vídeos, exceto o que será excluído
    with open("videos.txt", "r") as f:
        for linha in f:
            if not linha.startswith(nome_video + ";"):
                linhas.append(linha)

    # Sobrescreve o arquivo com a lista atualizada
    with open("videos.txt", "w") as f:
        f.writelines(linhas)

    print("Vídeo excluído!")


def adicionar_view(nome_video):
    """
    Incrementa o contador de visualizações de um vídeo específico.
    """
    linhas = []
    with open("videos.txt", "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(";")
            
            # Suporta formatos antigos e novos do arquivo
            if len(partes) == 4:
                nome, likes, dislikes, views = partes
            else:
                nome, likes = partes[0], partes[1]
                dislikes, views = "0", "0"
            
            # Incrementa views se o nome coincidir
            if nome == nome_video:
                views = str(int(views) + 1)
            linhas.append(f"{nome};{likes};{dislikes};{views}\n")

    # Atualiza o arquivo
    with open("videos.txt", "w") as f:
        f.writelines(linhas)


def buscar_video():
    """
    Busca vídeos pelo nome (case-insensitive) e exibe seus detalhes.
    Retorna o nome do vídeo selecionado pelo usuário.
    """
    busca = input("Buscar vídeo: ")

    encontrados = []
    with open("videos.txt", "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(";")
            
            # Parsing dos dados do vídeo
            if len(partes) == 4:
                nome, likes, dislikes, views = partes
            else:
                nome, likes = partes[0], partes[1]
                dislikes, views = "0", "0"
            
            # Filtro de busca
            if busca.lower() in nome.lower():
                print(f"{nome} | Curtidas: {likes} | Negativas: {dislikes} | Visualizações: {views}|")
                encontrados.append(nome)

    if not encontrados:
        print("Nenhum vídeo encontrado")
        return None

    # Lógica de seleção caso haja múltiplos resultados
    escolha = None
    if len(encontrados) == 1:
        escolha = encontrados[0]
    else:
        tentativa = input("Digite o nome do vídeo que deseja selecionar: ")
        if tentativa in encontrados:
            escolha = tentativa
        else:
            print("Vídeo inválido.")
            return None

    if escolha:
        # Registra a visualização ao selecionar o vídeo
        adicionar_view(escolha)
        return escolha


def curtir_video(nome_video):
    """
    Incrementa o contador de curtidas (likes) de um vídeo.
    """
    linhas = []
    with open("videos.txt", "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(";")
            if len(partes) == 4:
                nome, likes, dislikes, views = partes
            else:
                nome, likes = partes[0], partes[1]
                dislikes, views = "0", "0"
                
            if nome == nome_video:
                likes = str(int(likes) + 1)
            linhas.append(f"{nome};{likes};{dislikes};{views}\n")

    with open("videos.txt", "w") as f:
        f.writelines(linhas)

    print("Curtido!")


def negativar_video(nome_video):
    """
    Incrementa o contador de descurtidas (dislikes) de um vídeo.
    """
    linhas = []
    with open("videos.txt", "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(";")
            if len(partes) == 4:
                nome, likes, dislikes, views = partes
            else:
                nome, likes = partes[0], partes[1]
                dislikes, views = "0", "0"
                
            if nome == nome_video:
                dislikes = str(int(dislikes) + 1)
            linhas.append(f"{nome};{likes};{dislikes};{views}\n")

    with open("videos.txt", "w") as f:
        f.writelines(linhas)

    print("Negativado!")


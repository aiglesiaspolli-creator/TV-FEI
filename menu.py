"""
Módulo de menus do sistema TVFEI-Python.
Contém as interfaces de interação via terminal para usuários e administradores.
"""

from videos import *
from usuarios import *
from favoritos import *
from admin import *

def menu_usuario(usuario):
    """
    Exibe o menu de opções para um usuário comum logado.
    Permite buscar vídeos, interagir com eles e gerenciar favoritos.
    """
    while True:
        print("\n1.Buscar vídeo")
        print("2.Listar favoritos")
        print("3.Sair")

        op = input("Escolha: ")

        if op == "1":
            # Busca um vídeo por nome
            video_selecionado = buscar_video()
            if not video_selecionado:
                continue
            
            # Submenu de interação com o vídeo selecionado
            while True:
                print("\n1.Curtir")
                print("2.Negativar")
                print("3.Adicionar favorito")
                print("4.Voltar")

                op2 = input("Escolha: ")
                if op2 == "1":
                    curtir_video(video_selecionado)
                elif op2 == "2":
                    negativar_video(video_selecionado)
                elif op2 == "3":
                    adicionar_favorito(usuario, video_selecionado)
                elif op2 == "4":
                    break
        elif op == "2":
            # Lista os vídeos favoritados pelo usuário
            favoritos_encontrados = listar_favoritos(usuario)
            if not favoritos_encontrados:
                continue
                
            # Opção para remover um vídeo dos favoritos
            while True:
                print("\n1.Remover favorito")
                print("2.Voltar")
                op3 = input("Escolha: ")
                if op3 == "1":
                    # Se houver apenas um favorito, remove diretamente
                    if len(favoritos_encontrados) == 1:
                        remover_favorito(usuario, favoritos_encontrados[0])
                        break
                    else:
                        # Caso contrário, solicita o nome do vídeo a ser removido
                        vid = input("Digite o nome do vídeo para remover: ")
                        if vid in favoritos_encontrados:
                            remover_favorito(usuario, vid)
                            break
                        else:
                            print("Vídeo não encontrado na lista.")
                elif op3 == "2":
                    break
        elif op == "3":
            break


def menu_admin():
    """
    Exibe o menu de opções para usuários com privilégios de administrador.
    Permite gerenciar vídeos, visualizar usuários e estatísticas do sistema.
    """
    while True:
        print("\n1.Cadastrar vídeo")
        print("2.Excluir vídeo")
        print("3.Listar usuários")
        print("4.Estatísticas")
        print("5.Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_video()
        elif op == "2":
            excluir_video()
        elif op == "3":
            listar_usuarios()
        elif op == "4":
            estatisticas()
        elif op == "5":
            break
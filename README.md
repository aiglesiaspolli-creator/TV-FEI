# 📺 TV-FEI
> Plataforma de Transmissão e Gerenciamento de Vídeos em Python com Persistência em Arquivos e Controle de Acessos

O **TV-FEI** é um projeto acadêmico desenvolvido na **Centro Universitário FEI**. Inspirado no YouTube, o sistema é construído em Python com controle de acesso para dois perfis de usuários (Administrador e Usuário Comum), permitindo a navegação, interação com conteúdos e gerenciamento estatístico de vídeos.

---

## 📌 Funcionalidades

- **Módulo de Usuário (`USER`):**
  - Busca e navegação no catálogo de vídeos.
  - Sistema de interações: curtir conteúdos e adicionar vídeos à lista de favoritos.
  - Acesso ao histórico de favoritos salvos no perfil.

- **Módulo de Administração (`ADM`):**
  - Publicação e cadastro de novos vídeos no sistema.
  - Análise de métricas e estatísticas dos vídeos publicados (visualizações, curtidas, etc.).
  - Consulta e gerenciamento da base de usuários cadastrados.

- **Persistência de Dados:**
  - Armazenamento em arquivos de texto (`.txt`) para manutenção simples dos dados de usuários, favoritos e catálogo de vídeos sem dependência de banco de dados externo.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x:** Linguagem base para desenvolvimento de toda a lógica do sistema e menus.
- **Arquivos Texto (`.txt`):** Persistência simples e leitura/escrita de dados (`favoritos.txt`, `usuarios.txt`, `videos.txt`).

---

## 📂 Estrutura do Repositório

```text
├── admin.py       # Funções administrativas (postagem de vídeos, estatísticas, consulta)
├── favoritos.py   # Gerenciamento das interações de favoritos dos usuários
├── favoritos.txt  # Persistência de dados das listas de favoritos
├── main.py        # Ponto de entrada da aplicação e inicialização do sistema
├── menu.py        # Estrutura de navegação e fluxos de telas no terminal
├── usuarios.py    # Lógica de autenticação e cadastro de usuários
├── usuarios.txt  # Persistência de dados dos usuários cadastrados
├── videos.py      # Lógica de listagem, busca e interações de vídeos
├── videos.txt    # Persistência de dados do catálogo de vídeos
└── README.md      # Documentação do repositório

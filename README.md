# Gerador HTML 🌐

Um script simples e eficiente em Python que permite baixar o código fonte de qualquer página da web e salvá-lo localmente como um arquivo `.html`.

## 🚀 Funcionalidades

* **Download de HTML:** Captura o conteúdo de uma URL fornecida pelo usuário através de requisições HTTP.
* **Salvamento Personalizado:** Permite definir o nome do arquivo de saída de forma dinâmica.
* **Validação Simples:** Possui uma verificação básica para evitar espaços em branco nas entradas, prevenindo erros no sistema de arquivos.
* **Interface em Loop:** Menu interativo que permite converter múltiplos sites em sequência sem a necessidade de reiniciar o programa.

## 🛠️ Tecnologias Utilizadas

* **Python 3**: Linguagem base do projeto.
* **Biblioteca Requests**: Utilizada para realizar as requisições e obter o conteúdo das páginas web.

## 📦 Como Instalar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca necessária via terminal:
   ```bash
   pip install requests

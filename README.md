# 📒 Agenda de Contatos - Python

## 📖 Sobre o Projeto

Este projeto foi desenvolvido durante o curso **"Introdução ao Python e Algoritmos"** ofertado pela **Solyd Offensive Security**. 

Durante o desenvolvimento, foi possível aprender e aplicar conceitos fundamentais de programação, incluindo:

- **Lógica de programação** - Estruturação de algoritmos e resolução de problemas
- **Laços de repetição** - Utilização de `for` para iterar sobre coleções e `while` para criar menus interativos
- **Estruturas condicionais** - Implementação de `if`, `elif` e `else` para controle de fluxo
- **Manipulação de arquivos** - Leitura e escrita em arquivos CSV
- **Estruturas de dados** - Uso de dicionários para organizar informações
- **Tratamento de exceções** - Implementação de `try/except` para lidar com erros
- **Funções** - Modularização do código para melhor organização e reutilização

## 🚀 Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Mostrar todos os contatos** - Visualiza todos os contatos salvos na agenda
2. **Buscar contato** - Pesquisa um contato específico pelo nome
3. **Adicionar contato** - Cadastra um novo contato com telefone, e-mail e endereço
4. **Editar contato** - Modifica as informações de um contato existente
5. **Excluir contato** - Remove um contato da agenda
6. **Exportar contatos** - Salva os contatos em um arquivo CSV personalizado
7. **Importar contatos** - Carrega contatos de um arquivo CSV externo

## 📋 Pré-requisitos

- Python 3.x instalado no sistema
- Sistema operacional: Linux, Windows ou macOS

## 🔧 Como Usar

### 1. Clone ou baixe o projeto

```bash
cd /caminho/do/projeto/contactList
```

### 2. Execute o programa

```bash
python3 adressBook.py
```

### 3. Navegue pelo menu

Após executar o programa, você verá o seguinte menu:

```
----- AGENDA -----
1 - Mostrar todos os contatos da agenda
2 - Buscar contato
3 - Adicionar contato
4 - Editar contato
5 - Excluir contato
6 - Exportar contatos .CSV
7 - Importar contatos
0 - Fechar agenda
------------------
```

Digite o número da opção desejada e pressione Enter.

### 4. Adicionar um contato

1. Escolha a opção `3`
2. Digite o nome do contato
3. Informe o telefone (ex: 99 9 9999-9999)
4. Informe o e-mail
5. Informe o endereço

Os dados serão salvos automaticamente no arquivo `database.csv`.

### 5. Exportar/Importar contatos

**Exportar:**
- Escolha a opção `6`
- Digite o nome do arquivo desejado (ex: `meus_contatos.csv`)

**Importar:**
- Escolha a opção `7`
- Digite o nome do arquivo a ser importado
- O arquivo deve estar no formato CSV: `Nome,Telefone,Email,Endereço`

### 6. Formato do arquivo CSV

Os arquivos devem seguir o formato:

```csv
João Silva,99 9 1234-5678, joao@email.com, Rua das Flores
Maria Santos,99 9 8765-4321, maria@email.com, Av. Central
```

## 📁 Estrutura de Arquivos

```
contactList/
│
├── adressBook.py      # Arquivo principal do programa
├── database.csv       # Banco de dados dos contatos (gerado automaticamente)
└── README.md          # Este arquivo
```

## 💡 Dicas de Uso

- Os contatos são salvos automaticamente ao adicionar, editar ou excluir
- O arquivo `database.csv` é carregado automaticamente ao iniciar o programa
- Você pode fazer backup exportando para outro arquivo CSV
- Para sair do programa, escolha a opção `0`

## 👨‍💻 Autor

Desenvolvido por Ytalo Teixeira durante o curso da Solyd Offensive Security.

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.

---

⭐ **Solyd Offensive Security** - Introdução ao Python e Algoritmos

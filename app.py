"""

Sistema simples de cadastro de produtos com SQLite.

"""
import sqlite3

#  adiciona a conexão com o banco de dados SQlite
conexao = sqlite3.connect("produtos.db")
cursor = conexao.cursor()

# Cria a tabela se ela ainda não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )
""")
conexao.commit()

# cadastra um produto no banco de dados
def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço (ex: 19.90): "))
    quantidade = int(input("Quantidade em estoque: "))

    cursor.execute(
        "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
        (nome, preco, quantidade)
    )
    conexao.commit()
    print(f"\nProduto '{nome}' cadastrado com sucesso!\n")

# lista todos os produtos cadastrados no banco de dados
def listar_produtos():
    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
    produtos = cursor.fetchall()

    if len(produtos) == 0:
        print("\nNenhum produto cadastrado ainda.\n")
        return

    print("\n--- Lista de Produtos ---")
    for produto in produtos:
        id_produto, nome, preco, quantidade = produto
        print(f"ID: {id_produto} | Nome: {nome} | Preço: R$ {preco:.2f} | Estoque: {quantidade}")
    print("-------------------------\n")

# busca produtos pelo nome (ou parte do nome) no banco de dados
def buscar_produto():
    nome_busca = input("Digite o nome (ou parte do nome) do produto: ")

    cursor.execute(
        "SELECT id, nome, preco, quantidade FROM produtos WHERE nome LIKE ?",
        ("%" + nome_busca + "%",)
    )
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("\nNenhum produto encontrado com esse nome.\n")
        return

    print("\n--- Resultado da Busca ---")
    for produto in resultados:
        id_produto, nome, preco, quantidade = produto
        print(f"ID: {id_produto} | Nome: {nome} | Preço: R$ {preco:.2f} | Estoque: {quantidade}")
    print("--------------------------\n")

# atualiza a quantidade em estoque de um produto no banco de dados
def atualizar_estoque():
    id_produto = int(input("Digite o ID do produto: "))
    nova_quantidade = int(input("Nova quantidade em estoque: "))

    cursor.execute(
        "UPDATE produtos SET quantidade = ? WHERE id = ?",
        (nova_quantidade, id_produto)
    )
    conexao.commit()

    if cursor.rowcount == 0:
        print("\nProduto não encontrado.\n")
    else:
        print("\nEstoque atualizado com sucesso!\n")

# remove um produto do banco de dados pelo ID do produto
def remover_produto():
    id_produto = int(input("Digite o ID do produto que deseja remover: "))

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conexao.commit()

    if cursor.rowcount == 0:
        print("\nProduto não encontrado.\n")
    else:
        print("\nProduto removido com sucesso!\n")

#  faz um relatório de preços dos produtos cadastrados no banco de dados
def relatorio_precos():
    
    cursor.execute("SELECT preco FROM produtos")
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print("\nNenhum produto cadastrado ainda.\n")
        return

    # monta uma lista simples só com os preços (tira da lista de tuplas)
    lista_precos = []
    for linha in resultado:
        lista_precos.append(linha[0])

    preco_maximo = max(lista_precos)
    preco_minimo = min(lista_precos)
    preco_medio = sum(lista_precos) / len(lista_precos)
    lista_ordenada = sorted(lista_precos)

    print("\n--- Relatório de Preços ---")
    print(f"Quantidade de produtos: {len(lista_precos)}")
    print(f"Preço mais caro: R$ {preco_maximo:.2f}")
    print(f"Preço mais barato: R$ {preco_minimo:.2f}")
    print(f"Preço médio: R$ {preco_medio:.2f}")
    print(f"Preços em ordem crescente: {lista_ordenada}")
    print("---------------------------\n")

# mostra o menu principal do sistema
def mostrar_menu():
    print("===== SISTEMA DE CADASTRO DE PRODUTOS =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar estoque")
    print("5 - Remover produto")
    print("6 - Relatório de preços")
    print("7 - Sair")


# loop principal do sistema, que exibe o menu e processa as opções escolhidas pelo usuário
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        buscar_produto()
    elif opcao == "4":
        atualizar_estoque()
    elif opcao == "5":
        remover_produto()
    elif opcao == "6":
        relatorio_precos()
    elif opcao == "7":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")

# fecha a conexão com o banco de dados antes de encerrar o programa
conexao.close()

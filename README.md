# Sistema de Cadastro de Produtos

Projeto simples em **Python + SQL (SQLite)** para praticar lógica de programação e comandos SQL básicos, aplicando em Python a lógica de programação estudada em Java.

## Funcionalidades
- Cadastrar produto
- Listar todos os produtos
- Buscar produto por nome
- Atualizar quantidade em estoque
- Remover produto
- Relatório de preços (usa lista para calcular maior, menor, média e ordenar)

## Tecnologias
- Python 3
- SQLite (biblioteca `sqlite3`, nativa do Python — não precisa instalar nada)

## Pré-requisitos
- Ter o Python 3 instalado ([python.org](https://www.python.org/downloads/))

## Como rodar

```bash
git clone https://github.com/mariliamezalheiradev/projeto-simples-py-sql.git
cd projeto-simples-py-sql
python app.py
```

O banco de dados (`produtos.db`) é criado automaticamente na primeira execução, junto com a tabela `produtos`.

## Exemplo de uso

```
===== SISTEMA DE CADASTRO DE PRODUTOS =====
1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto
4 - Atualizar estoque
5 - Remover produto
6 - Relatório de preços
7 - Sair
Escolha uma opção:
```

## Estrutura do banco de dados

Tabela `produtos`:

| Campo      | Tipo    | Descrição                  |
|------------|---------|-----------------------------|
| id         | INTEGER | Identificador único (auto)  |
| nome       | TEXT    | Nome do produto              |
| preco      | REAL    | Preço do produto             |
| quantidade | INTEGER | Quantidade em estoque        |

## O que o projeto pratica
- Estruturas condicionais (`if`/`elif`/`else`)
- Loop (`while`)
- Funções
- Listas (`append`, `sorted`, `max`, `min`, `sum`, `len`)
- Comandos SQL: `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- Consultas parametrizadas (proteção contra SQL Injection)

Projeto desenvolvido como parte dos estudos de lógica de programação e banco de dados.
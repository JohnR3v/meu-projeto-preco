import sqlite3
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = BASE_DIR / "produtos.db"


def conectar():
    conn = sqlite3.connect(DB_NAME)
    criar_tabela(conn)
    return conn


def criar_tabela(conn):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            nome TEXT,
            mercado TEXT,
            preco_anterior REAL,
            preco_atual REAL,
            data_registro TEXT,
            PRIMARY KEY (nome, mercado)
        )
        """
    )
    conn.commit()


def buscar_produto(conn, nome, mercado):
    return conn.execute(
        "SELECT preco_anterior, preco_atual, data_registro FROM produtos WHERE nome = ? AND mercado = ?",
        (nome, mercado),
    ).fetchone()


def salvar_produto(conn, nome, mercado, preco_anterior, preco_atual):
    data_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    conn.execute(
        """
        INSERT INTO produtos (nome, mercado, preco_anterior, preco_atual, data_registro)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(nome, mercado) DO UPDATE SET
            preco_anterior = excluded.preco_anterior,
            preco_atual = excluded.preco_atual,
            data_registro = excluded.data_registro
        """,
        (nome, mercado, preco_anterior, preco_atual, data_registro),
    )
    conn.commit()


def remover_produto(conn, nome, mercado):
    conn.execute(
        "DELETE FROM produtos WHERE nome = ? AND mercado = ?",
        (nome, mercado),
    )
    conn.commit()


def listar_produtos(conn):
    return conn.execute(
        "SELECT nome, mercado, preco_atual FROM produtos ORDER BY nome, mercado"
    ).fetchall()

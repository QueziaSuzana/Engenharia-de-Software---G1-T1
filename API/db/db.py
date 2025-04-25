import sqlite3

from typing import List

from models.empresas import Empresas
from models.empresas_setores import EmpresasSetores


import logging

logging.basicConfig(filename="logs.log", level=logging.INFO)

def create_connection():
    conn = sqlite3.connect('db/database.db')
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empresas_setores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fk_cnpj TEXT NOT NULL,
            setor TEXT NOT NULL,
            total_funcionarios INTEGER NOT NULL,
            qtd_homens INTEGER NOT NULL,
            qtd_mulheres INTEGER NOT NULL,
            idade_media_homens REAL NOT NULL,
            idade_media_mulheres REAL NOT NULL,
            FOREIGN KEY (fk_cnpj) REFERENCES empresas(cnpj)
        );''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            cnpj TEXT UNIQUE NOT NULL,
            endereco TEXT NOT NULL,
            setor_atividade TEXT NOT NULL
        );''')


    conn.commit()
    conn.close()

def insert_from_text(file_path):
    conn = create_connection()
    cursor = conn.cursor()

    with open(file_path, 'r') as file:
        last_company_name = None
        for line in file:
            data = line.strip().split(',')
            if not last_company_name:
                last_company_name = data[0]
            
            if last_company_name != data[0]:
                last_company_name = data[0]

                data_empresa = (data[0], data[1], data[2], data[3])
                cursor.execute('''
                    INSERT INTO empresas (nome, cnpj, endereco, setor_atividade)
                    VALUES (?, ?, ?, ?)
                ''', data_empresa)

            data_empresa_setor = (data[1], data[4], data[5], data[6], data[7], data[8], data[9])

            cursor.execute('''
                INSERT INTO empresas_setores (fk_cnpj, setor, total_funcionarios, qtd_homens, qtd_mulheres, idade_media_homens, idade_media_mulheres)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', data_empresa_setor)

    conn.commit()
    conn.close()

def get_all_companies() -> List[Empresas]:
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM empresas
    ''')

    data = cursor.fetchall()
    conn.close()

    logging.info(f"Getting all companies: {data}")

    return Empresas.from_list(data)

def get_all_companies_sectors() -> List[EmpresasSetores]:
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM empresas_setores
    ''')

    data = cursor.fetchall()

    conn.close()
    
    print(data[0])

    return EmpresasSetores.from_list(data)

def get_company_by_cnpj(cnpj) -> Empresas:
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM empresas WHERE cnpj = ?
    ''', (cnpj,))
    data = cursor.fetchone()
    conn.close()

    return Empresas.from_tuple(data)


def get_company_sectors_by_cnpj(cnpj) -> List[EmpresasSetores]:
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM empresas_setores WHERE fk_cnpj = ?
    ''', (cnpj,))
    data = cursor.fetchall()
    conn.close()

    return EmpresasSetores.from_list(data)


create_table()

# run only once
#insert_from_text('db/mock_text.txt')

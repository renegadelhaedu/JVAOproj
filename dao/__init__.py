import psycopg2 as ps

def conectar_bd():
    con = ps.connect(
        host='localhost',
        database='mercadinho',
        user='postgres',
        password='12345'
    )
    return con

def inserir_usuario(nome, email, senha, tipo):
    conexao = conectar_bd()

    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuarios (nome, email, senha, tipo) VALUES ('{nome}', '{email}', '{senha}', '{tipo}' )"
        cur.execute(sql)
    except ps.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito

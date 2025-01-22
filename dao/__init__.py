import psycopg2

def conectardb():

    con = psycopg2.connect(

        #host='localhost',
        #database = 'server',
        #user = 'postgres',
        #password = '12345'
        host = 'dpg-cu8fuutds78s73a7nlag-a.oregon-postgres.render.com',
        database = 'pedrofitness',
        user = 'pedrofitness_user',
        password = 'dtEPT94YqmR6yYb8kcrVjubQtZgEcJj8'
    )
    return con


def login(login,senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT * from usuarios where login='{login}' and senha='{senha}'  "
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida

def inserir_user(login,senha,nome):

    conn = conectardb()
    cur = conn.cursor()

    try:
        sql = f"INSERT INTO usuarios (login, senha, nome) VALUES ('{login}','{senha}','{nome}')"
        cur.execute(sql)


    except psycopg2.IntegrityError:
        conn.rollback()
        print('1')
        exito = False
    else:
        print('2')
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def listausuarios():
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT  nome, login from usuarios"
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()
    return saida

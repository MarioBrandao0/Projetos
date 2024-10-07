import mysql.connector

def banco(host1, senha, usuario, banco):
    return mysql.connector.connect(
        host = host1,
        user = usuario,
        password = senha,
        database = banco

)

def armazenar(cursor, user, password):
    inserir = f'INSERT INTO logins(nome, senha) VALUES(%s, %s)'
    cursor.execute(inserir, (user, password))

def main(usuario, senha):
    try:
        conexao = banco(host1='localhost',senha='teste',usuario='root',banco='Login_site')
        cursor = conexao.cursor()
        armazenar(cursor=cursor, user=usuario, password=senha)
        
        conexao.commit()
    except Exception as e:
        print(f'Houve um erro: {e}')
    finally:
        cursor.close()
        conexao.close()

if __name__ == '__main__':
    main(usuario='', senha='')
import mysql.connector

def banco(hosti, usuario, senha, banco):
    return mysql.connector.connect(
        host = hosti,
        user = usuario,
        password = senha,
        database = banco
    )

def registrar_user(cursor):
    login = str(input('Digite o novo login: '))
    senha = str(input('Digite uma senha: '))
    inserir_user = f'INSERT INTO users (login, senha) VALUES ("{login}", "{senha}")'
    cursor.execute(inserir_user)
    print(f'Usuario {login} foi criado com sucesso')

def logins(cursor, result):
    l_login = []
    valores = 'SELECT * FROM users'
    cursor.execute(valores)
    login = cursor.fetchall()
    for dados in login:
        d_login = {}
        d_login['Login'] = dados[1]
        d_login['Senha'] = dados[2]
        l_login.append(d_login)
    return l_login
    #esta adicionando

def main(l_login):
    try:
        conexao = banco(hosti='localhost', usuario='root', senha='teste', banco='P_user')
        cursor = conexao.cursor()
        if __name__ == '__main__':
            escolha = str(input('Registrar/Alterar/Excluir: ')).upper()
            if escolha == 'REGISTAR':
                registrar_user(cursor=cursor)
            #adicionar mais funcionalidades
        
        l_logins = logins(cursor=cursor, result='')
        return l_logins  

        conexao.commit()
    
    except Exception as e:
        print(f'Houve um erro {e}')
    finally:
        conexao.close()
        cursor.close()

main(l_login= '')

import mysql.connector

def BancoBackup(hosti, usuario, senha, banco):
    return mysql.connector.connect(
        host = hosti,
        user = usuario,
        password = senha,
        database = banco
)

def Backup(cursor, NomesBp):
    for dado in NomesBp:
        inserir = 'INSERT INTO dados_backup(nome, sexo, idade, email, telefone, cidade) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (dado[1], dado[2], dado[3], dado[4], dado[5], dado[6])
        cursor.execute(inserir, valores)

def main(nomesBp):
    conexao = BancoBackup(hosti='localhost', usuario='root', senha='teste', banco='Backup_bd')
    cursor = conexao.cursor()
    #programa principal
    Backup(cursor=cursor, NomesBp=nomesBp)
    
    conexao.commit()
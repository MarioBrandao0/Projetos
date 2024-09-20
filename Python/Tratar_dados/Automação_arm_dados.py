import pandas as pd
import mysql.connector

#ler aquivo
df = pd.read_excel('Dados(1).xlsx')

#banco de dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'Akeatorii',
    password = 'aleatorio',
    database = 'Dados_excel',
)
cursor = conexao.cursor()

#Comandos
for index_n_usa, row in df.iterrows():
    inserir = 'INSERT INTO dados (nome, sexo, idade, email, telefone, cidade) VALUES(%s, %s, %s, %s, %s, %s)'
    valores = (row["nome"], row["sexo"], row["idade"], row["email"], row["telefone"], row["cidade"])
    cursor.execute(inserir, valores)
conexao.commit()
print(f'{cursor.rowcount}, registros inseridos com sucesso')

#Selecionar dados e imprimir
'''cursor.execute('SELECT * FROM dados')

dados = cursor.fetchall()
for linha in dados:
    print('-'*30)
    for linha2 in linha:
        print(linha2)'''
    
#Finalizar conexão
cursor.close()
conexao.close()

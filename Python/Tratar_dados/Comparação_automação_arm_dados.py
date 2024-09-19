import pandas as pd
import mysql.connector

#ler aquivo
df = pd.read_excel('Dados(1).xlsx')


#banco de dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'teste',
    database = 'Dados_excel',
)


cursor = conexao.cursor()

cursor.execute('SELECT * FROM dados')
dados_tabela = cursor.fetchall()
#Comandos

'''for index_n_usa, row in df.iterrows():
    # Valores a serem inseridos
    valores = (row["nome"], row["sexo"], row["idade"], row["email"], row["telefone"], row["cidade"])
    
    # Verificar se os dados já existem
    consulta = 'SELECT COUNT(*) FROM dados WHERE nome = %s AND sexo = %s AND idade = %s AND email = %s AND telefone = %s AND cidade = %s'
    cursor.execute(consulta, valores)
    
    # Recuperar o resultado da contagem
    resultado = cursor.fetchone()

    if resultado[0] > 0:#Caso a lista tenha algum valor
        print(f'Dados já existentes: {valores}')
        break  # Pula para a próxima iteração do loop

    # Inserir os dados, caso não existam
    inserir = 'INSERT INTO dados (nome, sexo, idade, email, telefone, cidade) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(inserir, valores)'''

for index_n_usa, row in df.iterrows():
    consulta = 'SELECT COUNT * FROM dados WHERE nome = %s, sexo = %s, idade = %s, telefone = %s, email = %s, cidade = %s'
    valores = (row["nome"], row["sexo"], row["idade"], row["email"], row["telefone"], row["cidade"])
    cursor.execute(consulta, valores)
    resultado = cursor.fetchone()
    if resultado[0] > 0:
        print('resultados ja existem')
        break#Caso exista encerra aqui
    #caso nao exista, continua
    inserir = 'INSERT INTO dados (nome, sexo, idade, email, telefone, cidade) VALUES(%s, %s, %s, %s, %s, %s)'
    valores = (row["nome"], row["sexo"], row["idade"], row["email"], row["telefone"], row["cidade"])
    cursor.execute(inserir, valores)
conexao.commit()
print(f'{cursor.rowcount}, registros inseridos com sucesso')

'''cursor.execute('SELECT * FROM dados')

dados = cursor.fetchall()
for linha in dados:
    print('-'*30)
    for linha2 in linha:
        print(linha2)'''
    

#Finalizar conexão
cursor.close()
conexao.close()


#comparar:

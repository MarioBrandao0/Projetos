import pandas as pd
import mysql.connector

#ler aquivo
df = pd.read_excel('Caminho do arquivo')

#banco de dados
conexao = mysql.connector.connect(
    host = 'Seu host',
    user = 'Seu User',
    password = 'Sua senha',
    database = 'Sua base de dados',
)


cursor = conexao.cursor()


#Listas
lista_excel = []
lista_Nsql = []
#-----------------------------
resposta = ''
consultar = 'SELECT nome FROM tabela;'
cursor.execute(consultar)
resposta = cursor.fetchall()


#transformar os dados da tabela em listas
for index_n_usa, row in df.iterrows():
    v_consulta = (row["nome"])
    lista_excel.append(v_consulta)

#filtrar e transformar a tabela do mysql em lista:
for lista_sql in resposta:
    for nome in lista_sql:
        lista_Nsql.append(nome)
#print(lista_Nsql)

#adcionar valores. caso esxista, adcionar os que não existe
setada1 = set(lista_Nsql)
setada2 = set(lista_excel)
valores_faltando = setada2 - setada1
#comparando se tem valor faltando
if valores_faltando:
    for index_n_usa, row in df.iterrows():
        inserir = 'INSERT INTO tabela (nome, sexo, idade, email, telefone, cidade) VALUES(%s, %s, %s, %s, %s, %s)'
        valores = (row["nome"], row["sexo"], row["idade"], row["email"], row["telefone"], row["cidade"])
        cursor.execute(inserir, valores)
        print(f'Os novos valores: {valores_faltando} Foram adcionados')
else:
    print('Os valores do banco e do excel são igauis')
conexao.commit()

#encerrando conexão
cursor.close()
conexao.close()


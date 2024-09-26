import pandas as pd
import mysql.connector

def abrir_arquivo(caminho):
    return (pd.read_excel(caminho))

def conexao_banco(hosti, usuario, senha, banco):
    return mysql.connector.connect(
        host=hosti,
        user=usuario,
        password=senha,
        database=banco
    )

def obter_nome_bancos(cursor):
    lista_sql1 = []
    cursor.execute('SELECT nome FROM dados')
    resposta = cursor.fetchall()
    for lista in resposta:
        for nome in lista:
            lista_sql1.append(nome)
    return lista_sql1

def extrair_nome_df(df):
    lista_excel1 = []
    for index_n_usa, row in df.iterrows():
        v_consulta = (row["nome"])
        if v_consulta:
            lista_excel1.append(v_consulta)
    return lista_excel1

def comparar_listas(lista_sql, lista_excel):
    setada1 = set(lista_excel)
    setada2 = set(lista_sql)
    comparar = setada1 - setada2
    return comparar

def adicionar_valores(cursor, df):
    for index_n_usa, row in df.iterrows():
        inserir = 'INSERT INTO dados (nome, sexo, idade, email, telefone, cidade) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (row["nome"], row["sexo"], row["idade"], row["email"], row["telefone"], row["cidade"])
        cursor.execute(inserir, valores)

def main():
    try:
        #arquivo
        df = abrir_arquivo('Dados(2).xlsx')
        #conexão
        conexao = conexao_banco('localhost','root', 'teste', 'Dados_excel')
        cursor = conexao.cursor()

        #lista
        nomes_excel = extrair_nome_df(df=df,)
        nomes_tabela =obter_nome_bancos(cursor=cursor)

        #verificar valores faltando
        valores_faltando = comparar_listas(lista_sql=nomes_tabela, lista_excel=nomes_excel)


        if valores_faltando:
            adicionar_valores(cursor=cursor, df=df)
            print(f'Valores faltantes: {valores_faltando} Foram adicionado com sucesso ')
        else:
            print('Valores do excel ja inseridos')
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        print('Houver algum erro')

if __name__ == '__main__':
    main()

#Isso foi um teste para o Github direto do vsCode
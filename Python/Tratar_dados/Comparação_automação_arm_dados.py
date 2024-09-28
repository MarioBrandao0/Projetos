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

def atualizar_valores(cursor):
    nome = str(input('Nome da pessoa: ')).capitalize()
    v_trocar = str(input('O que deseja trocar: '))
    novo_valor = str(input(f'Digite o novo {v_trocar}:'))

    atualizar = f'UPDATE dados SET {v_trocar} = "{novo_valor}" WHERE nome = "{nome}"'
    cursor.execute(atualizar)
    print(f'O {v_trocar} de {nome} foi atualizado com sucesso: ')

def excluir_cliente(cursor):
    print('----Excluir----')
    nome = str(input('Nome do cliente:'))
    excluir = f'DELETE FROM dados WHERE nome = "{nome}"'
    cursor.execute(excluir)
    print(f'Cliente {nome} excluido com sucesso')
def main():
    try:
        #Conexão com banco
        conexao = conexao_banco('localhost','root', 'teste', 'Dados_excel')
        cursor = conexao.cursor()
        
        escolha = str(input('O que você deseja fazer? [Atualizar/Registrar/Excluir]')).upper()
        if escolha == 'REGISTRAR':
            arquivo = str(input('Caminho do arquivo: ')).strip()
            
            #arquivo
            df = abrir_arquivo(arquivo)
            #conexão


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
        
        elif escolha == 'ATUALIZAR':
            atualizar_valores(cursor=cursor)
        elif escolha == 'EXCLUIR':
            excluir_cliente(cursor=cursor)
        
        conexao.commit()
        cursor.close()
        conexao.close()
    except Exception as e:
        print(f'Houve um erro {e}')
if __name__ == '__main__':
    main()

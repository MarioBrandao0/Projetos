# Documentação do Código
(Atualizar documentação)
## Descrição
Este código é um projeto que permite interagir com um banco de dados MySQL para gerenciar informações de usuários. Ele suporta operações de registro, atualização e exclusão de dados, além de realizar validações de login. Os dados podem ser importados de um arquivo Excel.

## Estrutura do Código

### Importações
- `pandas`: Utilizado para manipulação de dados, especialmente para ler arquivos Excel.
- `mysql.connector`: Usado para estabelecer conexões com um banco de dados MySQL.
- `Validação_user`: Um arquivo que tem como funcionalidade fazer uma verificação para se conectar ao banco.

### Funções

1. **abrir_arquivo(caminho)**:
   - Lê um arquivo Excel e retorna um DataFrame.

2. **conexao_banco(hosti, usuario, senha, banco)**:
   - Estabelece uma conexão com o banco de dados MySQL e retorna o objeto de conexão.

3. **obter_nome_bancos(cursor)**:
   - Executa uma consulta SQL para obter os nomes de todos os usuários no banco de dados.

4. **extrair_nome_df(df)**:
   - Extrai os nomes do DataFrame e retorna uma lista de nomes.

5. **comparar_listas(lista_sql, lista_excel)**:
   - Compara duas listas e retorna os valores que estão na lista do Excel, mas não na lista do banco de dados.

6. **adicionar_valores(cursor, df)**:
   - Adiciona novos registros ao banco de dados com base nos dados do Dataframe(Caso ja exista o mesmo valor, ele so ira adicionar os valores que não estão na tabela).

7. **atualizar_valores(cursor)**:
   - Permite ao usuário atualizar um valor específico de um usuário existente no banco de dados.

8. **excluir_cliente(cursor)**:
   - Permite ao usuário excluir um cliente com base no nome.

9. **main()**:
   - Função principal que gerencia a lógica do programa. Realiza a conexão com o banco de dados, valida o login e chama as funções apropriadas com base na escolha do usuário.

## Considerações Finais
Este projeto ainda está em desenvolvimento e será atualizado com melhorias de segurança, validação de entradas e tratamento de erros para tornar o sistema mais robusto e confiável.

# OBS:Projeto pessoal


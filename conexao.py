import mysql.connector

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='20010828Mv@#',
        database='db_financeiro',
    )

    if conexao.is_connected():
        print("Conexão bem-sucedida!")

    cursor = conexao.cursor()

    cursor.close()
    conexao.close()

except mysql.connector.Error as erro:
    print("Erro ao conectar ao banco de dados:", erro)

#DELETE
#nome2 = "João"
#comando = f'DELETE FROM usuario WHERE nome = "{nome2}"'
#cursor.execute(comando)
#conexao.commit() 


#UPDATE
#nome1 = "João"
#nome2 = "Marcos"
#comando = f'UPDATE usuario SET nome = "{nome1}" WHERE nome = "{nome2}"'
#cursor.execute(comando)
#conexao.commit() 


# READ
#comando = 'SELECT * FROM usuario'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

#  CREATE
#v_nome = "Marcos"
#v_email = "marcos@outlook.com"
#v_user = "Marty22"
#v_cpf = "12345678910"
#v_senha = "Maadhdh"
#v_nasc = "1997-07-28"  # Formato AAAA-MM-DD
#v_saldo = 2000
#v_despesas = 0
#v_gastos = 0
#comando = f'INSERT INTO usuario (nome, email, user_name, cpf, senha, data_de_nascimento, data_de_cadastro, saldo, despesas_fixas, limite_de_gastos) VALUES ("{v_nome}", "{v_email}", "{v_user}", "{v_cpf}", "{v_senha}", "{v_nasc}", NOW(), {v_saldo}, {v_despesas}, {v_gastos})'
#cursor.execute(comando)
#conexao.commit() 
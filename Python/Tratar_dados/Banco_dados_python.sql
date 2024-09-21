CREATE SCHEMA Dados_excel;

USE Dados_excel;

CREATE TABLE dados(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    sexo VARCHAR(100),
    idade INT,
    email VARCHAR(100),
    telefone VARCHAR(100),
    cidade VARCHAR(100)
);

SELECT * FROM dados;
SELECT * FROM dados WHERE sexo = 'F';

-- Autor: Wanderson Gomes da Costa
-- E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
-- Data da Ultima Modificacao: 03 de Dezembro de 2021
-- SGDB: MySQL
-- DESCRICAO DO BANCO:
--      Banco de dados da Questao 13

-- APAGA O BANCO DE DADOS SE ELE EXISTIR
DROP DATABASE IF EXISTS questao13;

-- CRIA O BANCO DE DADOS
CREATE DATABASE IF NOT EXISTS questao13;

-- DEFINE O BANCO DE DADOS A SER USADO
USE questao13;

-- CRIA A TABELA FUNCIONARIOS
CREATE TABLE Funcionarios (
    id INT NOT NULL AUTO_INCREMENT,
    Nome VARCHAR(30) NOT NULL,
    Sexo CHAR NOT NULL,

    PRIMARY KEY (id)
);

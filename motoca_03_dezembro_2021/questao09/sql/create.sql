-- Autor: Wanderson Gomes da Costa
-- E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
-- Data da Ultima Modificacao: 03 de Dezembro de 2021
-- SGDB: MySQL
-- DESCRICAO DO BANCO:
--      Banco de dados da Questao 09

-- APAGA O BANCO DE DADOS SE ELE EXISTIR
DROP DATABASE IF EXISTS questao09;

-- CRIA O BANCO DE DADOS
CREATE DATABASE IF NOT EXISTS questao09;

-- DEFINE O BANCO DE DADOS A SER USADO
USE questao09;

-- CRIA AS TABELAS QUE SERAO NECESSARIAS PARA A QUESTAO
CREATE TABLE IF NOT EXISTS Atores (
    Codigo INT NOT NULL AUTO_INCREMENT,
    Nome VARCHAR(50) NOT NULL,

    PRIMARY KEY (Codigo)
);

CREATE TABLE IF NOT EXISTS Filmes (
    Codigo INT NOT NULL AUTO_INCREMENT,
    Nome VARCHAR(50) NOT NULL,
    Genero VARCHAR(30) NOT NULL,

    PRIMARY KEY (Codigo)
);

CREATE TABLE IF NOT EXISTS AtoresEmFilmes (
    CodFilme INT NOT NULL,
    CodAtor INT NOT NULL,

    PRIMARY KEY (CodFilme, CodAtor)
);
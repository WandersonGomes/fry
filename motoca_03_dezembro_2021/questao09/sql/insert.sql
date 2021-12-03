-- Autor: Wanderson Gomes da Costa
-- E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
-- Data da Ultima Modificacao: 03 de Dezembro de 2021
-- SGDB: MySQL

-- ESCOLHE O BANCO DE DADOS
USE questao09;

-- POVOA AS TABELAS
INSERT INTO Filmes
    (Nome, Genero)
VALUES
    ("Filme 1", "Genero 1"),
    ("Filme 2", "Genero 2"),
    ("Filme 3", "Genero 3")
;

INSERT INTO Atores
    (Nome)
VALUES
    ("Ator 1"),
    ("Monica Belucci"),
    ("Ator 2")
;

INSERT INTO AtoresEmFilmes
    (CodFilme, CodAtor)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 2),
    (3, 1),
    (3, 3)
;
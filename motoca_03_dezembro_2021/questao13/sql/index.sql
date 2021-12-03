-- Autor: Wanderson Gomes da Costa
-- E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
-- Data da Ultima Modificacao: 03 de Dezembro de 2021
-- SGDB: MySQL

-- ESCOLHE O BANCO DE DADOS
USE questao13;

-- VERIFICA PERFOMANCE ANTES DO INDEX
EXPLAIN SELECT DISTINCT A.Nome FROM Funcionarios A WHERE A.Sexo = "F" OR A.Sexo = "M";

-- CRIA OS INDICE PARA A TABELA FUNCIONARIOS
CREATE IF NOT EXISTS INDEX idx_funcionario ON Funcionarios(Nome);

-- VERIFICA PERFOMANCE DEPOIS DO INDEX
EXPLAIN SELECT DISTINCT A.Nome FROM Funcionarios A;

-- RESPOSTA FINAL
SELECT DISTINCT F.Nome FROM Funcionarios F;
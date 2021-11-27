-- AUTOR: Wanderson Gomes da Costa
-- E-MAIL: wanderson.gomes.costa05@aluno.ifce.edu.br
-- DATA ULTIMA MODIFICACAO: 27 de Novembro de 2021
-- SGDB: Oracle

-- cria a tabela docente
CREATE TABLE docente (
    id NUMBER GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(40) NOT NULL,
    dataAdmissao DATE NOT NULL
);

-- descrever a tabela
DESCRIBE docente;

-- insercao de dados para analise
INSERT ALL
    INTO docente (nome, dataAdmissao) VALUES ('Joao', TO_DATE('01 MAR 2020', 'DD MM YYYY'))
    INTO docente (nome, dataAdmissao) VALUES ('Maria', TO_DATE('01 JAN 2000', 'DD MM YYYY'))
SELECT * FROM dual;

-- apresentar a tabela com os dados preenchidos
SELECT * FROM docente; 

-- verificar a quantidade de meses que o docente esta na instituicao
WITH tmp_nomeDocenteQtdMeses AS (
    SELECT
        nome,
        FLOOR(
            MONTHS_BETWEEN(SYSDATE, dataAdmissao)
        ) qtd_meses
    FROM
        docente
)
;

-- resolucao do problema, nome, qtd_anos e qtd_meses
SELECT 
    nome, 
    FLOOR(qtd_meses/12) QTD_ANOS,
    MOD(qtd_meses, 12) QTD_MESES
FROM
    tmp_nomeDocenteQtdMeses
;


-- RESOLUCAO VERSAO 2.0
SELECT 
    nome, 
    FLOOR(qtd_meses/12) QTD_ANOS,
    MOD(qtd_meses, 12) QTD_MESES
FROM
    (
    SELECT
        nome,
        FLOOR(
            MONTHS_BETWEEN(SYSDATE, dataAdmissao)
        ) qtd_meses
    FROM
        docente
    ) tabela
;
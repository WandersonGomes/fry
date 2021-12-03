-- Autor: Wanderson Gomes da Costa
-- E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
-- Data da Ultima Modificacao: 03 de Dezembro de 2021
-- SGDB: MySQL

USE questao09;

-- CONSULTA QUE RETORNA O CODIGO E NOME DE TODOS OS FILMES QUE
-- A ATRIZ "Monica Belucci" nao atuou
SELECT 
    F.Codigo,
    F.Nome
FROM
    Filmes F JOIN AtoresEmFilmes AF
    ON AF.CodFilme = F.Codigo
    JOIN Atores A
    ON AF.CodAtor = A.Codigo
WHERE
    A.Nome NOT LIKE 'Monica Belucci'
    AND
    F.Codigo NOT IN (
        SELECT
            Filmes.Codigo
        FROM
            Filmes JOIN AtoresEmFilmes
            ON AtoresEmFilmes.CodFilme = Filmes.Codigo
            JOIN Atores
            ON AtoresEmFilmes.CodAtor = Atores.Codigo
        WHERE
            Atores.Nome LIKE 'Monica Belucci'
    )
GROUP BY
    F.Codigo
;

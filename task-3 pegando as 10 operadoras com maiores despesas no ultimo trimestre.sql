SELECT reg_ans, Datas, SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
FROM balanco_contabil
WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÃŠNCIA A SAÃšDE MEDICO HOSPITALAR ' -- OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR
AND Datas = '2024-01-01' 
GROUP BY reg_ans, Datas
ORDER BY total_despesa DESC
LIMIT 10;
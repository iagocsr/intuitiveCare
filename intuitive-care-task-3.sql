SELECT 
    reg_ans AS operadora,
    Datas,
    SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
FROM balanco_contabil
WHERE Datas >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
AND vl_saldo_final - vl_saldo_inicial > 0  
GROUP BY reg_ans, Datas
ORDER BY total_despesa DESC 
LIMIT 10;
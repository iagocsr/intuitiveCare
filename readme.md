# Documentação de Scripts task 3 utilizando SQL

Este repositório contém scripts SQL que são utilizados para criar uma tabela, importar dados e realizar consultas específicas para analisar as despesas das operadoras de saúde. Abaixo estão as etapas detalhadas para a execução dos scripts no MySQL Workbench.

Baixe os arquivos dos últimos 2 anos do repositório
público: https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/

Antes de executar os scripts SQL, é necessário realizar as seguintes etapas:

1. **Criar um esquema (banco de dados):** Crie um esquema (banco de dados) no MySQL para armazenar a tabela e os dados. 
   
   Para criar o esquema, execute o comando:
   `CREATE DATABASE nome_do_esquema;`

2. **Usar o esquema criado:** Após criar o esquema, é necessário selecionar o esquema com o comando:
 `USE nome_do_esquema;`

3. **Arquivos CSV:** Você deve ter os arquivos CSV baixados corretamente para importar os dados. Os arquivos CSV necessários para a importação são:

- `1T2024.csv`
- `2T2024.csv`
- `3T2024.csv`
- `4T2024.csv`

Esses arquivos CSV devem ser armazenados no diretório correto para que o MySQL consiga acessá-los durante a importação.
## 1. Criar a Tabela `balanco_contabil`

```sql
USE teste;

CREATE TABLE balanco_contabil (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Datas DATE NOT NULL,
    reg_ans VARCHAR(7) NOT NULL,
    cd_conta_contabil VARCHAR(15) NOT NULL,
    descricao VARCHAR(250) NOT NULL,
    vl_saldo_inicial DECIMAL(18,2) NOT NULL,
    vl_saldo_final DECIMAL(18,2) NOT NULL
);
```
## 2. Importar Dados
```sql
USE teste;

SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2024.csv' 
INTO TABLE balanco_contabil
FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2T2024.csv' 
INTO TABLE balanco_contabil
FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2024.csv' 
INTO TABLE balanco_contabil
FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2024.csv' 
INTO TABLE balanco_contabil
FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

## 3. Consultar as 10 Operadoras com Maiores Despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR" no Último Trimestre
```sql
SELECT reg_ans, Datas, SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
FROM balanco_contabil
WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
AND Datas = '2024-01-01' 
GROUP BY reg_ans, Datas
ORDER BY total_despesa DESC
LIMIT 10;
```
## 4. Consultar as 10 Operadoras com Maiores Despesas no Último Ano
```sql

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
```

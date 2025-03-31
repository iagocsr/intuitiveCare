use teste;
CREATE TABLE balanco_contabil (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Datas date NOT NULL,
    reg_ans varchar(7) NOT NULL,
    cd_conta_contabil varchar(15) NOT NULL,
    descricao varchar(250) NOT NULL,
    vl_saldo_inicial DECIMAL(18,2) NOT NULL,
    vl_saldo_final DECIMAL(18,2) NOT NULL
);
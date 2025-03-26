import pandas as pd
import pdfplumber
import zipfile

# Nome do arquivo PDF baixado anteriormente
pdf_filename = "downloads/Anexo_I.pdf"
csv_filename = "Rol_Procedimentos.csv"
zip_filename = "Teste_Iago.zip"

# Lista para armazenar os dados extraídos
data = []

# Lendo o PDF e extraindo tabelas
with pdfplumber.open(pdf_filename) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                data.append(row)

# Criando um DataFrame
df = pd.DataFrame(data)

# Ajustando as colunas (supondo que a primeira linha seja o cabeçalho)
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

# Renomeando as colunas OD e AMB
df.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)

# Salvando em CSV
df.to_csv(csv_filename, index=False, encoding="utf-8")

# Compactando o CSV em um ZIP
with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write(csv_filename)

print(f"Arquivo ZIP criado: {zip_filename}")

import requests
from bs4 import BeautifulSoup 
import os
import zipfile

# Configurações
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
OUTPUT_DIR = "downloads"
ZIP_NAME = "anexos.zip"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mapeamento de renomeação
RENAME_MAPPING = {
    "Anexo_I": "Anexo_I_Rol_2021RN_465.2021_RN627",
    "Anexo_II": "Anexo_II_DUT_2021_RN_465.2021_RN628"
}

def download_file(url, filename):
    """Baixa um arquivo e salva com o nome especificado"""
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return True
    except Exception as e:
        print(f"Erro ao baixar {url}: {str(e)}")
        return False

# Obter links dos PDFs
print("Acessando o site...")
try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    pdf_links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if any(key in href for key in RENAME_MAPPING.values()) and href.endswith(".pdf"):
            pdf_links.append(href if href.startswith("http") else f"https://www.gov.br{href}")

    if len(pdf_links) < 2:
        raise Exception("Não foram encontrados os links para ambos os anexos")

    # Download e renomeação
    downloaded_files = []
    for pdf_url in pdf_links:
        original_name = os.path.basename(pdf_url)
        
        # Determinar se é Anexo I ou II
        new_name = ""
        if RENAME_MAPPING["Anexo_I"] in original_name:
            new_name = "Anexo_I.pdf"
        elif RENAME_MAPPING["Anexo_II"] in original_name:
            new_name = "Anexo_II.pdf"
        
        if not new_name:
            continue
            
        output_path = os.path.join(OUTPUT_DIR, new_name)
        print(f"Baixando {original_name} como {new_name}...")
        
        if download_file(pdf_url, output_path):
            downloaded_files.append(output_path)

    # Compactação
    if downloaded_files:
        print("\nCriando arquivo ZIP...")
        with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in downloaded_files:
                zipf.write(file, os.path.basename(file))
        
        print(f"\nProcesso concluído com sucesso!")
        print(f"Arquivo ZIP criado: {ZIP_NAME}")
        print(f"Arquivos incluídos: {[os.path.basename(f) for f in downloaded_files]}")
    else:
        print("Nenhum arquivo foi baixado para compactação.")

except Exception as e:
    print(f"\nOcorreu um erro durante a execução: {str(e)}")
    print("Verifique sua conexão com a internet ou tente novamente mais tarde.")
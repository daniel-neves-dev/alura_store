from packages import pd

url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

URLS = [url1, url2, url3, url4]

def load_stores(urls) -> pd.DataFrame:
    """ Load stores from a list of stores"""

    df = pd.read_csv(urls, index_col=0)
    return df

stores = {f'Loja{i+1}': load_stores(u) for i, u in enumerate(URLS)}


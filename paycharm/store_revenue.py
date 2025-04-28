from packages import pd, PrettyTable
from load_stores import stores

revenues = {store_name: (sum(df['Preço'])) for store_name, df in stores.items()}
df_revenue = (pd.DataFrame(revenues.items(), columns=['Loja', 'Preço'])
               .rename(columns={'Preço':'Faturamento'}))

def plot_tabel_revenue(revenues_df: pd.DataFrame):
    """ Plot the total revenues for all stores """

    """
        Enter with the revenue in data frame format 
    """

    tabel = PrettyTable(['Loja', 'Faturamento'])
    for _, row in revenues_df.iterrows():
        tabel.add_row([
            row['Loja'],
            f"R${row['Faturamento']:,.2f}".replace(',', 'x').replace('.', ',').replace('x', '.')
        ])

    title = 'Faturamento por loja'
    tabel_str = tabel.get_string()
    width = len(tabel_str.splitlines()[0])

    print('\n' + title.center(width))
    print(tabel_str)



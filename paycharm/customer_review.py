from pacakes import pd, plt, PrettyTable

from load_stores import stores

customers_rank = {store_name: round(df['Avaliação da compra'].mean(),2) for store_name, df in stores.items()}
df_customer_rank = (pd.DataFrame(customers_rank.items(), columns=['Loja', 'Avaliação da compra'])
                    .rename(columns={'Avaliação da compra':'Avaliação média'}))

def plot_table_customer_rank(customer_rank_df:pd.DataFrame):
    """  Plot the table average customer rank review for each store """
    customer_rank_df = customer_rank_df.sort_values(by='Avaliação média',ascending=False)

    table = PrettyTable(['Loja', 'Avaliação média' ])
    for _, row in customer_rank_df.iterrows():
        table.add_row([
            row['Loja'],
            row['Avaliação média']
        ])

    title = 'Avaliação média dos cientes'
    table_str = table.get_string()
    width =len(table_str.splitlines()[0])

    print('\n' + title.center(width))
    print(table_str)

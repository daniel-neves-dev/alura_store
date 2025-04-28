from packages import pd, plt, PrettyTable, Patch
from load_stores import stores

products = {store_name: df.groupby('Produto').size().reset_index(name='Quantidade')
            for store_name, df in stores.items()}

def table_top_tree_sell(dic_products:dict[str, pd.DataFrame]):
    """  Plot a table of the top 3 products most sold """

    for store , df in dic_products.items():
        table = PrettyTable(['Produto', 'Quantidade'])
        top_row = df.nlargest(3,'Quantidade')

        for _, row in top_row.iterrows():
            table.add_row([
                row['Produto'],
                f"{row['Quantidade']}"
            ])
        title = f'Top 3 produtos mais vendidos - {store}'
        table_str = table.get_string()
        width = len(table_str.splitlines()[0])

        print('\n' + title.center(width))
        print(table_str)

def table_bottom_tree_sell(dic_products:dict[str, pd.DataFrame]):
    """  Plot a table of the 3 products least sold """

    for store , df in dic_products.items():
        table = PrettyTable(['Produto', 'Quantidade'])
        top_bottom = df.nsmallest(3,'Quantidade')

        for _, row in top_bottom.iterrows():
            table.add_row([
                row['Produto'],
                f"{row['Quantidade']}"
            ])
        title = f' Os 3 produtos menos vendidos - {store}'
        table_str = table.get_string()
        width = len(table_str.splitlines()[0])

        print('\n' + title.center(width))
        print(table_str)


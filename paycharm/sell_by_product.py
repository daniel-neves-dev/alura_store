from packages import pd, plt, PrettyTable, Patch
from load_stores import stores

products = {store_name: df.groupby('Produto').size().reset_index(name='Quantidade')
            for store_name, df in stores.items()}

def table_top_tree_sell(dic_products:dict[str, pd.DataFrame])-> None:
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

def table_bottom_tree_sell(dic_products:dict[str, pd.DataFrame])-> None:
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

def frame_top_tree_product_sell(s_products:pd.DataFrame, store_name:str )-> list:
    """ Make a top tree most product sold list """
    top_tree = s_products.nlargest(3,'Quantidade')
    frame = [
        (f"{store_name}\n{row['Produto']}", row['Quantidade'])
         for _, row in top_tree.iterrows()]

    return frame

def plot_product_bar_graph(product_list:list)->None:
    """  Plot a bar graphic of the 3 products most sold """
    labels, values = zip(*product_list)

    stores_n = [lbl.split('\n')[0] for lbl in labels]
    stores_order = sorted(set(stores_n))
    color_map = {s: plt.cm.tab10(i) for i, s in enumerate(stores_order)}
    colors = [color_map[s] for s in stores_n]

    fig, axs = plt.subplots(figsize=(16,13))

    bars = axs.bar(labels, values, color = colors, width=0.6)
    axs.bar_label(bars, fontsize=12)
    axs.set_title('Produtos com maior número de unidades vendidas\n Top 3', fontsize=14, fontweight='bold')
    axs.spines[['top', 'left', 'right']].set_visible(False)
    axs.yaxis.set_visible(False)

    axs.set_xticks(range(len(labels)))
    axs.set_xticklabels(labels, rotation=30, ha='right')

    legends = [Patch(color=cor, label=loja) for loja, cor in color_map.items()]
    axs.legend(handles=legends, title='Lojas', loc="upper right")

    plt.show()

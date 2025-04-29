from packages import pd, plt, PrettyTable, Patch
from load_stores import stores

categories = {store_name: df.groupby('Categoria do Produto').size()
            .reset_index(name='Quantidade')
            .rename(columns = {'Categoria do Produto':'Categoria'})
            for store_name, df in stores.items()}

def plot_table_categories_most_sell(dict_categories)-> None:
    """  Plot store products category most sold """

    table = PrettyTable(['Loja', 'Categoria', 'Quantidade'])
    for store, df in dict_categories.items():
        max_row = df.loc[df['Quantidade'].idxmax()]
        table.add_row([
            store,
            max_row['Categoria'],
            f"{max_row['Quantidade']} Unidades"
        ])

    title = 'Categoria mais vendida'
    table_str = table.get_string()
    width = len(table_str.splitlines()[0])

    print('\n' + title.center(width))
    print(table_str)

def plot_table_categories_least_sell(dict_categories:dict) -> None:
    """  Plot store products category least sold """

    table = PrettyTable(['Loja', 'Categoria', 'Quantidade'])
    for store, df in dict_categories.items():
        min_row = df.loc[df['Quantidade'].idxmin()]
        table.add_row([
            store,
            min_row['Categoria'],
            f"{min_row['Quantidade']} Unidades"
        ])

    title = 'Categoria menos vendida'
    table_str = table.get_string()
    width = len(table_str.splitlines()[0])

    print('\n' + title.center(width))
    print(table_str)

def most_least_category_sold(name_category:pd.DataFrame, name_store:str) -> list:
    max_row = name_category.loc[name_category['Quantidade'].idxmax()]
    min_row = name_category.loc[name_category['Quantidade'].idxmin()]

    frame = [
        (f"{name_store}\nCategoria: {max_row['Categoria']}", max_row['Quantidade']),
        (f"{name_store}\nCategoria: {min_row['Categoria']}", min_row['Quantidade'])
    ]

    return frame

def plot_category_sell_bar_graph(list_data:list) -> None:
    """ Plot bar chart for most and least category selling"""
    labels, values = zip(*list_data)
    fig, axs = plt.subplots(figsize=(16,10))

    bar_colors = ['tab:blue', 'tab:red']

    bars = axs.bar(labels, values, width=0.8, color=bar_colors)
    axs.bar_label(bars, fontsize = 12)
    axs.spines[['top', 'left', 'right']].set_visible(False)
    axs.set_title('Vendas por categoria\nTotal em unidades', fontsize = 14, fontweight='bold')
    axs.yaxis.set_visible(False)

    axs.set_xticks(range(len(labels)))
    axs.set_xticklabels(labels, rotation=20, ha="right", fontsize=12)

    legend_elements = [
        Patch(facecolor="tab:blue", label="Mais vendido"),
        Patch(facecolor="tab:red",  label="Menos vendido")
    ]
    axs.legend(handles=legend_elements, loc="upper right")

    plt.tight_layout()
    plt.show()


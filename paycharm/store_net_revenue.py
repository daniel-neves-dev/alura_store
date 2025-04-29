from packages import pd, plt, PrettyTable
from load_stores import stores

net_revenue = {store_name: (df['Preço']-df['Frete']).mean()
                for store_name, df in stores.items()}
df_net_revenue = pd.DataFrame(list(net_revenue.items()), columns = ['Loja', 'Faturamento líquido médio'])


def plot_table_net_revenue(net_revenue_df:pd.DataFrame)-> None:
    """ Plot a net revenue of each store table """

    net_revenue_df = net_revenue_df.sort_values(by='Faturamento líquido médio', ascending=False)

    table = PrettyTable(['Loja', 'Faturamento líquido médio'])
    for _, row in net_revenue_df.iterrows():
        table.add_row([
            row['Loja'],
            f"R${row['Faturamento líquido médio']:,.2f}".replace('.', ',')
        ])
    title = 'Faturamento líquido médio por loja'
    table_str = table.get_string()
    width = len(table_str.splitlines()[0])

    print('\n' + title.center(width))
    print(table_str)

def plot_bar_net_revenue(net_revenue_df:pd.DataFrame)->None:
    """ Plot a bar graph net revenue of each store table """

    net_revenue_df = net_revenue_df.sort_values(by='Faturamento líquido médio', ascending=False)
    fig, axs = plt.subplots(figsize=(12, 12))
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    labels = [lbl for lbl in net_revenue_df['Loja']]
    values = [val / 1e0 for val in net_revenue_df['Faturamento líquido médio']]

    bars = axs.bar(labels, values, color=bar_colors)
    axs.bar_label(bars, labels=[f'R${vl:.2f}' for vl in values], fontsize=12)
    axs.set_title('Faturamento líquido médio por loja', fontsize=14, fontweight='bold')

    axs.set_xticks(range(len(labels)))
    axs.set_xticklabels(labels, fontsize=12)

    axs.yaxis.set_visible(False)
    axs.spines[['top', 'left', 'right']].set_visible(False)

    plt.show()



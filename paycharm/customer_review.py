from packages import pd, plt, PrettyTable
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

def plot_customer_rank_bar_graph(customer_rank_df:pd.DataFrame):
    """  Plot the bar graph average customer rank review for each store """

    customer_rank_df = customer_rank_df.sort_values(by='Avaliação média', ascending=False)
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    fig, axs = plt.subplots(figsize=(10,10))
    labels = [lbl for lbl in customer_rank_df['Loja']]
    values = [va/1e0 for va in customer_rank_df['Avaliação média']]

    bars = axs.bar(labels, values, color = bar_colors, width=0.5)
    axs.bar_label(bars, fontsize=12)
    axs.set_title('Avaliação média dos clientes por loja', fontsize=14, fontweight= 'bold')

    axs.set_xticks(range(len(labels)))
    axs.set_xticklabels(labels, fontsize=12)

    axs.yaxis.set_visible(False)
    axs.spines[['top', 'left', 'right']].set_visible(False)

    plt.show()


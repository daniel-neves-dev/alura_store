from packages import pd, plt, PrettyTable
from load_stores import stores

store_fare = {store_name: round(df['Frete'].mean()) for store_name, df in stores.items()}
df_store_fare = pd.DataFrame(store_fare.items(), columns=['Loja', 'Frete'])

def plot_store_fare_table(store_fare_df:pd.DataFrame):
    """ Plot the average store fare for each store """

    table = PrettyTable(['Loja', 'Frete'])

    for _, row in store_fare_df.iterrows():
        table.add_row([
            row['Loja'],
            f"R${row['Frete']:,.2f}".replace('.' ,',')
        ])

    title = 'Custo médio do frete por loja'
    table_str = table.get_string()
    width = len(table_str.splitlines()[0])

    print('\n' + title.center(width))
    print(table_str)

def plot_store_fare_bar_plot(store_fare_df:pd.DataFrame):
    fig, axs = plt.subplots(figsize=(12,12))
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    labels = [lbl for lbl in store_fare_df['Loja']]
    values = [val/1e0 for val in store_fare_df['Frete']]

    bars = axs.bar(labels, values, color=bar_colors)
    axs.bar_label(bars, labels=[f'R${vl:.2f}' for vl in values], fontsize=12)
    axs.set_title('Custo faturamento médio por loja', fontsize = 14, fontweight= 'bold')

    axs.set_xticks(range(len(labels)))
    axs.set_xticklabels(labels, fontsize=12)

    axs.yaxis.set_visible(False)
    axs.spines[['top', 'left', 'right']].set_visible(False)

    plt.show()


plot_store_fare_bar_plot(df_store_fare)
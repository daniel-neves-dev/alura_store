from packages import pd, plt, PrettyTable
from load_stores import stores

revenues = {store_name: (sum(df['Preço'])) for store_name, df in stores.items()}
df_revenue = (pd.DataFrame(revenues.items(), columns=['Loja', 'Preço'])
               .rename(columns={'Preço':'Faturamento'}))

def plot_tabel_revenue(revenue_df: pd.DataFrame):
    """ Plot the total revenues for all stores """

    """
        Enter with the revenue in data frame format 
    """

    tabel = PrettyTable(['Loja', 'Faturamento'])
    for _, row in revenue_df.iterrows():
        tabel.add_row([
            row['Loja'],
            f"R${row['Faturamento']:,.2f}".replace(',', 'x').replace('.', ',').replace('x', '.')
        ])

    title = 'Faturamento por loja'
    tabel_str = tabel.get_string()
    width = len(tabel_str.splitlines()[0])

    print('\n' + title.center(width))
    print(tabel_str)

def plot_revenue_bar_graph(revenue_df: pd.DataFrame):
    fig, axs = plt.subplots(figsize=(10,10))
    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

    labels = [lbl for lbl in revenue_df['Loja']]
    values = [va/1e6 for va in revenue_df['Faturamento']]


    bars = axs.bar(labels, values, color = bar_colors, width=0.5)
    axs.bar_label(bars, labels=[f'{vl:.2f} M' for vl in values], fontsize = 12)
    axs.set_title('Faturamento total de cada loja em milhões', fontsize = 12, fontweight= 'bold')

    axs.set_xticks(range(len(labels)))
    axs.set_xticklabels(labels, fontsize = 12)

    axs.yaxis.set_visible(False)
    axs.spines[['top', 'left', 'right']].set_visible(False)

    plt.show()

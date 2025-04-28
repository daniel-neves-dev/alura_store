from sell_by_category import *

#----------- SELL BY CATEGORY --------------
plot_table_categories_most_sell(categories)
plot_table_categories_least_sell(categories)
category_data = []
for n_store in categories.keys():
    category_data.extend(most_least_category_sold(categories[n_store], n_store))
plot_category_sell_bar_graph(category_data)
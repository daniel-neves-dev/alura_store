from load_stores import stores
from store_fare import plot_store_fare_table, df_store_fare, plot_store_fare_bar_plot
from customer_review import  plot_table_customer_rank, plot_customer_rank_bar_graph, df_customer_rank
from store_revenue import plot_tabel_revenue, df_revenue, plot_revenue_bar_graph
from sell_by_category import *

#----------- SELL BY CATEGORY --------------
plot_table_categories_most_sell(categories)
plot_table_categories_least_sell(categories)
category_data = []
for n_store in categories.keys():
    category_data.extend(most_least_category_sold(categories[n_store], n_store))
plot_category_sell_bar_graph(category_data)

#------------------ Store fare cost ---------------------

plot_store_fare_table(df_store_fare)
plot_store_fare_bar_plot(df_store_fare)

#------ CUSTOMER RANK -------------
plot_table_customer_rank(df_customer_rank)
plot_customer_rank_bar_graph(df_customer_rank)

#---- REVENUES -----

plot_tabel_revenue(df_revenue)
plot_revenue_bar_graph(df_revenue)


from load_stores import stores
from customer_review import  plot_table_customer_rank, plot_customer_rank_bar_graph, df_customer_rank
from store_revenue import plot_tabel_revenue, df_revenue, plot_revenue_bar_graph

#------ CUSTOMER RANK -------------
plot_table_customer_rank(df_customer_rank)
plot_customer_rank_bar_graph(df_customer_rank)

#---- REVENUES -----

plot_tabel_revenue(df_revenue)
plot_revenue_bar_graph(df_revenue)


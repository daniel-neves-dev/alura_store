from load_stores import stores
from customer_review import  plot_table_customer_rank, plot_customer_rank_bar_graph, df_customer_rank

#------ CUSTOMER RANK -------------
plot_table_customer_rank(df_customer_rank)
plot_customer_rank_bar_graph(df_customer_rank)
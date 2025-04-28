from sell_by_product import *

#----- PRODUCTS -----------
table_top_tree_sell(products)
table_bottom_tree_sell(products)
product_data = []
for store in products.keys():
    product_data.extend(frame_top_tree_product_sell(products[store], store))
plot_product_bar_graph(product_data)
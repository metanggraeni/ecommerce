import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sellers_dataset_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/sellers_dataset.csv")
products_dataset_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/products_dataset.csv")
customers_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/customers_dataset.csv")
geolocation_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/geolocation_dataset.csv")
order_items_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/order_items_dataset.csv")
order_payments_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/order_payments_dataset.csv")
orders_dataset_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/orders_dataset.csv")
product_category_name_translation_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/product_category_name_translation.csv")

order_customers_df = pd.merge(
    left=orders_dataset_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)

order_customers_df.head()

bystate_df = order_customers_df.groupby(by="customer_state").customer_id.nunique().reset_index()
bystate_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
bystate_df.sort_values(by="customer_count", ascending=False)

products_order_df = pd.merge(
    left=products_dataset_df,
    right=order_items_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)

final_merged_df = pd.merge(products_order_df, product_category_name_translation_df, how='inner', on='product_category_name')
final_merged_df.head()

final_merged_df.sample(5)

final_merged_df.describe(include="all")

final_merged_df.groupby(by="product_category_name_english").product_id.nunique().sort_values(ascending=False)

customers_df.sample(5)

customers_df.describe(include="all")

customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False)

customers_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)

geolocation_df.sample(5)

geolocation_df.describe(include="all")

# Judul
st.header('🌟E-Commerce Public Dataset Dashboard🌟')
st.caption('by Metha Anggraeni 2024')


# Peforma Produk
st.subheader("Peforma kategori produk terbaik dan terburuk")

sum_order_items_df = final_merged_df.groupby("product_category_name_english").order_item_id.sum().sort_values(ascending=False).reset_index()
sum_order_items_df.head(10)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 6))

sns.barplot(x="order_item_id", y="product_category_name_english", data=sum_order_items_df.head(6), ax=ax[0])
ax[1].set_ylabel("Kategori Produk")
ax[1].set_xlabel("Jumlah item yang telah terbeli")
ax[0].set_title("kategori produk yang paling banyak dibeli", loc="center", fontsize=18)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(x="order_item_id", y="product_category_name_english", data=sum_order_items_df.sort_values(by="order_item_id", ascending=True).head(6), ax=ax[1])
ax[1].set_ylabel("Kategori Produk")
ax[1].set_xlabel("Jumlah item yang telah terbeli")
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("kategori produk yang paling sedikit dibeli", loc="center", fontsize=18)
ax[1].tick_params(axis='y', labelsize=15)

st.pyplot(fig)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Demografi Konsumen
st.subheader("Negara dengan pembelian produk terbanyak")

plt.figure(figsize=(10, 5))
colors_ = ["#EB5E5E"]
sns.barplot(
    x="customer_count",
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
plt.title("Negara yang paling banyak melakukan pembelian produk kita", loc="center", fontsize=10)
plt.ylabel("Negara")
plt.xlabel("Jumlah Customers")
plt.tick_params(axis='y', labelsize=8)
st.pyplot()
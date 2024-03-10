import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data from saved CSV files

bystate_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/bystate.csv")
final_merged_df = pd.read_csv("https://raw.githubusercontent.com/metanggraeni/ecommerce/main/final_merged.csv")

# Judul
st.header('🌟E-Commerce Public Dataset Dashboard🌟')
st.caption('by Metha Anggraeni 2024')

# Peforma Produk
st.subheader("Peforma kategori produk terbaik dan terburuk")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 6))

sns.barplot(x="order_item_id", y="product_category_name_english", data=final_merged_df.head(6), ax=ax[0])
ax[0].set_ylabel("Kategori Produk")
ax[0].set_xlabel("Jumlah item yang telah terbeli")
ax[0].set_title("kategori produk yang paling banyak dibeli", loc="center", fontsize=18)
ax[0].tick_params(axis='y', labelsize=15)

sns.barplot(x="order_item_id", y="product_category_name_english", data=final_merged_df.sort_values(by="order_item_id", ascending=True).head(6), ax=ax[1])
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

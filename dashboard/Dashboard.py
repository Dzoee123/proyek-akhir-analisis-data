import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

st.title("Dashboard Bike Sharing Dataset")

main_data_df = pd.read_csv('main_data.csv')

tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

with tab1:
    st.subheader("Kondisi cuaca mana yang paling sering menyebabkan penjualan rendah?")
    
    weather_sales = main_data_df.groupby(by="weathersit").agg({
        "cnt": "sum"
    }).reset_index()
    
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=weather_sales,
        x="weathersit",
        y="cnt",
        palette="viridis"
    )
    
    plt.title("Total Penjualan Berdasarkan Kondisi Cuaca")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Total Penjualan")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(plt.gcf())

    st.write("**Conclusion:** Dari analisis total penjualan berdasarkan kondisi cuaca, pada cuaca *severe weather* menunjukkan total penjualan sebanyak 223, yang mana adalah total penjualan terendah. Hal ini menunjukkan bahwa cuaca buruk secara signifikan mempengaruhi minat pelanggan untuk melakukan pembelian.")

with tab2:
    st.subheader("Apakah ada bulan tertentu dengan frekuensi pembelian yang lebih tinggi dibandingkan bulan lainnya?")
    
    purchase_frequency = main_data_df.groupby(by=["mnth", "yr"]).agg({
        "cnt": "count"
    }).reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=purchase_frequency,
        x="mnth",
        y="cnt",
        hue="yr",
        palette="pastel",
        marker="o"
    )
    
    plt.title("Frekuensi Pembelian per Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Frekuensi Pembelian")
    plt.legend(title="Tahun", loc="upper right")
    plt.tight_layout()
    
    st.pyplot(plt.gcf())

    st.write("**Conclusion:** Berdasarkan analisis frekuensi pembelian per bulan, bulan tertentu menunjukkan frekuensi pembelian yang lebih tinggi. Bulan Desember, Juli, dan Mei memiliki angka pembelian yang tinggi dengan jumlah pembelian masing-masing yang mencapai lebih dari 740. Sebaliknya, bulan Februari menunjukkan frekuensi pembelian terendah, dengan angka sekitar 649.")
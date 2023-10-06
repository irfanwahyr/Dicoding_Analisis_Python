import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    all_df = pd.read_csv("main_data.csv")
    sns.set(style='dark')

    st.header('Bike Sharing Data :sparkles:')

    # Membuat tab navigasi
    selected_tab = st.sidebar.radio("Navigation",
                                    ["Statistik Peminjaman Sepeda",
                                     "Deskripsi Dataset", 'Sewa Musim 4',
                                     "sewa cuaca buruk",
                                     "sebaran penyewa"
                                     ])

    # Menampilkan konten sesuai tab yang dipilih
    if selected_tab == "Statistik Peminjaman Sepeda":
        show_content(all_df)
    elif selected_tab == "Deskripsi Dataset":
        show_deskripsi_data(all_df)
    elif selected_tab == "Sewa Musim 4":
        show_sewa_musim4(all_df)
    elif selected_tab == "sewa cuaca buruk":
        show_sewa_cuaca_buruk(all_df)
    elif selected_tab == "sebaran penyewa":
        sebaran_penyewa(all_df)

def show_content(all_df):
    st.title('Statistik Peminjaman Sepeda')
    jam_range = st.slider("Pilih Rentang Jam", 0, 23, (0, 23))
    filtered_data = all_df[(all_df['hr'] >= jam_range[0]) & (all_df['hr'] <= jam_range[1])]
    st.markdown("---")
    st.write("Data Sepeda disewa jam:", jam_range[0], "sampai jam ", jam_range[1])
    st.write(filtered_data[['hr', 'cnt']])
    st.markdown("---")
    st.write("Statistik Sepeda disewa:")
    st.write("Rata-rata:", filtered_data['cnt'].mean())
    st.write("Median:", filtered_data['cnt'].median())
    st.write("Maksimum:", filtered_data['cnt'].max())
    st.write("Minimum:", filtered_data['cnt'].min())
    st.markdown("---")
    st.write("Grafik Sepeda disewa:")
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['hr'], filtered_data['cnt'])
    plt.xlabel('Jam (hr)')
    plt.ylabel('Jumlah Sepeda disewa (cnt)')
    plt.title('Grafik Peminjaman Sepeda')
    st.pyplot(plt) # type: ignore

def show_deskripsi_data(all_df):
    st.title('Deskripsi Bike Sharing Dataset')
    st.write(all_df.describe())
def show_sewa_musim4(all_df):
    # Menampilkan judul
    st.title("Jumlah Penyewaan pada Musim 4")

    # Filter data untuk musim 4
    season_4_data = all_df[all_df['season'] == 4]

    # Membuat diagram batang
    plt.figure(figsize=(12, 6))
    plt.bar(season_4_data['hr'], season_4_data['cnt'])
    plt.xlabel('Jam (hour)')
    plt.ylabel('Jumlah Penyewaan')
    plt.title('Jumlah Penyewaan pada Musim 4')
    plt.xticks(rotation=45)
    plt.grid(True)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(plt) # type: ignore
def show_sewa_cuaca_buruk(all_df):
    # Filter data untuk weathersit = 4
    weathersit_4_data = all_df[all_df['weathersit'] == 4]

    # Membuat diagram batang
    plt.figure(figsize=(12, 6))
    plt.bar(weathersit_4_data['hr'], weathersit_4_data['cnt'])
    plt.xlabel('Jam (hour)')
    plt.ylabel('Jumlah Penyewaan')
    plt.title('Jumlah Penyewaan pada Cuaca Buruk')
    plt.xticks(rotation=45)  # Untuk mengatur rotasi label sumbu x agar lebih mudah dibaca
    plt.xticks(range(1, max(weathersit_4_data['hr']) + 1, 1))
    plt.grid(False)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(plt) # type: ignore
def sebaran_penyewa(all_df):
    # Menghitung jumlah "casual" dan "registered"
    total_casual = all_df['casual'].sum()
    total_registered = all_df['registered'].sum()

    # Membuat diagram batang
    plt.figure(figsize=(10, 6))
    bars = plt.bar(['casual', 'registered'], [total_casual, total_registered], color=['red', 'blue'])
    plt.xlabel('Atribut')
    plt.title('Jumlah "casual", "registered"')
    plt.grid(True)

    # Menambahkan label jumlah pada tiap batang
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')

    st.pyplot(plt) # type: ignore


if __name__ == '__main__':
    main()

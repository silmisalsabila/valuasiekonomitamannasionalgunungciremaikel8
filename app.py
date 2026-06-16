import os
import streamlit as st

# ================= KONFIGURASI HALAMAN =================
st.set_page_config(
    page_title="Forest Value Explorer",
    page_icon="assets/logo_unisba.png",
    layout="wide"
)

# ================= COVER =================
col1, col2 = st.columns([1, 5])

with col1:
    logo_path = "assets/logo_unisba.png"

    if os.path.exists(logo_path):
        st.image(logo_path, width=130)

with col2:
    st.markdown("""
    <h1 style='color:#0b3d2e; margin-bottom:0;'>
    FOREST VALUE EXPLORER
    </h1>

    <h4 style='color:#2f5d50; margin-top:10px;'>
    Aplikasi Interaktif untuk Memahami Ekonomi dan Keberlanjutan
    Sumber Daya Hutan Indonesia
    </h4>
    """, unsafe_allow_html=True)

st.markdown("---")

st.write("### Disusun Oleh")
st.write("**Kelompok 8**")

st.write("""
1. Nadylah Agustinawati (10090224003)

2. Silmi Yusniah Salsabila (10090224020)

3. Siti Annisa Dewanty (10090224033)
""")

st.write("""
Program Studi Ekonomi Pembangunan

Universitas Islam Bandung
""")

st.markdown("---")

# ================= SIDEBAR =================
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Pendahuluan",
        "Manfaat Ekonomi Hutan",
        "Permasalahan",
        "Grafik",
        "Studi Kasus",
        "Simulasi",
        "Kesimpulan"
    ]
)

# ================= PENDAHULUAN =================
if menu == "Pendahuluan":

    st.header("Pendahuluan")

    st.write("""
    Ekonomi sumber daya hutan merupakan cabang ilmu yang mempelajari
    pemanfaatan sumber daya hutan secara optimal untuk meningkatkan
    kesejahteraan masyarakat tanpa mengabaikan aspek keberlanjutan.

    Berdasarkan tiga jurnal yang digunakan, hutan memiliki nilai ekonomi
    yang besar baik dari hasil kayu, hasil non-kayu, jasa lingkungan,
    maupun sektor ekowisata.
    """)

# ================= MANFAAT =================
elif menu == "Manfaat Ekonomi Hutan":

    st.header("Manfaat Ekonomi Sumber Daya Hutan")

    manfaat = pd.DataFrame({
        "Jenis Manfaat": [
            "Hasil Kayu",
            "Hasil Non Kayu",
            "Jasa Lingkungan",
            "Ekowisata"
        ],
        "Keterangan": [
            "Bahan baku industri dan konstruksi",
            "Madu, rotan, getah, tanaman obat",
            "Penyerap karbon dan penyimpan air",
            "Pendakian, wisata alam dan konservasi"
        ]
    })

    st.dataframe(manfaat, use_container_width=True)

# ================= PERMASALAHAN =================
elif menu == "Permasalahan":

    st.header("Permasalahan Sumber Daya Hutan")

    masalah = pd.DataFrame({
        "Permasalahan": [
            "Deforestasi",
            "Penebangan Liar",
            "Kebakaran Hutan",
            "Eksploitasi Berlebihan"
        ],
        "Dampak": [
            "Berkurangnya luas hutan",
            "Kerusakan ekosistem",
            "Pencemaran dan kerugian ekonomi",
            "Penurunan kualitas sumber daya hutan"
        ]
    })

    st.dataframe(masalah, use_container_width=True)

# ================= GRAFIK =================
elif menu == "Grafik":

    st.header("Tingkat Ancaman terhadap Hutan")

    grafik = pd.DataFrame({
        "Kategori": [
            "Deforestasi",
            "Penebangan Liar",
            "Kebakaran",
            "Eksploitasi"
        ],
        "Skor": [40, 25, 20, 15]
    })

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        grafik["Kategori"],
        grafik["Skor"]
    )

    ax.set_ylabel("Persentase (%)")
    ax.set_title("Ancaman terhadap Sumber Daya Hutan")

    st.pyplot(fig)

# ================= STUDI KASUS =================
elif menu == "Studi Kasus":

    st.header("Studi Kasus Taman Nasional Gunung Ciremai")

    st.write("""
    Penelitian pada Taman Nasional Gunung Ciremai menggunakan
    Contingent Valuation Method (CVM) untuk mengetahui
    kesediaan membayar (Willingness To Pay/WTP)
    pengunjung terhadap peningkatan pengelolaan kawasan wisata.

    Hasil penelitian menunjukkan bahwa wisata alam memiliki
    nilai ekonomi yang penting dalam mendukung konservasi
    dan pengelolaan sumber daya hutan secara berkelanjutan.
    """)

# ================= SIMULASI =================
elif menu == "Simulasi":

    st.header("Simulasi Nilai Ekonomi Wisata Hutan")

    jumlah = st.slider(
        "Jumlah Pengunjung",
        100,
        10000,
        1000
    )

    wtp = st.number_input(
        "Willingness To Pay per Pengunjung (Rp)",
        value=10000
    )

    nilai = jumlah * wtp

    st.success(
        f"Estimasi Nilai Ekonomi Wisata = Rp {nilai:,.0f}"
    )

# ================= KESIMPULAN =================
elif menu == "Kesimpulan":

    st.header("Kesimpulan")

    st.write("""
1. Hutan memiliki nilai ekonomi yang tinggi melalui hasil kayu,
hasil non-kayu, jasa lingkungan dan ekowisata.

2. Pemanfaatan hutan harus memperhatikan prinsip keberlanjutan
agar fungsi ekologis tetap terjaga.

3. Valuasi ekonomi sumber daya hutan penting sebagai dasar
pengambilan kebijakan pengelolaan hutan.

4. Pengembangan ekowisata dapat menjadi alternatif peningkatan
pendapatan sekaligus mendukung konservasi hutan.
""")

st.markdown("---")
st.caption("Sumber: Hasil sintesis tiga jurnal ekonomi sumber daya hutan.")

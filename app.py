import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================

st.set_page_config(
    page_title="Eco-Forest Valuation",
    layout="wide"
)

# ==================================================
# JUDUL APLIKASI
# ==================================================

col1, col2 = st.columns([1, 6])

with col1:
    st.image("Logo_Unisba.png", width=100)

with col2:
    st.title("Eco-Forest Valuation")
    st.subheader("Pembelajaran Ekonomi Sumber Daya Hutan")

# ==================================================
# SIDEBAR MENU
# ==================================================

st.sidebar.subheader("Pilih Menu")

menu = st.sidebar.radio(
    "",
    [
        "Beranda",
        "Profil TNGC",
        "Kalkulator TEV",
        "Trade-off Lahan",
        "Kebijakan PES",
        "Kasus Interaktif",
        "Visualisasi TEV",
        "Tentang Aplikasi"
    ]
)

# ==================================================
# BERANDA
# ==================================================

if menu == "Beranda":

    st.header("Beranda")

    st.write("""
    Eco-Forest Valuation merupakan aplikasi pembelajaran interaktif yang dirancang untuk membantu mahasiswa memahami konsep ekonomi sumber daya hutan melalui pendekatan valuasi ekonomi. Aplikasi ini mengintegrasikan berbagai konsep penting dalam Ekonomi Sumber Daya Alam dan Lingkungan, seperti Total Economic Value (TEV), trade-off penggunaan lahan, serta Payment for Ecosystem Services (PES).

    Sebagai contoh penerapan, aplikasi ini menggunakan pendekatan studi kasus pada Taman Nasional Gunung Ciremai yang memiliki fungsi ekologis, ekonomi, dan sosial yang penting bagi masyarakat sekitar. Kawasan ini berperan sebagai penyedia jasa lingkungan berupa penyimpanan karbon, pengaturan tata air, pelestarian keanekaragaman hayati, dan pengembangan ekowisata.

    Melalui simulasi dan visualisasi yang tersedia, pengguna dapat memahami bagaimana suatu kawasan hutan tidak hanya menghasilkan manfaat ekonomi secara langsung, tetapi juga memberikan manfaat tidak langsung dan manfaat keberlanjutan yang sering kali tidak diperhitungkan dalam pengambilan keputusan pembangunan.
    """)

    st.subheader("Modul Aplikasi")

    st.write("""
    1. Profil Taman Nasional Gunung Ciremai

    2. Kalkulator Total Economic Value (TEV)

    3. Simulasi Trade-off Penggunaan Lahan

    4. Payment for Ecosystem Services (PES)

    5. Studi Kasus Interaktif

    6. Visualisasi Nilai Ekonomi Hutan
    """)

elif menu == "Profil TNGC":

    st.header("Profil Taman Nasional Gunung Ciremai")

    st.subheader("Indikator Kawasan")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Luas Kawasan",
            "14.841,30 ha"
        )

    with col2:
        st.metric(
            "Ketinggian Puncak",
            "3.078 mdpl"
        )

    with col3:
        st.metric(
            "Jenis Tumbuhan",
            "119"
        )

    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            "Spesies Fauna",
            ">300"
        )

    with col5:
        st.metric(
            "Spesies Anggrek",
            "117"
        )

    st.subheader("Keanekaragaman Hayati")

    biodiv = pd.DataFrame({
        "Kategori": [
            "Jenis Tumbuhan",
            "Spesies Fauna",
            "Spesies Anggrek"
        ],
        "Jumlah": [
            119,
            300,
            117
        ]
    })

    st.bar_chart(
        biodiv.set_index("Kategori")
    )
    st.bar_chart(
        biodiv.set_index("Kategori")
    )

    st.write("""
    Keanekaragaman hayati Taman Nasional Gunung Ciremai merupakan aset ekonomi lingkungan yang memiliki:

    • Existence Value

    • Option Value

    • Conservation Value

    dalam konsep Total Economic Value (TEV).
    """)

    st.subheader("Flora Dominan")

    flora = pd.DataFrame({
    "Flora Dominan": [
        "Saninten",
        "Puspa",
        "Huru",
        "Mara"
    ],
    "Jumlah Spesies": [
        35,
        28,
        22,
        18
    ]
})

    st.table(flora)

    st.write("""
    Fungsi ekologis flora dominan:

    • Penyerap karbon

    • Penjaga kesuburan tanah

    • Penyimpan cadangan air

    • Habitat berbagai satwa liar
    """)

    st.subheader("Satwa Kunci")

    satwa = pd.DataFrame({
    "Satwa": [
        "Macan Tutul Jawa",
        "Elang Jawa",
        "Surili",
        "Kodok Merah Ciremai"
    ],
    "Estimasi Populasi": [
        15,
        25,
        80,
        120
    ]
})

    st.table(satwa)

    st.write("""
    Satwa tersebut merupakan spesies indikator dan satwa konservasi utama yang mencerminkan kesehatan ekosistem Taman Nasional Gunung Ciremai.
    """)

# ==================================================
# KALKULATOR TEV
# ==================================================

elif menu == "Kalkulator TEV":

    st.header("Kalkulator Total Economic Value (TEV)")

    st.write("""
Pada simulasi ini, pengguna dapat memasukkan nilai dari setiap komponen manfaat untuk memperoleh estimasi total nilai ekonomi suatu kawasan hutan.

Komponen yang digunakan meliputi:

• Nilai guna langsung → wisata dan hasil hutan.

• Jasa lingkungan → penyediaan air dan penyimpanan karbon.

• Nilai pilihan → potensi pemanfaatan di masa depan.

• Nilai eksistensi → nilai keberadaan flora dan fauna.

Pendekatan ini banyak digunakan dalam pengambilan keputusan konservasi dan pengelolaan hutan berkelanjutan.
""")

    st.info("""
    Contoh Studi Kasus:
    Taman Nasional Gunung Ciremai memiliki luas kawasan sekitar 14.841 hektar.
    """)

    luas = st.number_input(
        "Luas Hutan (Ha)",
        min_value=1,
        value=14841
    )

    nilai_langsung = st.number_input(
        "Nilai Guna Langsung (Rp/Ha)",
        min_value=0,
        value=500000
    )

    nilai_jasa = st.number_input(
        "Nilai Jasa Lingkungan (Rp/Ha)",
        min_value=0,
        value=900000
    )

    nilai_opsi = st.number_input(
        "Nilai Pilihan (Rp/Ha)",
        min_value=0,
        value=300000
    )

    nilai_eksistensi = st.number_input(
        "Nilai Eksistensi (Rp/Ha)",
        min_value=0,
        value=300000
    )

    tev = luas * (
        nilai_langsung +
        nilai_jasa +
        nilai_opsi +
        nilai_eksistensi
    )

    st.success(
        f"Total Economic Value = Rp {tev:,.0f}"
    )

# ==================================================
# TRADE OFF LAHAN
# ==================================================

elif menu == "Trade-off Lahan":

    st.header("Simulasi Trade-off Penggunaan Lahan")

    st.info("""
Simulasi ini membandingkan dua alternatif penggunaan lahan:

• Hutan Lestari

• Konversi Pertanian

Keuntungan ekonomi jangka pendek belum tentu lebih besar dibandingkan manfaat ekologis dan ekonomi jangka panjang yang dihasilkan oleh hutan.
""")

    nilai_hutan = st.slider(
        "Nilai Hutan Lestari (Miliar Rupiah)",
        0,
        200,
        120
    )

    nilai_pertanian = st.slider(
        "Nilai Konversi Pertanian (Miliar Rupiah)",
        0,
        200,
        80
    )

    data = pd.DataFrame({
        "Alternatif": [
            "Hutan Lestari",
            "Konversi Pertanian"
        ],
        "Nilai": [
            nilai_hutan,
            nilai_pertanian
        ]
    })

    st.bar_chart(
        data.set_index("Alternatif")
    )

    if nilai_hutan > nilai_pertanian:

        st.success(
            "Mempertahankan hutan memberikan manfaat ekonomi dan lingkungan yang lebih tinggi dalam jangka panjang."
        )

    elif nilai_hutan < nilai_pertanian:

        st.warning(
            "Konversi lahan memberikan keuntungan ekonomi jangka pendek yang lebih besar namun berpotensi mengurangi jasa lingkungan."
        )

    else:

        st.info(
            "Kedua alternatif memiliki nilai ekonomi yang sama."
        )

# ==================================================
# KEBIJAKAN PES
# ==================================================

elif menu == "Kebijakan PES":

    st.header("Payment for Ecosystem Services (PES)")

    st.write("""
Payment for Ecosystem Services (PES) merupakan mekanisme insentif ekonomi yang diberikan kepada masyarakat atau pengelola kawasan yang mampu menjaga jasa lingkungan.

Dalam konteks Taman Nasional Gunung Ciremai, skema PES dapat dikaitkan dengan:

• Penyimpanan karbon

• Perlindungan daerah tangkapan air

• Konservasi keanekaragaman hayati

Simulasi berikut digunakan untuk menghitung estimasi insentif berdasarkan serapan karbon.
""")

    karbon = st.slider(
        "Serapan Karbon (Ton CO2)",
        0,
        1000,
        300
    )

    harga_karbon = st.number_input(
        "Harga Karbon per Ton (Rp)",
        min_value=0,
        value=150000
    )

    insentif = karbon * harga_karbon

    st.metric(
        "Estimasi Nilai Insentif",
        f"Rp {insentif:,.0f}"
    )

# ==================================================
# KASUS INTERAKTIF
# ==================================================

elif menu == "Kasus Interaktif":

    st.header("Kasus Interaktif")

    kasus = st.selectbox(
        "Pilih Kasus",
        [
            "Taman Nasional Gunung Ciremai",
            "Karbon Hutan",
            "Ekowisata"
        ]
    )

    if kasus == "Taman Nasional Gunung Ciremai":

        st.subheader("Taman Nasional Gunung Ciremai")

        st.write("""
Taman Nasional Gunung Ciremai merupakan kawasan konservasi yang memiliki berbagai manfaat ekonomi dan ekologis.

Selain berfungsi sebagai habitat berbagai jenis flora dan fauna, kawasan ini juga menjadi daerah tangkapan air yang penting bagi masyarakat Kabupaten Kuningan, Majalengka, dan Cirebon.

Dari perspektif ekonomi lingkungan, manfaat kawasan ini tidak hanya berasal dari wisata alam, tetapi juga dari penyimpanan karbon, perlindungan biodiversitas, serta fungsi hidrologis. Oleh karena itu, valuasi ekonomi diperlukan agar seluruh manfaat tersebut dapat dipertimbangkan dalam proses pengambilan kebijakan.
""")

    elif kasus == "Karbon Hutan":

        st.subheader("Karbon Hutan")

        st.write("""
        Hutan berperan sebagai penyerap karbon alami yang membantu mengurangi konsentrasi gas rumah kaca di atmosfer.
        """)

    else:

        st.subheader("Ekowisata")

        st.write("""
        Ekowisata merupakan bentuk pemanfaatan sumber daya hutan yang mengedepankan prinsip konservasi dan keberlanjutan.
        """)

# ==================================================
# VISUALISASI TEV
# ==================================================

elif menu == "Visualisasi TEV":

    st.header("Visualisasi Komponen TEV")

    data = pd.DataFrame({
        "Komponen": [
            "Nilai Guna Langsung",
            "Jasa Lingkungan",
            "Nilai Pilihan",
            "Nilai Eksistensi"
        ],
        "Persentase": [
            25,
            45,
            15,
            15
        ]
    })

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.pie(
        data["Persentase"],
        labels=data["Komponen"],
        autopct="%1.0f%%"
    )

    ax.set_title("Komposisi Total Economic Value")

    st.pyplot(fig)

    st.write("""
    Jasa lingkungan menjadi komponen terbesar dalam Total Economic Value karena mencakup manfaat penyimpanan karbon, penyediaan air, perlindungan keanekaragaman hayati, serta berbagai fungsi ekologis lainnya yang mendukung keberlanjutan lingkungan.
    """)

# ==================================================
# TENTANG APLIKASI
# ==================================================

elif menu == "Tentang Aplikasi":

    st.header("Tentang Aplikasi")

    st.write("""
Eco-Forest Valuation dikembangkan sebagai media pembelajaran pada mata kuliah Ekonomi Sumber Daya Alam dan Lingkungan (ESDAL).

Tujuan aplikasi ini adalah membantu mahasiswa memahami konsep valuasi ekonomi lingkungan melalui simulasi interaktif dan studi kasus nyata.

Konsep yang digunakan meliputi:

• Total Economic Value (TEV)

• Payment for Ecosystem Services (PES)

• Trade-off Penggunaan Lahan

• Valuasi Jasa Lingkungan

• Konservasi Biodiversitas

Studi kasus yang digunakan adalah Taman Nasional Gunung Ciremai sebagai contoh kawasan konservasi yang memiliki nilai ekonomi, sosial, dan ekologis yang tinggi.
""")

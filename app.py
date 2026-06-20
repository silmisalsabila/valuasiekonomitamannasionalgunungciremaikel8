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

st.title("Eco-Forest Valuation")
st.subheader("Pembelajaran Ekonomi Sumber Daya Hutan")

# ==================================================
# SIDEBAR MENU
# ==================================================

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Beranda",
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
    Eco-Forest Valuation merupakan aplikasi pembelajaran interaktif yang dirancang untuk membantu mahasiswa memahami konsep ekonomi sumber daya hutan melalui pendekatan valuasi ekonomi. Aplikasi ini mengintegrasikan konsep Total Economic Value (TEV), trade-off penggunaan lahan, dan Payment for Ecosystem Services (PES) untuk menggambarkan bagaimana sumber daya hutan memberikan manfaat ekonomi, sosial, dan lingkungan secara berkelanjutan.

    Sebagai contoh penerapan, aplikasi ini menggunakan pendekatan studi kasus Taman Nasional Gunung Ciremai. Kawasan konservasi ini memiliki peran penting sebagai penyedia jasa lingkungan, penyerap karbon, habitat keanekaragaman hayati, serta sumber manfaat ekonomi melalui kegiatan wisata alam dan pemberdayaan masyarakat sekitar.

    Melalui simulasi dan visualisasi yang tersedia, pengguna dapat memahami bahwa nilai suatu kawasan hutan tidak hanya berasal dari hasil hutan yang dapat dimanfaatkan secara langsung, tetapi juga dari berbagai manfaat tidak langsung yang mendukung keberlanjutan lingkungan dan kesejahteraan masyarakat.
    """)

    st.subheader("Modul Aplikasi")

    st.write("""
    1. Kalkulator Total Economic Value (TEV)

    2. Simulasi Trade-off Penggunaan Lahan

    3. Payment for Ecosystem Services (PES)

    4. Studi Kasus Interaktif

    5. Visualisasi Komponen Nilai Ekonomi Hutan
    """)

# ==================================================
# KALKULATOR TEV
# ==================================================

elif menu == "Kalkulator TEV":

    st.header("Kalkulator Total Economic Value (TEV)")

    st.write("""
    Total Economic Value (TEV) merupakan pendekatan yang digunakan untuk menghitung seluruh manfaat ekonomi yang dihasilkan oleh suatu kawasan hutan. Pendekatan ini mencakup nilai guna langsung, nilai jasa lingkungan, nilai pilihan, dan nilai eksistensi.
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

    st.write("""
    Simulasi ini membantu pengguna memahami konsep trade-off dengan membandingkan nilai ekonomi dari hutan lestari dan konversi lahan pertanian.
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
    Payment for Ecosystem Services (PES) merupakan mekanisme pemberian insentif kepada masyarakat atau pengelola kawasan yang mampu menjaga jasa lingkungan.
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
        Taman Nasional Gunung Ciremai merupakan kawasan konservasi yang memiliki nilai ekologis dan ekonomi yang tinggi.
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

    ax.set_title(
        "Komposisi Total Economic Value"
    )

    st.pyplot(fig)

# ==================================================
# TENTANG APLIKASI
# ==================================================

elif menu == "Tentang Aplikasi":

    st.header("Tentang Aplikasi")

    st.write("""
    Eco-Forest Valuation dikembangkan sebagai media pembelajaran untuk mendukung pemahaman mahasiswa terhadap konsep ekonomi sumber daya hutan.

    Konsep yang digunakan dalam aplikasi ini meliputi:

    • Total Economic Value (TEV)

    • Trade-off Penggunaan Lahan

    • Payment for Ecosystem Services (PES)

    • Valuasi Jasa Lingkungan

    • Pengelolaan Hutan Berkelanjutan
    """)

import streamlit as st
import pandas as pd

# --- Title ---
st.title("Pengeluaran Anak Kos 71251212")


# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
uang_bulanan = st.number_input("Masukan Uang Bulanan:", value=None, placeholder="type a number")

# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
makanan = st.number_input("Pengeluaran untuk makan:", value=None) # Ada 5
kos = st.number_input("Uang sewa Kos:", value=None) # Kategori
transportasi = st.number_input("Pengeluaran untuk Bensin:", value=None) # Pengeluaran
internet = st.number_input("Pengeluaran untuk Internet:", value=None) # Ya kan
hiburan = st.number_input("Pengeluaran untuk Hiburan:", value=None) # Paham lah ya

# --- Tombol Ngitung Pengeluaran ---
if st. button("Hitung Pengeluaran"): # if jangan dihapus, cuman nambahin tombol disini :

    # --- Ngitung Total Pengeluaran ---
    total_pengeluaran = (makanan + kos + transportasi + internet + hiburan)

    # --- Ngitung Sisa Uang ---
    sisa_uang = uang_bulanan - total_pengeluaran


    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            # Tampilin uang bulanan di sini
            "uang_bulanan", f"{uang_bulanan:,.0f}"
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            "Pengeluaran", f"{total_pengeluaran:,.0f}"
        )
    with kolom3:
        st.metric(
            # Tampilin sisa uang di sini
            "Sisa Uang", f"{sisa_uang:,.0f}"
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa_uang > 0:
        st.success("Keuangan Masih Aman Bulan ini")

    # Kondisi 2
    elif sisa_uang == 0:
        st.warning("Uang Anda Habis")

    # Kondisi 3
    else:
        st.error("Pengeluaran Anda Melebihi Uang Bulanan")


    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    pengeluaran_terbesar = [] # Cari pengeluaran terbesar
    nilai_terbesar = max(
        makanan,
        kos,
        transportasi,
        internet,
        hiburan
    )   
    if makanan == nilai_terbesar:
        pengeluaran_terbesar.append("makanan")
    if kos == nilai_terbesar:
         pengeluaran_terbesar.append("Kos")
    if transportasi == nilai_terbesar:
        pengeluaran_terbesar.append("Transportasi")
    if internet == nilai_terbesar:
        pengeluaran_terbesar.append("Internet")
    if hiburan == nilai_terbesar:
        pengeluaran_terbesar.append("Hiburan")

    st.subheader("Pengeluaran Terbesar")
    st.write(pengeluaran_terbesar) # Tampilin pengeluaran terbesar di sini


    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    st.bar_chart(df_pengeluaran) # Tampilin grafik pengeluaran di sini
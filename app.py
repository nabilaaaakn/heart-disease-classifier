import streamlit as st
import numpy as np
import pandas as pd
import pickle

# ===================== DESKRIPSI PROYEK ===================== #
st.markdown("""
<h1 style='text-align: center; color: #8B0000;'>
💓 Klasifikasi Risiko Penyakit Jantung
</h1>
<p style='text-align: center; font-size:16px;'>
Aplikasi ini menggunakan model machine learning untuk <b>mengklasifikasikan apakah seseorang berisiko terkena penyakit jantung</b> atau tidak, berdasarkan data medis dasar.
</p>
<p style='text-align: center; font-size:14px;'>
Model ini dibangun menggunakan algoritma Random Forest dan telah dilatih menggunakan dataset <i>heart.csv</i>.
</p>
""", unsafe_allow_html=True)

# ===================== Load Model ===================== #
model_filename = "ML_Klasifikasi_Jantung.pkl"
with open(model_filename, "rb") as file:
    model = pickle.load(file)

# ===================== Form Input ===================== #
st.markdown("---")
st.markdown("### 📝 Formulir Data Pasien")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Usia", min_value=1, max_value=120, value=55)
    sex = st.selectbox("Jenis Kelamin", [("Laki-laki", 1), ("Perempuan", 0)])
    cp = st.selectbox("Tipe Nyeri Dada", [
        ("Typical Angina", 0),
        ("Atypical Angina", 1),
        ("Non-anginal Pain", 2),
        ("Asymptomatic", 3)
    ])
    thalach = st.number_input("Detak Jantung Maksimum", min_value=50, max_value=250, value=150)
    exang = st.selectbox("Nyeri Dada saat Olahraga?", [("Tidak", 0), ("Ya", 1)])
    oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox("Slope Segmen ST", [("Up", 2), ("Flat", 1), ("Down", 0)])
    ca = st.number_input("Jumlah Pembuluh Tersumbat", min_value=0, max_value=3, value=1)
    thal = st.selectbox("Hasil Tes Thalium", [
        ("Normal", 0),
        ("Fixed Defect", 1),
        ("Reversible Defect", 2)
    ])

with col2:
    st.markdown("""
    ### ℹ️ **Keterangan Isian**
    - **Usia:** Umur pasien dalam tahun.
    - **Jenis Kelamin:** 1 = Laki-laki, 0 = Perempuan.
    - **Tipe Nyeri Dada:**
      - 0: Typical Angina
      - 1: Atypical Angina
      - 2: Non-anginal Pain
      - 3: Asymptomatic
    - **Oldpeak:** Depresi segmen ST setelah olahraga.
    - **Slope:** 0 = Down, 1 = Flat, 2 = Up.
    - **Pembuluh Tersumbat:** Dari 0–3 hasil fluoroskopi.
    - **Thalium Test:** 0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect.
    """)

# ===================== DataFrame Input ===================== #
sex = sex[1]
cp = cp[1]
exang = exang[1]
slope = slope[1]
thal = thal[1]

columns = ['age', 'sex', 'cp', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
input_df = pd.DataFrame([[age, sex, cp, thalach, exang, oldpeak, slope, ca, thal]], columns=columns)

# ===================== Prediksi ===================== #
st.markdown("---")
if col1.button("🔍 Jalankan Klasifikasi"):
    prediction = model.predict(input_df)

    st.markdown("## 📊 Hasil Klasifikasi")

    if prediction[0] == 1:
        st.markdown("<h3 style='color:red'>🚨 Pasien Berisiko!</h3>", unsafe_allow_html=True)
        st.error("Model menunjukkan bahwa pasien memiliki risiko penyakit jantung.")

        with st.expander("🔎 Faktor-faktor potensial yang berkontribusi:"):
            if oldpeak > 2.0:
                st.markdown("🔴 Oldpeak tinggi → kemungkinan depresi ST segmen.")
            if slope == 0:
                st.markdown("🔴 Slope menurun (Down) → gejala jantung umum.")
            if ca > 0:
                st.markdown(f"🔴 Ditemukan {ca} pembuluh darah yang tersumbat.")
            if thal == 2:
                st.markdown("🔴 Tes Thalium menunjukkan 'reversible defect'.")
            if thalach < (220 - age) * 0.7:
                st.markdown("🔴 Detak jantung maksimum rendah dari standar usia.")

    else:
        st.markdown("<h3 style='color:green'>✅ Pasien Tidak Berisiko</h3>", unsafe_allow_html=True)
        st.success("Model tidak mendeteksi adanya risiko penyakit jantung berdasarkan data ini.")

        with st.expander("✅ Faktor pendukung hasil baik:"):
            if oldpeak <= 2.0:
                st.markdown("🟢 Oldpeak dalam batas normal.")
            if slope == 2:
                st.markdown("🟢 Slope ST menanjak (Up) → pertanda baik.")
            if ca == 0:
                st.markdown("🟢 Tidak ada pembuluh darah yang tersumbat.")
            if thal == 0:
                st.markdown("🟢 Tes Thalium menunjukkan kondisi normal.")
            if thalach >= (220 - age) * 0.7:
                st.markdown("🟢 Detak jantung maksimum sesuai usia.")

    # ✅ Tambahan catatan fairness gender
    st.markdown("""
    ---
    💡 **Catatan Penting**:  
    Model ini menggunakan data jenis kelamin sebagai salah satu fitur.  
    Jika hasil klasifikasi untuk perempuan cenderung berisiko,  
    itu disebabkan distribusi data asli menunjukkan proporsi perempuan berisiko lebih tinggi.  

    Namun, model ini **tidak menggantikan diagnosis medis**.  
    Konsultasikan hasil ini dengan tenaga kesehatan profesional.
    """)

# ===================== Footer ===================== #
st.markdown("""
<hr>
<div style='text-align: center'>
    📌 <i>Dibuat oleh <b>Nabila & Ichsan</b> menggunakan Streamlit</i>  
</div>
""", unsafe_allow_html=True)

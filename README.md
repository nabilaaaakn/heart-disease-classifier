# heart-disease-classifier
Aplikasi klasifikasi risiko penyakit jantung menggunakan model machine learning Random Forest. Berdasarkan data seperti usia, jenis kelamin, detak jantung, oldpeak, dan hasil tes medis. Dibuat dengan Streamlit untuk tujuan edukasi, bukan diagnosis klinis.

# 💓 Klasifikasi Risiko Penyakit Jantung

Aplikasi berbasis Streamlit yang menggunakan model machine learning untuk mengklasifikasikan apakah seorang pasien **berisiko terkena penyakit jantung** atau tidak berdasarkan data medis dasar.

Model ini dibangun menggunakan algoritma **Random Forest Classifier** dan dilatih dari dataset `heart.csv` yang berisi fitur seperti:
- Usia
- Jenis Kelamin
- Tipe Nyeri Dada
- Detak Jantung Maksimum
- Oldpeak (ST Depression)
- Slope ST
- Jumlah Pembuluh Tersumbat
- Hasil Tes Thalium

> ⚠️ **Catatan Penting**  
> Model ini hanya untuk **tujuan edukasi** dan **tidak menggantikan diagnosis medis profesional**.  
> Silakan konsultasikan hasil dengan tenaga kesehatan.

---

## 📦 Fitur Aplikasi

- Form input data pasien
- Klasifikasi apakah pasien **berisiko atau tidak**
- Penjelasan faktor-faktor yang memengaruhi prediksi
- Fairness note tentang pengaruh gender dalam model
- Desain antarmuka intuitif dan interaktif

---

## 🚀 Coba Aplikasinya

👉 Klik untuk mencoba langsung di Streamlit:  
**[🔗 Coba Aplikasi Klasifikasi Jantung](https://nama-deploy-kamu.streamlit.app)**  
_(ganti dengan link deploy kamu nanti)_

---

## ⚙️ Instalasi Lokal (Opsional)

```bash
# Clone repo
git clone https://github.com/nabila/klasifikasi-resiko-jantung.git
cd klasifikasi-resiko-jantung

# Buat virtual environment (opsional tapi disarankan)
python -m venv venv
source venv/bin/activate  # atau venv\Scripts\activate di Windows

# Install dependencies
pip install -r requirements.txt

# Jalankan Streamlit
streamlit run app.py

import streamlit as st
import pickle

    # Muat model
    model_dtc = pickle.load(open('ginjal_model.sav', 'rb'))

    # Judul web
    st.title('Prediksi Penyakit Ginjal')
    st.write('Silakan input kesehatan anda untuk memprediksi kemungkinan penyakit ginjal')

    # CSS untuk styling
    st.markdown("""
        <style>
        body {
            background-color: #D6E63;
            color: #FFFFFF;
        }
        .main {
            background-color: #8D6E63;
            padding: 20px;
            border-radius: 10px;
            color: #FFFFFF;
        }
        .stImage > img {
            border-radius: 10px;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #D7CCC8;
        }
        .stMarkdown p {
            font-size: 16px;
            line-height: 1.6;
            color: #FFFFFF;
        }
        .stTextInput, .stRadio {
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Form input data pengguna
    with st.form("prediction_form"):
        st.header("Informasi Medis")

        col1, col2 = st.columns(2)

        with col1:
            tekanan_darah = st.text_input("Tekanan Darah (mmHg)", help="Contoh: 120")
            berat_jenis = st.text_input("Berat Jenis Urine", help="Contoh: 1.015")
            albumin = st.text_input("Albumin", help="Contoh: 4.0")
            gula = st.text_input("Gula", help="Contoh: 90")
            glukosa_darah_acak = st.text_input("Glukosa Darah Acak", help="Contoh: 140")
            urea_darah = st.text_input("Urea Darah", help="Contoh: 50")

        with col2:
            kreatinin_serum = st.text_input("Kreatinin Serum", help="Contoh: 1.2")
            natrium = st.text_input("Natrium", help="Contoh: 138")
            kalium = st.text_input("Kalium", help="Contoh: 4.0")
            haemoglobin = st.text_input("Haemoglobin", help="Contoh: 13")
            volume_sel_yang_dikemas = st.text_input("Volume Sel yang Dikemas", help="Contoh: 40")
            jumlah_sel_darah_putih = st.text_input("Jumlah Sel Darah Putih", help="Contoh: 8000")
            jumlah_sel_darah_merah = st.text_input("Jumlah Sel Darah Merah", help="Contoh: 5.0")

        st.header("Kondisi Kesehatan")

        col3, col4 = st.columns(2)

        with col3:
            sel_Darah_merah = st.radio(
                "Apakah jumlah sel darah merah Anda berada dalam kisaran normal?",
                ("Normal", "Tidak Normal"),
                help="Pilih 'Normal' jika jumlah sel darah merah Anda normal, sebaliknya pilih 'Tidak Normal'."
            )

            sel_nanah = st.radio(
                "Apakah jumlah sel nanah Anda normal atau tidak normal?",
                ("Normal", "Tidak Normal"),
                help="Pilih 'Normal' jika jumlah sel nanah Anda normal, sebaliknya pilih 'Tidak Normal'."
            )

            gumpalan_sel_nanah = st.radio(
                "Apakah Anda mengalami gumpalan sel nanah?",
                ("Ya", "Tidak"),
                help="Pilih 'Ya' jika Anda mengalami gumpalan sel nanah, sebaliknya pilih 'Tidak'."
            )

            bacteria = st.radio(
                "Apakah Anda mengalami bakteri?",
                ("Ya", "Tidak"),
                help="Pilih 'Ya' jika Anda mengalami bakteri, sebaliknya pilih 'Tidak'."
            )

            hipertensi = st.radio(
                "Apakah Anda mengalami hipertensi?",
                ("Ya", "Tidak"),
                help="Pilih 'Ya' jika Anda mengalami hipertensi, sebaliknya pilih 'Tidak'."
            )

        with col4:
            diabetes_mellitus = st.radio(
                "Apakah Anda mengalami diabetes melitus?",
                ("Ya", "Tidak"),
                help="Pilih 'Ya' jika Anda mengalami diabetes melitus, sebaliknya pilih 'Tidak'."
            )

            penyakit_arteri_koroner = st.radio(
                "Apakah Anda mengalami penyakit arteri koroner?",
                ("Ya", "Tidak"),
                help="Pilih 'Ya' jika Anda mengalami penyakit arteri koroner, sebaliknya pilih 'Tidak'."
            )

            nafsu_makan = st.radio(
                "Bagaimana nafsu makan Anda?",
                ("Baik", "Buruk"),
                help="Pilih 'Baik' jika nafsu makan Anda baik, sebaliknya pilih 'Buruk'."
            )

            pedal_edema = st.radio(
                "Apakah Anda mengalami pedal edema?",
                ("Ya", "Tidak"),
                help="Pilih 'Ya' jika Anda mengalami pedal edema, sebaliknya pilih 'Tidak'."
            )

            anemia = st.radio(
                "Apakah Anda mengalami anemia?",
                ("Ya", "Tidak"),
                help="Pilih 'Ya' jika Anda mengalami anemia, sebaliknya pilih 'Tidak'."
            )

        # Membuat tombol untuk prediksi
        if st.form_submit_button('Test Prediksi gagal ginjal'):
            # Mendapatkan data input dari pengguna
            try:
                data_input = [
                    float(tekanan_darah), float(berat_jenis), float(albumin), float(gula),
                    1 if sel_Darah_merah == "Normal" else 0,
                    1 if sel_nanah == "Normal" else 0,
                    1 if gumpalan_sel_nanah == "Ya" else 0,
                    1 if bacteria == "Ya" else 0,
                    float(glukosa_darah_acak), float(urea_darah), float(kreatinin_serum),
                    float(natrium), float(kalium), float(haemoglobin), float(volume_sel_yang_dikemas),
                    float(jumlah_sel_darah_putih), float(jumlah_sel_darah_merah),
                    1 if hipertensi == "Ya" else 0,
                    1 if diabetes_mellitus == "Ya" else 0,
                    1 if penyakit_arteri_koroner == "Ya" else 0,
                    1 if nafsu_makan == "Buruk" else 0,
                    1 if pedal_edema == "Ya" else 0,
                    1 if anemia == "Ya" else 0
                ]
                
                # Prediksi dengan model
                ginjal_prediction = ginjal_model.predict([data_input])
                
                if ginjal_prediction[0] == 0:
                    gagal_ginjal = 'pasien rentan terkena gagal ginjal'
                else:
                    gagal_ginjal = 'pasien tidak terkena gagal ginjal'
                st.success(gagal_ginjal)
            except ValueError:
                st.error("Pastikan semua nilai input sudah diisi dengan benar dan dalam format numerik.")

import streamlit as st

from key_week6B.login import login
from key_week6B.data import get_data_tugas
from key_week6B.tugas import (
    tampilkan_tugas,
    tambah_tugas,
    edit_tugas
)

if "login" not in st.session_state:
    st.session_state.login = False
if "tugas" not in st.session_state:
    st.session_state.tugas = get_data_tugas()

if not st.session_state.login:
    login()
else:
    st.sidebar.title("📚 Site Tugas")
    st.sidebar.write("Role:",st.session_state.role)

    menu = st.sidebar.radio("Menu",["Daftar Tugas"])

    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.session_state.role = None
        st.rerun()

    if menu == "Daftar Tugas":
        tampilkan_tugas()
        if st.session_state.role == "dosen":
            st.write("---")
            tambah_tugas()
            st.write("---")
            edit_tugas()


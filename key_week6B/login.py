
import streamlit as st


def login():
    st.title("📚 Site Tugas")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):
        if username == "murid" and password == "123":
            st.session_state.login = True
            st.session_state.role = "murid"
            st.rerun()
        elif username == "dosen" and password == "123":
            st.session_state.login = True
            st.session_state.role = "dosen"
            st.rerun()
        else:
            st.error("Username atau password salah")


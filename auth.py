import streamlit as st

def login():
    placeholder = st.empty()

    actual_email = "admin"
    actual_password = "admin"

    with placeholder.form("Login"):
        st.markdown("### Введіть ваші дані для входу")
        email = st.text_input("Email")
        password = st.text_input("Пароль", type="password")
        submit = st.form_submit_button("Увійти")

    if submit and email == actual_email and password == actual_password:
        placeholder.empty()
        st.success("Вхід успішний")
        return True
    elif submit:
        st.error("Невірний email або пароль")
        return False
    return None

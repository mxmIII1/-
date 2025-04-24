import streamlit as st
from datetime import datetime, time

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

if login():
    st.title("Просте веб-застосунок на Streamlit")

    st.subheader("Оберіть період:")

    # Календарі
    start_date = st.date_input("Дата початку")
    end_date = st.date_input("Дата завершення")

    # Час для обох дат
    start_time = st.time_input("Час початку", value=time(9, 0))
    end_time = st.time_input("Час завершення", value=time(18, 0))

    if st.button("Підтвердити"):
        start_datetime = datetime.combine(start_date, start_time)
        end_datetime = datetime.combine(end_date, end_time)

        if start_datetime <= end_datetime:
            st.success(f"Ви обрали період з {start_datetime} по {end_datetime}")
        else:
            st.error("Дата/час завершення не може бути раніше за дату/час початку")

import streamlit as st
from datetime import datetime, time

def authenticate():
    placeholder = st.empty()
    credentials = {"admin": "admin"}  # Зберігайте облікові дані в словнику

    with placeholder.form("Авторизація"):
        st.markdown("### Будь ласка, увійдіть")
        username = st.text_input("Ім'я користувача")
        password = st.text_input("Пароль", type="password")
        submitted = st.form_submit_button("Увійти")

    if submitted and username in credentials and credentials[username] == password:
        placeholder.empty()
        st.success("Успішно авторизовано!")
        st.session_state.logged_in = True  # Використовуйте state для відстеження статусу
        return True
    elif submitted:
        st.error("Невірне ім'я користувача або пароль")
        return False
    return False

if not hasattr(st.session_state, 'logged_in'):
    st.session_state.logged_in = False

if authenticate() or st.session_state.logged_in:
    st.title("Інтерактивний веб-застосунок на Streamlit")
    st.subheader("Виберіть часовий проміжок:")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Початкова дата")
        start_time = st.time_input("Початковий час", value=time(9, 0))
    with col2:
        end_date = st.date_input("Кінцева дата")
        end_time = st.time_input("Кінцевий час", value=time(18, 0))

    if st.button("Застосувати"):
        start_datetime = datetime.combine(start_date, start_time)
        end_datetime = datetime.combine(end_date, end_time)

        if start_datetime <= end_datetime:
            st.info(f"Обраний період: з {start_datetime.strftime('%d.%m.%Y %H:%M')} до {end_datetime.strftime('%d.%m.%Y %H:%M')}")
        else:
            st.error("Помилка: Кінцева дата/час не може бути раніше за початкову дату/час.")
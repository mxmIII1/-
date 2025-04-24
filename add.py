import streamlit as st
from datetime import datetime, time
from auth import login

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

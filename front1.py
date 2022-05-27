import hashlib
import sqlite3
from back import for_col
from back import res
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
# import streamlit_modal as modal
import streamlit.components.v1 as components
import datetime
import pickle

# Переменные
HM = Image.open('HM.jpg')
zoo = Image.open('Zoo.png')
fc = Image.open('fc.jpg')

# Импортирование заглавного текста


# АВТОРИЗАЦИЯ
# Security
# passlib,hashlib,bcrypt,scrypt

f = open('users_dict.bin', 'wb')  # открыть для записи
L = {}
pickle.dump(L, f)  # записать в файл
f.close()


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',
              (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',
              (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main():
    """Simple Login App"""

    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu, key="0")

    if choice == "Home":
        st.title("Время приключений")
        st.subheader("Home")

        # Окна ввода времени
        col1, col2 = st.columns(2)
        with col1:
            t1 = st.time_input('Время начала пересадки', datetime.time(8, 45))
            #st.write('Сейчас', t)
        with col2:
            t2 = st.time_input('Время окончания пересадки',
                               datetime.time(8, 45))
            #st.write('Вам нужно быть в:', t)

        # Слайдер с ценой
        Prise = st.slider("Цена:", 0, 15000)

        # Реализация столбцов
        col1, col2 = st.columns(2)
        with col1:
            location = st.multiselect(
                "Вопрос", ['отв1', 'отв2'])
        with col2:
            sort = st.selectbox("Сортировать: ",
                                ['Сначала популярные', 'Сначала дешевле', 'Сначала дороже', 'Сначала с высоким рейтингом'], key="11")

        # Реализация фильтров
        col1, col2 = st.columns(2)
        with col1:
            aktiv = st.multiselect("Чем хотите заняться?",
                                   ['Прогулка', 'Экскурсия', 'Отдых', 'Еда'])

        with col2:
            family = st.multiselect("Вопрос",
                                    ['Отв1', 'Отв2', 'Отв2'])

        # Реализация карточек
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Создать рекомендацию на основе фильтров', key="12"):
                st.write('тут будет фильтрация')
        with col2:
            if st.button('Или создать персональную рекомендацию на основе выбора других пользователей', key="13"):
                st.write('тут будет персональная рекомендация')

        col1, col2, col3 = st.columns(3)

        with col1:
            dictt = for_col(res[0])
            st.image(HM, caption=dictt['Достопремечательность'])
            st.write(
                f"Общее время на посещение и дорогу: {dictt['Общее_время']} час(а)")
            if st.button('Цена', key="14"):
                st.write(dictt['Стоимость'])
            if st.button('Подробнее про место', key="15"):
                st.write('Фабрика - пук-пук-пук')
            mark1 = st.selectbox(
                "Оценка: ", ['1', '2', '3', '4', '5'], key="16")
            if st.button('Сохранить ответ', key="17"):
                f = open('users_dict.bin', 'rb')  # открыть для чтения
                L = pickle.load(f)  # считать из файла
                f.close()
                f = open('users_dict.bin', 'wb')  # открыть для записи
                L[username][dictt['Достопремечательность']] = mark1
                pickle.dump(L, f)  # записать в файл
                f.close()
                st.write(dictt['Ответ сохранен'])

        with col2:
            dictt = for_col(res[1])
            st.image(HM, caption=dictt['Достопремечательность'])
            st.write(
                f"Общее время на посещение и дорогу: {dictt['Общее_время']} час(а)")
            if st.button('Цена', key="18"):
                st.write(dictt['Стоимость'])
            if st.button('Подробнее про место', key="19"):
                st.write('Фабрика - пук-пук-пук')
            mark2 = st.selectbox(
                "Оценка: ", ['1', '2', '3', '4', '5'], key="20")
            if st.button('Сохранить ответ', key="21"):
                f = open('users_dict.bin', 'rb')  # открыть для чтения
                L = pickle.load(f)  # считать из файла
                f.close()
                f = open('users_dict.bin', 'wb')  # открыть для записи
                L[username][dictt['Достопремечательность']] = mark2
                pickle.dump(L, f)  # записать в файл
                f.close()
                st.write(dictt['Ответ сохранен'])

        with col3:
            dictt = for_col(res[2])
            st.image(HM, caption=dictt['Достопремечательность'])
            st.write(
                f"Общее время на посещение и дорогу: {dictt['Общее_время']} час(а)")
            if st.button('Цена', key="22"):
                st.write(dictt['Стоимость'])
            if st.button('Подробнее про место', key="23"):
                st.write('Фабрика - пук-пук-пук')
            mark3 = st.selectbox(
                "Оценка: ", ['1', '2', '3', '4', '5'], key="24")
            if st.button('Сохранить ответ', key="25"):
                f = open('users_dict.bin', 'rb')  # открыть для чтения
                L = pickle.load(f)  # считать из файла
                f.close()
                f = open('users_dict.bin', 'wb')  # открыть для записи
                L[username][dictt['Достопремечательность']] = mark3
                pickle.dump(L, f)  # записать в файл
                f.close()
                st.write(dictt['Ответ сохранен'])

        col1, col2, col3 = st.columns(3)

        with col1:
            dictt = for_col(res[3])
            st.image(HM, caption=dictt['Достопремечательность'])
            st.write(
                f"Общее время на посещение и дорогу: {dictt['Общее_время']} час(а)")
            if st.button('Цена', key="26"):
                st.write(dictt['Стоимость'])
            if st.button('Подробнее про место', key="27"):
                st.write('Фабрика - пук-пук-пук')
            mark4 = st.selectbox(
                "Оценка: ", ['1', '2', '3', '4', '5'], key="28")
            if st.button('Сохранить ответ', key="29"):
                f = open('users_dict.bin', 'rb')  # открыть для чтения
                L = pickle.load(f)  # считать из файла
                f.close()
                f = open('users_dict.bin', 'wb')  # открыть для записи
                L[username][dictt['Достопремечательность']] = mark4
                pickle.dump(L, f)  # записать в файл
                f.close()
                st.write(dictt['Ответ сохранен'])

        with col2:
            dictt = for_col(res[4])
            st.image(HM, caption=dictt['Достопремечательность'])
            st.write(
                f"Общее время на посещение и дорогу: {dictt['Общее_время']} час(а)")
            if st.button('Цена', key="1"):
                st.write(dictt['Стоимость'])
            if st.button('Подробнее про место', key="2"):
                st.write('Фабрика - пук-пук-пук')
            mark5 = st.selectbox(
                "Оценка: ", ['1', '2', '3', '4', '5'], key="3")
            if st.button('Сохранить ответ', key="4"):
                f = open('users_dict.bin', 'rb')  # открыть для чтения
                L = pickle.load(f)  # считать из файла
                f.close()
                f = open('users_dict.bin', 'wb')  # открыть для записи
                L[username][dictt['Достопремечательность']] = mark5
                pickle.dump(L, f)  # записать в файл
                f.close()
                st.write(dictt['Ответ сохранен'])

        with col3:
            dictt = for_col(res[5])
            st.image(HM, caption=dictt['Достопремечательность'])
            st.write(
                f"Общее время на посещение и дорогу: {dictt['Общее_время']} час(а)")
            if st.button('Цена', key="5"):
                st.write(dictt['Стоимость'])
            if st.button('Подробнее про место', key="6"):
                st.write('Фабрика - пук-пук-пук')
            mark6 = st.selectbox(
                "Оценка: ", ['1', '2', '3', '4', '5'], key="7")
            if st.button('Сохранить ответ', key="8"):
                f = open('users_dict.bin', 'rb')  # открыть для чтения
                L = pickle.load(f)  # считать из файла
                f.close()
                f = open('users_dict.bin', 'wb')  # открыть для записи
                L[username][dictt['Достопремечательность']] = mark6
                pickle.dump(L, f)  # записать в файл
                f.close()
                st.write(dictt['Ответ сохранен'])

    elif choice == "Login":
        st.title("Время приключений")
        st.subheader("Секция Login")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')

        if st.sidebar.checkbox("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))

                task = st.selectbox(
                    "Task", ["Add Post", "Аналитика", "Профили"], key="9")
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Аналитика":
                    st.subheader("Analytics")
                elif task == "Профили":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result, columns=[
                                            "Username", "Password"])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.title("Время приключений")
        st.subheader("Создайте новый аккаунт")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")

            f = open('users_dict.bin', 'rb')  # открыть для чтения
            L = pickle.load(f)  # считать из файла
            f.close()
            st.info("Записано")
            f = open('users_dict.bin', 'wb')  # открыть для записи
            L[new_user] = {1: 1}
            pickle.dump(L, f)  # записать в файл
            f.close()
            st.info("Сохранено")


if __name__ == '__main__':
    main()

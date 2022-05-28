import hashlib
import sqlite3
from unittest import result
from GITback import for_col
from GITback import res
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
# import streamlit_modal as modal
import streamlit.components.v1 as components
import datetime
import pickle


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


def PIC(d):
    picture = d.replace(' ', '')
    picture = picture + '.png'
    return picture


def PAGE():

    st.title("Время приключений")
    st.subheader("Домашняя страница")

    # Окна ввода времени
    col1, col2 = st.columns(2)
    with col1:
        t1 = st.time_input('Время начала пересадки',
                           datetime.time(13, 00))
    with col2:
        t2 = st.time_input('Время окончания пересадки',
                           datetime.time(18, 00))

    # Слайдер с ценой
    '''
    Prise = st.slider("Цена:", 0, 15000)
    '''
    # Реализация столбцов
    '''
    col1, col2 = st.columns(2)
    with col1:
        aktiv = st.multiselect("Чем хотите заняться?",
                               ['Прогулка', 'Экскурсия', 'Отдых', 'Еда'])
    with col2:
        sort = st.selectbox("Сортировать: ",
                            ['Сначала популярные', 'Сначала дешевле', 'Сначала дороже', 'Сначала с высоким рейтингом'], key="11")
    '''

    # Реализация карточек
    '''
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Создать рекомендацию на основе фильтров', key="12"):
            st.write('тут будет фильтрация')
    with col2:
        if st.button('Или создать персональную рекомендацию на основе выбора других пользователей', key="13"):
            st.write('тут будет персональная рекомендация')
    '''
    col1, col2, col3 = st.columns(3)

    with col1:
        dictt = for_col(res[0])
        picture = PIC(dictt['Достопремечательность'])
        st.image(picture, caption=dictt['Достопремечательность'])
        st.write(
            f"Общее время на посещение и дорогу: {dictt['Общее_время']} ч")
        st.write(dictt['Краткое описание'])
        if st.button('Подробнее про место', key="15"):
            st.write(dictt['Описание'])
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
        picture = PIC(dictt['Достопремечательность'])
        st.image(picture, caption=dictt['Достопремечательность'])
        st.write(
            f"Общее время на посещение и дорогу: {dictt['Общее_время']} ч")
        st.write(dictt['Краткое описание'])
        if st.button('Подробнее про место', key="19"):
            st.write(dictt['Описание'])
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
        picture = PIC(dictt['Достопремечательность'])
        st.image(picture, caption=dictt['Достопремечательность'])
        st.write(
            f"Общее время на посещение и дорогу: {dictt['Общее_время']} ч")
        st.write(dictt['Краткое описание'])
        if st.button('Подробнее про место', key="23"):
            st.write(dictt['Описание'])
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
        picture = PIC(dictt['Достопремечательность'])
        st.image(picture, caption=dictt['Достопремечательность'])
        st.write(
            f"Общее время на посещение и дорогу: {dictt['Общее_время']} ч")
        st.write(dictt['Краткое описание'])
        if st.button('Подробнее про место', key="27"):
            st.write(dictt['Описание'])
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
        picture = PIC(dictt['Достопремечательность'])
        st.image(picture, caption=dictt['Достопремечательность'])
        st.write(
            f"Общее время на посещение и дорогу: {dictt['Общее_время']} ч")
        st.write(dictt['Краткое описание'])
        if st.button('Подробнее про место', key="2"):
            st.write(dictt['Описание'])
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
        picture = PIC(dictt['Достопремечательность'])
        st.image(picture, caption=dictt['Достопремечательность'])
        st.write(
            f"Общее время на посещение и дорогу: {dictt['Общее_время']} ч")
        st.write(dictt['Краткое описание'])
        if st.button('Подробнее про место', key="6"):
            st.write(dictt['Описание'])
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


def main():
    """Simple Login App"""
    menu = ["Домашняя страница", "Авторизация", "Регистрация"]
    choice = st.sidebar.selectbox("Menu", menu, key="0")

    if choice == "Домашняя страница":
        PAGE()

    elif choice == "Авторизация":
        st.title("Время приключений")
        st.subheader("Секция Авторизации")

        username = st.sidebar.text_input("Имя пользователя")
        password = st.sidebar.text_input("Пароль", type='password')

        if st.sidebar.checkbox("Авторизация"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:

                st.success("Вошел как {}".format(username))

                if st.button('Профили', key="89"):
                    st.subheader("Профили пользователей")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result, columns=[
                                            "Имя пользователя", "Пароль"])
                    st.dataframe(clean_db)

            else:
                st.warning("Неверное имя пользователя или пароль")

    elif choice == "Регистрация":
        st.title("Время приключений")
        st.subheader("Создайте новый аккаунт")
        new_user = st.text_input("Имя пользователя")
        new_password = st.text_input("Пароль", type='password')

        if st.button("Регистрация"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("Аккаунт создан успешно")
            st.info("Авторизуйтесь в разделе 'Авторизация'")
            f = open('users_dict.bin', 'rb')  # открыть для чтения
            L = pickle.load(f)  # считать из файла
            f.close()
            # st.info("Записано")
            f = open('users_dict.bin', 'wb')  # открыть для записи
            L[new_user] = {1: 1}
            pickle.dump(L, f)  # записать в файл
            f.close()
            # st.info("Сохранено")
            st.info(L)


if __name__ == '__main__':
    main()

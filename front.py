from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
import streamlit_modal as modal
import streamlit.components.v1 as components

# Переменные
HM = Image.open('HM.jpg')
zoo = Image.open('Zoo.png')
fc = Image.open('fc.jpg')

# Импортирование заглавного текста
st.title("Рекомендационный проект МТС")

# Реализация столбцов
col1, col2 = st.columns(2)
with col1:
    Prise = st.slider("Цена:", 0, 15000)
with col2:
    sort = st.selectbox("Сортировать: ",
                        ['Сначала популярные', 'Сначала дешевле', 'Сначала дороже', 'Сначала с высоким рейтингом'])

# Мультивыбор тэгов
location = st.multiselect(
    "Где Вы работали?", ['t', 'k'])

# Реализация фильтров
col1, col2 = st.columns(2)
with col1:
    aktiv = st.multiselect("Активность: ",
                           ['Парк', 'Поход', 'Бег'])
with col2:
    family = st.multiselect("Семья: ",
                            ['Есть дети', 'Нет детей', 'Двое (я и жена)'])

col1, col2 = st.columns(2)
with col1:
    state = st.multiselect("Место:",
                           ['Москва', 'Лондон', 'Непал'])
with col2:
    kategor = st.multiselect("Еда: ",
                             ['Ресторан', 'Фаст фуд', 'Пекарня'])

# Реализация карточек
col1, col2, col3 = st.columns(3)
with col1:
    st.image(HM, caption='Исторический музей')
    st.markdown(
        'Исторический музей - крупнейший национальный исторический музей России.')
    st.button('Цена', key='4')
    if st.button('Подробнее про ГИМ'):
        st.write('Фабрика - пук-пук-пук')
with col2:
    st.image(zoo, caption='Московский зоопарк')
    st.markdown('Московский зоопарк - зоологический парк в центре Москвы.')
    st.button('Цена', key='2')
    if st.button('Подробнее про зоопарк'):
        st.write('Фабрика - пук-пук-пук')

with col3:
    st.image(fc, caption='Завод "Чистая линия"')
    st.markdown('Московский зоопарк - крупнейший национальный зоопарк России.')
    st.button('Цена', key='3')
    if st.button('Подробнее про фабрику'):
        st.write('Завод "Чистая линия" - фабрика по производству мороженого')

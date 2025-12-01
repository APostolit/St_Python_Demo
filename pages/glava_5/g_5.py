import streamlit as st
import fun_g5

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 5", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 5")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 5",
        ("Листинг 5.1", "Листинг 5.2", "Листинг 5.3", "Листинг 5.4",
         "Листинг 5.5", "Листинг 5.6", "Листинг 5.7", "Листинг 5.8",
         "Листинг 5.9", "Листинг 5.10", "Листинг 5.11", "Листинг 5.12"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    st.page_link('https://pythonlib.ru/sandbox', label='🛠️ Редактор код ✍🏻')
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)
    elif options == "Листинг 5.1":
        path = 'pages/glava_5/Listing_5_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_1()
    elif options == "Листинг 5.2":
        path = 'pages/glava_5/Listing_5_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_2()
    elif options == "Листинг 5.3":
        path = 'pages/glava_5/Listing_5_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_3()
    elif options == "Листинг 5.4":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_4()
    elif options == "Листинг 5.5":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_5()
    elif options == "Листинг 5.6":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_6()
    elif options == "Листинг 5.7":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_7()
    elif options == "Листинг 5.8":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_8()
    elif options == "Листинг 5.9":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_9()
    elif options == "Листинг 5.10":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_10()
    elif options == "Листинг 5.11":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_11()
    elif options == "Листинг 5.12":
        with st.expander("🔍 Показать результат"):
            fun_g5.run_5_12()

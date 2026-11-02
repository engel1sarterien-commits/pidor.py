import streamlit as st
import random
import time

# Конфигурация страницы в строгом стиле
st.set_page_config(page_title="Главная проверка 🤨", page_icon="🎲", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #f3f4f6; }
    .main-title { font-size: 28px; font-weight: bold; text-align: center; color: #3b82f6; margin-bottom: 5px; }
    .subtitle { font-size: 14px; text-align: center; color: #9ca3af; margin-bottom: 30px; }
    .question-title { font-size: 40px; font-weight: bold; text-align: center; color: #ff3333; margin: 20px 0; letter-spacing: 2px; }
    .dice-display { font-size: 110px; text-align: center; line-height: 1; margin: 25px 0; color: #3b82f6; }
    .code-box { background-color: #111827; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 13px; border-left: 3px solid #3b82f6; color: #10b981; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">ЦЕНТР СВЕРХТОЧНОЙ ДИАГНОСТИКИ СУДЬБЫ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Анализ ДНК и истории браузера по протоколу ТГ-рандома</div>', unsafe_allow_html=True)

st.write(
    "Здорово. Наука зашла слишком далеко, и мы разработали независимый квантовый кубик, "
    "который определяет твой статус со стопроцентной точностью. Результат броска покажет ответ на главный вопрос."
)

st.write("📋 **Варианты ТГ-кубика:**\n* **1, 2, 3** — Вариант А.\n* **4, 5** — Вариант Б.\n* **6** — Секретный статус.")

# ГЛАВНЫЙ ВОПРОС ПЕРЕД КУБИКОМ
st.markdown('<div class="question-title">СОСАЛ?</div>', unsafe_allow_html=True)

if 'bro_attempts' not in st.session_state:
    st.session_state.bro_attempts = 0
if 'bro_dice' not in st.session_state:
    st.session_state.bro_dice = None

dice_symbols = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}

if st.button("ИСПЫТАТЬ УДАЧУ И КИНУТЬ КУБИК", use_container_width=True):
    st.session_state.bro_attempts += 1
    
    with st.empty():
        for _ in range(6):
            st.markdown(f'<div class="dice-display">{random.choice(list(dice_symbols.values()))}</div>', unsafe_allow_html=True)
            time.sleep(0.1)
            
    # Логика: в первый раз даем случайное число от 1 до 5 (чтобы сразу выдать ДА), со второго раза — жестко шестерку
    if st.session_state.bro_attempts == 1:
        st.session_state.bro_dice = random.randint(1, 5)
    else:
        st.session_state.bro_dice = 6

if st.session_state.bro_dice is not None:
    val = st.session_state.bro_dice
    st.markdown(f'<div class="dice-display">{dice_symbols[val]}</div>', unsafe_allow_html=True)
    st.write(f"Анализ завершен. Значение кубика: **{val}**")
    
    # Смешной бэкенд-лог
    st.markdown('<div class="code-box"><strong>[SYSTEM LOG]</strong><br>'
                f'Status: scanning_user_soul...<br>'
                f'Database check: ID_BROTHER found.<br>'
                f'Anti-cheat protocol: ACTIVE | Attempts: {st.session_state.bro_attempts}</div>', unsafe_allow_html=True)
    st.write("")

    # Результаты бросков (Ответы без выбора)
    if val <= 3:
        st.error("📉 ВЕРДИКТ СИСТЕМЫ: ДА, СОСАЛ.")
        st.write("Кубик врать не будет. Математика, физика и ТГ-рандом сошлись в одной точке. Диагноз окончательный, обжалованию не подлежит.")
        
    elif val == 4 or val == 5:
        st.error("📉 ВЕРДИКТ СИСТЕМЫ: ОЧЕВИДНО, ДА.")
        st.write("Система зафиксировала критическое совпадение траектории кубика. Результаты теста отправлены в общий чат.")

    elif val == 6:
        st.info("🧬 ОСОБЫЙ СТАТУС: ИДИ НАХУЙ.")
        st.write("Шестерка активировала скрытый режим абсолютного иммунитета. Система подумала и решила послать тебя лесом. Тест аннулирован автоматически, ты свободен.")
        st.session_state.bro_attempts = 0

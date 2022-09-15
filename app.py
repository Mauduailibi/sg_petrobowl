import streamlit as st
import pandas as pd
import numpy as np
import os

from models.question import Question

# System functions

# Paths
app_path = os.path.dirname('./')
tables_path = os.path.join(app_path, 'assets/xlsx/')
style = os.path.join(app_path, 'assets/css/style.css')

# Tables count on assets folder
tables_counter = 0
for path in os.listdir(tables_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(tables_path, path)):
        tables_counter += 1

tables = list()
for i in range(tables_counter):
    tables.append(pd.read_excel(os.path.join(tables_path, f'W{i+1}.xlsx')))

# Setting questions

questions = list()

for idx, table in enumerate(tables):
    week = idx + 1
    for i in range(len(table)):
        questions.append(Question(table['Perguntas'][i], table['Respostas'][i], f'Week {week}'))

if 'current_question' not in st.session_state:
    st.session_state['current_question'] = ''
    st.session_state['current_answer'] = ''
    st.session_state['current_week'] = ''

def randomQuestion():
    random = np.random.randint(0, len(questions))
    st.session_state['current_question'] = questions[random].getQuestion()
    st.session_state['current_answer'] = questions[random].getAnswer()
    st.session_state['current_week'] = questions[random].getWeek()

randomQuestion()

# View

with open(style) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('PetroBowl Team CESFI/UDESC')
st.caption('Número de tabelas para treino: {}'.format(tables_counter))
st.caption('Número de perguntas do banco de dados: {}'.format(len(questions)))

st.markdown('<hr>', unsafe_allow_html=True)

st.caption(st.session_state.current_week)
st.write(st.session_state.current_question)
st.success(st.session_state.current_answer)

col_btn_last, col_btn_answer, col_btn_next = st.columns([1, 3, 1])

# with col_btn_last:
#     btn_last = st.button('Anterior')

# with col_btn_answer:
#     btn_answer = st.button('Mostrar resposta')

with col_btn_next:
    btn_next = st.button('Próxima')

# if btn_answer:
#     btn_next = False
#     st.write('Resposta: {}'.format(st.session_state.current_answer))

if btn_next:
    btn_answer = False
    randomQuestion()

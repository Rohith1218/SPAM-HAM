import streamlit as st
import joblib 

model_nd = joblib.load('SPAM-HAM')

st.title('SPAM-HAM CLASSIFIER')
ip = st.text_input('Enter your text: ')

op = model_nb.predict([ip])
if st.button('predict'):
  st.title(op[0])

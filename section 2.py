import streamlit as st 
import os,time
import random
st.title(":sparkles: Lotto")
def generate_lotto():
    lotto = [i + 1 for i in range(45)]
    return lotto

button = st.button('create lotto')
if button:
    for i in range(5):
        st.subheader(f"{i+1}")

def generate_lotto():
    lotto = [i + 1 for i in range(45)]
    random.shuffle(lotto)
    return lotto[:6]
button = st.button("find lotte number")

if button: 
    for i in range(5):
        st.subheader(f"{i+1}. lucky number")

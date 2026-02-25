import streamlit as st 
import os,time
print(f"{os.path.basename(__file__)}실행됨")
st.title("다양한 widget들")
model = st.selectbox("모델선택", ("GPT-3", "GPT-4", "GPT-5"))
st.markdown(f"model: {model}")
# 선택된 값을 출력하기 위해서 

name = st.text_input("what is your name?")
st.markdown(f"name: :red[{name}]")

value = st.slider(label="tempterature",
          min_value=0.1, max_value=1.0)
st.markdown(f"value: :violet[{value}]")
if value > 0.4:
    st.write("high diversity")
else: 
    st.write("Normal model")
    st.text_input("write down the question")
button = st.button("click this button")
if button: 
    st.write(":blue[buttone]is here :sparkles:")
st.markdown('---')
num1 = st.number_input('number 1 enter',
                min_value = 10, max_value = 100, step = 5)
num2 = st.number_input('number 2 enter',
                min_value = 10, max_value = 100, step = 5)
btn_calc = st.button('calculate')
if btn_calc:
    st.write(f"""
             {num1} + {num2} = {num1 + num2}
             {num1} + {num2} = {num1 - num2}

             """)







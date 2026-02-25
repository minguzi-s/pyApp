import streamlit as st
st.title("hey")
st.header("yo")
st.header("hey yo :suglasses:")
st.text("text")
st.caption("caption")
sample_code = '''
def function():
    print('hello, world')
'''

st.text(sample_code)
st.markdown('streamli은 **마크다운 문법** 지원')
st.table([
    ['name', 'age'],
    ['jenny', '43'],
])
st.metric(label='samsung electronic',value = '154,234$', delta = "1,233won")
st.title('write()')
st.write("hello")
st.write(10,20,30)
st.write([2,3,4])
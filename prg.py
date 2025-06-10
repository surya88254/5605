import streamlit as st
from streamlit_option_menu import option_menu  


st.title("Welcome")
st.header("This is my header")
st.subheader("This is my subheader")


st.write("🟢 This is write")
st.text("This is text")
st.write("😊")


st.code("""
#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
""", language="c")


st.latex(r"E=mc^2")


st.metric(label="Temperature", value="70°F", delta="-1.2°F")


st.progress(0.5, text="50%")


st.text_input("Enter your name")
st.number_input("Enter your age")
st.date_input("Enter your date of birth")
st.checkbox("I agree")
st.radio("Select your gender", ["Male", "Female", "Other"])
st.selectbox("Select your country", ["India", "Pakistan", "Kazakhstan"])
st.multiselect("Select your country", ["India", "Pakistan", "Kazakhstan"])
st.slider(label="Set your age", min_value=0, max_value=100, value=25)


with st.sidebar:
    select = option_menu(
        menu_title='Vinsup',
        options=['Home', 'About', 'Service']
    )


if select == 'Home':
    st.title("Hello World")
    st.header("Hellooo Hii")
    st.subheader("Hi 😎 Hellooo")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        a = st.text_input("Name")
        st.write(a)
        
        st.balloons()

    with col2:
        st.text_input("Name1")

elif select == "About":
    st.number_input("Enter your age:")
    st.date_input("Enter date:")
    st.checkbox("I agree")

else:
    st.text("Good evening")
    st.text("Good evening")
import streamlit as st

st.title("Find the Largest Among Three Numbers")

st.write("Enter three numbers below:")

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)
num3 = st.number_input("Enter third number", value=0)

if st.button("Find Largest"):
    largest = max(num1, num2, num3)
    st.write(f"The largest number is: {largest}")


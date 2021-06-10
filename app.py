import streamlit as st 

st.title("Basic Calculator")
a = st.slider("Select the first number :", 0,100)    # User input for first number 
b = st.slider("Select the second number :", 0 ,100)  # User input for second number 
select = st.selectbox("WHICH OPERATION", ("Addition","Subtraction", "Multiplication","Division"))
if select == "Addition":
  calc = int(a) + int(b)
elif select == "Subtraction":
  calc = int(a) - int(b)
elif select == "Multiplication":
  calc = int(a) * int(b)
elif select == "Division":
  calc = int(a) / int(b)
if st.button("CALCULATE!"):
  st.write(f"The {select} of {a} and {b} is {calc}")

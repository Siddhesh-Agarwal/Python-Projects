import streamlit as st

st.title('Python Projects by Siddhesh-Agarwal')
st.header('BMI Calculator')

# Weight of user
weight = st.number_input('Enter your weight')
WeightUnit = st.radio('Select Units', ('kg', 'lbs'))
if WeightUnit == 'lbs':
    weight /= 2.20462262

# Height of user
height = st.number_input('Enter your height')
HeightUnit = st.radio('Select Units', ('m', 'cm', 'inch'))
if HeightUnit == 'cm':
    height /= 100
elif HeightUnit == 'inches':
    height /= 39.3700787

# Results
if st.button('Result'):
    BMI = round(weight / (height ** 2), 1)
    st.info(f'Your Body-Mass Index (BMI) is {BMI}')

    if BMI < 16:
        st.error("You are Extremely Underweight.")
    elif BMI >= 16 and BMI < 18.5:
        st.warning("You are Underweight.")
    elif BMI >= 18.5 and BMI < 25:
        st.success("You are Healthy.")
    elif BMI >= 25 and BMI < 30:
        st.warning("You are Overweight.")
    elif BMI >= 30:
        st.error("You are Extremely Overweight.")

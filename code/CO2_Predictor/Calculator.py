import streamlit as st
import pandas as pd
from sklearn import linear_model

@st.cache
def CO2_Predictor(weight, volume):
    df = pd.read_csv('cars.csv')
    x = df[['Weight', 'Volume']]
    y = df['CO2']

    regr = linear_model.LinearRegression()
    regr.fit(x, y)

    predictedCO2 = regr.predict([[weight, volume]])[0]
    return predictedCO2

st.title('Python Projects by Siddhesh-Agarwal')
st.header('CO2 Emmision predictor')
st.info('''Just enter the weight and fuel displacement of your car and we will predict the CO2
emmitted by your car.''')

Weight = st.number_input('Enter weight')
WeightUnit = st.radio('Select Units', ('kg', 'Tonne'))
if WeightUnit == 'Tonne':
    Weight *= 1000

FuelDisplacement = st.number_input('Enter Fuel Displacement (in CC)')

if st.button('Predict'):
    CO2_Emmitted = CO2_Predictor(Weight, FuelDisplacement)
    if CO2_Emmitted <= 97.5:
        st.success(f'Your car emmits {CO2_Emmitted} grams of CO2 per Kilometer')
    elif CO2_Emmitted > 97.5 and CO2_Emmitted <= 110:
        st.warning(f'Your car emmits {CO2_Emmitted} grams of CO2 per Kilometer')
    else:
        st.error(f'Your car emmits {CO2_Emmitted} grams of CO2 per Kilometer')
    st.warning('This result is calculated on the assumption that the car runs on fossil fuel. Actual results may vary.')

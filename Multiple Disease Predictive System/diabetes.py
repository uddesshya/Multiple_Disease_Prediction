
"""
Created on Fri Jan 12 17:38:52 2024

@author: uddes
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_models = pickle.load(open('C:/Users/uddes/OneDrive/Desktop/Desktop/Multiple Disease Predictive System/Trained Model/diabetes_model.sav','rb'))

# Sidebar for Navigate
with st.sidebar:

    selected = option_menu('Disease Prediction System',

                         ['Diabetes Prediction'],

                         icons=['heart'],
                         default_index=0)


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number Of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI Level')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'DiabetesPedigreeFunction value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''

    # creating a buton for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_models.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if(diab_prediction[0] == 1):
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is not Diabetic'

    st.success(diab_diagnosis)


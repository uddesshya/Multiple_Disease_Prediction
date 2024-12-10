# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 17:38:52 2024

@author: uddes
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_models = pickle.load(open('C:/Users/uddes/OneDrive/Desktop/Desktop/Multiple Disease Predictive System/Trained Model/diabetes_model.sav','rb'))

parkinsons_models = pickle.load(open('C:/Users/uddes/OneDrive/Desktop/Desktop/Multiple Disease Predictive System/Trained Model/parkinsons_model.sav','rb')) 

# Sidebar for Navigate
with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',

                         ['Diabetes Prediction',
                          'Parkinsons Prediction'],

                         icons=['heart', 'person'],
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

if (selected == 'Parkinsons Prediction'):
    # page title
    st.title('Parkinsons Prediction using ML')

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        Fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        Fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        Flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter = st.text_input('MDVP:Jitter()')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
         Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
         Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
         APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
         DDA = st.text_input('Shimmer:DDA')

    with col5:
          NHR = st.text_input('NHR')

    with col1:
         HNR = st.text_input('HNR')

    with col2:
          RPDE = st.text_input('RPDE')

    with col3:
          DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
         spread2 = st.text_input('spread2')

    with col1:
         D2 = st.text_input('D2')

    with col2:
         PPE = st.text_input('PPE')

    # Code for Prediction
    parkinsons_diagnosis = ''

    # creating a buton for prediction
    if st.button('Parkinsons Test Result'):
       parkinsons_prediction = parkinsons_models.predict([[Fo,Fhi,Flo,Jitter,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB, APQ3, APQ5,APQ,DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

       if(parkinsons_prediction[0] == 1):
           parkinsons_diagnosis = 'The Person is having Parkinson'
       else:
           parkinsons_diagnosis = 'The Person is Healthy'

    st.success(parkinsons_diagnosis)
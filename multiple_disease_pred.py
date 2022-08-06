# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 00:20:57 2022

@author: Dell
"""

import pickle
import streamlit as st
import sklearn
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/Dell/Desktop/Project/saved_model/diabetes_model.sav', 'rb'))


#sidebar for navigate
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity'],
                           default_index=0)

#Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):
    #page title

    st.title('Diabetes Prediction using ML')

    #Putting the below values into 3 columns in single row

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of the person ")

    #Code for Prediction
    diab_diagnosis = ''

    #Creating a Button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diab_prediction[0]==0):
            diab_diagnosis = 'The person is not diabetic'
        else:
            diab_diagnosis = 'The person is diabetic'
    st.success(diab_diagnosis)


    
    
    
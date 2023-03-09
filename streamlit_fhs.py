# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import pickle

st.write("# PREDICTION COMBAT POKEMON")

first_pokemon = st.text_input("Entrer le premier pokémon")
second_pokemon = st.text_input("Entrer le deuxième pokémon")

st.button('Predict')

df_pred = pd.DataFrame([[first_pokemon,second_pokemon]],

columns= ['first_pokemon','second_pokemon'])

model = pickle.load(open('best_model.pkl', 'rb')) 

prediction = model.predict(df_pred)

if st.button('Predict'):
    if(prediction[0]==1):
        st.write('<p class="big-font">Le premier pokémon gagne.</p>',unsafe_allow_html=True)
    else:
        st.write('<p class="big-font">Le second pokémon gagne.</p>',unsafe_allow_html=True)
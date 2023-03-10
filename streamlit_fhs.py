# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import pickle
from PIL import Image

import sys
sys.path.insert(0, '/Users/laurasenecaille/opt/anaconda3/lib/python3.9/site-packages/plotly')
import plotly.plotly as py
from plotly import graph_objs as go


im = Image.open("poke.ico")
st.set_page_config(
   page_title="Pokemon Prediction App",
   page_icon=im
)

df_pokemon_copie_1 = pd.read_csv("new_pokemon_prediction_1.csv")
df_pokemon_copie_1.set_index("ID", inplace=True)

df_pokemon_1 = pd.read_csv("df_pokemon_1.csv")



dict_type1 = dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['Type_1']))
dict_type2 = dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['Type_2']))
dict_HP = dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['HP']))
dict_Attack = dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['Attack']))
dict_Defense = dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['Defense']))
dict_Atq_speciale= dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['Atq_speciale']))
dict_Def_speciale= dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['Def_speciale']))
dict_vitesse= dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['vitesse']))
dict_victoire= dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['victoire']))
dict_ratio= dict(zip(df_pokemon_copie_1.index, df_pokemon_copie_1['ratio']))

st.write("# PREDICTION COMBAT POKEMON")

image = Image.open('pokeball.png')
image1 = Image.open('pikachu.jpg')
image2 = Image.open('dracau.jpg')

col1, col2  = st.columns(2)

col11, col22, col33 , col44, col55 = st.columns(5)

first_pokemon = col1.number_input("Entrer le premier pokémon", key = "First_pokemon", min_value = 1, max_value = 800, step = 1, value = 2)
second_pokemon = col2.number_input("Entrer le deuxième pokémon", key='Second_pokemon',  min_value = 1, max_value = 800, step = 1, value = 3)

with col11:
    st.image(image1, width=250)
with col22:
    pass
with col44:
    st.image(image2, width=250)
with col55:
    pass
with col33 :
    st.write(" ")
    st.write(" ")

    st.image(image, width=100)
    st.write(" ")
    st.write(" ")

    button1 = st.button('Fight')

st.write('<hr>',unsafe_allow_html=True  )


df_combat = pd.DataFrame([[first_pokemon,second_pokemon]],
columns= ['First_pokemon','Second_pokemon'])

df_combat_copie = df_combat.copy()

df_combat_copie['First_pokemon_type1'] = df_combat_copie['First_pokemon'].replace(dict_type1)
df_combat_copie['First_pokemon_type2'] = df_combat_copie['First_pokemon'].replace(dict_type2)
df_combat_copie['First_pokemon_HP'] = df_combat_copie['First_pokemon'].replace(dict_HP)
df_combat_copie['First_pokemon_Attack'] = df_combat_copie['First_pokemon'].replace(dict_Attack)
df_combat_copie['First_pokemon_Defense'] = df_combat_copie['First_pokemon'].replace(dict_Defense)
df_combat_copie['First_pokemon_Atq_speciale'] = df_combat_copie['First_pokemon'].replace(dict_Atq_speciale)
df_combat_copie['First_pokemon_Def_speciale'] = df_combat_copie['First_pokemon'].replace(dict_Def_speciale)
df_combat_copie['First_pokemon_vitesse'] = df_combat_copie['First_pokemon'].replace(dict_vitesse)
df_combat_copie['First_pokemon_victoire'] = df_combat_copie['First_pokemon'].replace(dict_victoire)
df_combat_copie['First_pokemon_ratio'] = df_combat_copie['First_pokemon'].replace(dict_ratio)

df_combat_copie['Second_pokemon_type1'] = df_combat_copie['Second_pokemon'].replace(dict_type1)
df_combat_copie['Second_pokemon_type2'] = df_combat_copie['Second_pokemon'].replace(dict_type2)
df_combat_copie['Second_pokemon_HP'] = df_combat_copie['Second_pokemon'].replace(dict_HP)
df_combat_copie['Second_pokemon_Attack'] = df_combat_copie['Second_pokemon'].replace(dict_Attack)
df_combat_copie['Second_pokemon_Defense'] = df_combat_copie['Second_pokemon'].replace(dict_Defense)
df_combat_copie['Second_pokemon_Atq_speciale'] = df_combat_copie['Second_pokemon'].replace(dict_Atq_speciale)
df_combat_copie['Second_pokemon_Def_speciale'] = df_combat_copie['Second_pokemon'].replace(dict_Def_speciale)
df_combat_copie['Second_pokemon_vitesse'] = df_combat_copie['Second_pokemon'].replace(dict_vitesse)
df_combat_copie['Second_pokemon_victoire'] = df_combat_copie['Second_pokemon'].replace(dict_victoire)
df_combat_copie['Second_pokemon_ratio'] = df_combat_copie['Second_pokemon'].replace(dict_ratio)

dropCols_new2 = ['First_pokemon', 'Second_pokemon', 'First_pokemon_type1', 'First_pokemon_type2', 'Second_pokemon_type1', 'Second_pokemon_type2']
df_test_copie = df_combat_copie.drop(dropCols_new2, axis=1)

model = pickle.load(open('best_model.pkl', 'rb')) 

prediction = model.predict(df_test_copie)

df_test_new = df_combat.copy()

df_test_new['First Win'] = prediction

gagnant = pd.DataFrame(df_test_new.apply(lambda x: x["First_pokemon"] if x["First Win"]==1 else x["Second_pokemon"], axis=1), columns=["Winner"])

df_test_new = pd.concat([df_test_new, gagnant], axis=1)

df_test_new = df_test_new.drop('First Win', axis=1)

noms_pokemon = dict(zip(df_pokemon_1['ID'], df_pokemon_1['Name']))
colonne = ['First_pokemon', 'Second_pokemon', 'Winner']
df_combat_nom = df_test_new[colonne].replace(noms_pokemon)

col_pok1 = st.columns(2)

if button1:
    st.write('<hr>',unsafe_allow_html=True  )
    with col_pok1[0]:
      st.write('<center>',df_combat_nom.iloc[0]['First_pokemon'],'</center>', unsafe_allow_html=True )
      st.write('<center><p>Score de victoire : <strong>',  str(round(df_test_copie.iloc[0]['First_pokemon_ratio'], 3)), '</strong></p></center>', unsafe_allow_html=True)
    
    with col_pok1[1]:
      st.write('<center>', df_combat_nom.iloc[0]['Second_pokemon'], '</center>',unsafe_allow_html=True  )
      st.write('<center><p>Score de victoire : <strong>', str(round(df_test_copie.iloc[0]['Second_pokemon_ratio'], 3)), '</strong></p></center>', unsafe_allow_html=True)

    st.write('<center><p class="big-font">Le vainqueur du combat est<b> ', df_combat_nom.iloc[0]['Winner'], '</b></p></center>',unsafe_allow_html=True)
    st.write('<hr>',unsafe_allow_html=True  )

##################### GRAPHIQUE
####PREMIER POKEMON
df_combat_graph = df_combat_copie.copy()
dropCols_poke1 = ['First_pokemon', 'Second_pokemon', 'First_pokemon_type1', 'First_pokemon_type2', 'Second_pokemon_type1', 'Second_pokemon_type2',
            'Second_pokemon_HP', 'Second_pokemon_Attack', 'Second_pokemon_Defense', 'Second_pokemon_Atq_speciale','Second_pokemon_Def_speciale',
            'Second_pokemon_vitesse', 'Second_pokemon_ratio', 'Second_pokemon_victoire', 'First_pokemon_victoire','First_pokemon_ratio' ]
df_poke_best_poke1 = df_combat_graph.drop(dropCols_poke1, axis=1)

df_poke_best_poke1.rename(columns = {'First_pokemon_HP' : 'PV' , 'First_pokemon_Attack' : 'Attaque', 'First_pokemon_Defense' : 'Defense', 'First_pokemon_Atq_speciale' : 'Atq. Speciale','First_pokemon_Def_speciale' : 'Def. Speciale', "First_pokemon_vitesse" : "Vitesse"}, inplace = True)

value_best_poke1 = df_poke_best_poke1.values[0]
value_best_poke1 = value_best_poke1.tolist()
index_best_poke1 = list(df_poke_best_poke1.columns)

####DEUXIÈME POKEMON
df_combat_graph_2 = df_combat_copie.copy()
dropCols_poke2 = ['First_pokemon', 'Second_pokemon', 'First_pokemon_type1', 'First_pokemon_type2', 'Second_pokemon_type1', 'Second_pokemon_type2',
            'First_pokemon_HP', 'First_pokemon_Attack', 'First_pokemon_Defense', 'First_pokemon_Atq_speciale','First_pokemon_Def_speciale',
            'First_pokemon_vitesse', 'Second_pokemon_ratio', 'First_pokemon_victoire','First_pokemon_ratio', 'Second_pokemon_victoire' ]
df_poke_best_poke2 = df_combat_graph_2.drop(dropCols_poke2, axis=1)

df_poke_best_poke2.rename(columns = {'Second_pokemon_HP' : 'PV' , 'Second_pokemon_Attack' : 'Attaque', 'Second_pokemon_Defense' : 'Defense', 'Second_pokemon_Atq_speciale' : 'Atq. Speciale','Second_pokemon_Def_speciale' : 'Def. Speciale', 'Second_pokemon_vitesse' : 'Vitesse'}, inplace = True)

value_best_poke2 = df_poke_best_poke2.values[0]
value_best_poke2 = value_best_poke2.tolist()
index_best_poke2 = list(df_poke_best_poke2.columns)

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=df_poke_best_poke1.values[0],
      theta=index_best_poke1,
      fill='toself',
      name= df_combat_nom.iloc[0]['First_pokemon']
))
fig.add_trace(go.Scatterpolar(
      r=df_poke_best_poke2.values[0],
      theta=index_best_poke2,
      fill='toself',
      name=df_combat_nom.iloc[0]['Second_pokemon']
))

fig.update_layout(
  showlegend=True
)

radar_chart = st.write(fig)
#####################

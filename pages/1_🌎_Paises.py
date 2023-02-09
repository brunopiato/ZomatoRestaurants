########################################################
#              Carregando bibliotecas
########################################################

import pandas as pd
import numpy as np
import plotly.express as px
import inflection
import plotly.graph_objs as go
import streamlit as st


st.set_page_config(page_title = 'Visão de Países', layout='wide', page_icon = '🌎')

########################################################
#              Carregando dados tratados
########################################################

data = pd.read_csv('processed_data.csv')

########################################################
#              Definindo funcoes
########################################################










########################################################
#              Layout da barra lateral
########################################################

st.sidebar.image('pages/Zomato_logo.png', width=100, )

st.sidebar.markdown('# Zomato Restaurants')
st.sidebar.markdown('##### *Conecting people with experiences*')
st.sidebar.markdown("""---""")

paises_selec = st.sidebar.multiselect(label='Selecione os países', 
                       options=['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'],
                       default = ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])

nota_inicial, nota_final = st.sidebar.select_slider(label='Escolha o intervalo de notas',
                         options=[0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5.0],
                         value=(0, 5))
st.sidebar.write('Você escolheu notas entre', nota_inicial, 'e', nota_final)

#Vinculando os widgets aos dados
linhas_selecionadas = data['country'].isin(paises_selec)
data = data.loc[linhas_selecionadas, :]
linhas_selecionadas = (data['aggregate_rating'] >= nota_inicial) & (data['aggregate_rating'] <= nota_final)
data = data.loc[linhas_selecionadas, :]

st.sidebar.markdown('##### Powered by ComunidadeDS')

########################################################
#              Layout do corpo da página
########################################################

st.markdown("# :earth_americas: Visão de Países")
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        # st.markdown('### Quantidade de restaurantes por país')
        df_aux = (data[['country', 'restaurant_name']]
        .groupby('country')
        .nunique()
        .sort_values(by='restaurant_name', ascending=False)
        .reset_index())

        fig = px.bar(x=df_aux.country, 
            y=df_aux.restaurant_name,
            title='Quantidade de restaurantes por país',
            labels={'x':'Países', 'y':'Número de restaurantes registrados'},
            color=df_aux.country)
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # st.markdown('### Quantidade de cidades por país')
        df_aux = (data[['country', 'city']]
        .groupby('country')
        .nunique()
        .sort_values(by='city', ascending=False)
        .reset_index())

        fig = px.bar(x=df_aux.country, 
            y=df_aux.city,
            title='Quantidade de cidades por país',
            labels={'x':'Países', 'y':'Número de cidades registradas'},
            color=df_aux.country)
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

with st.container():
    st.markdown('## Avaliações', )
    col1, col2 = st.columns(2)
    
    with col1:
        # st.markdown('### Média de notas por país')
        df_aux = (data[['country', 'aggregate_rating']]
        .groupby('country')
        .mean()
        .round(2)
        .sort_values(by='aggregate_rating', ascending=False)
        .reset_index())

        fig = px.bar(x=df_aux.country, 
            y=df_aux.aggregate_rating,
            title='Nota média dos restaurantes por país',
            labels={'x':'Países', 'y':'Nota média dos restaurantes'},
            color=df_aux.country)
        # fig = go.Figure(fig, layout_yaxis_range = [3, 5])
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # st.markdown('### Média de avaliaçoes por restaurante em cada país')
        df_aux = (data[['country', 'votes']]
        .groupby('country')
        .mean()
        .round(2)
        .sort_values(by='votes', ascending=False)
        .reset_index())

        fig = px.bar(x=df_aux.country, 
            y=df_aux.votes,
            title='Quantidade média de avaliaçoes por país',
            labels={'x':'Países', 'y':'Quantidade média de avaliaçoes'},
            color=df_aux.country)
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = "📈")

st.sidebar.image('pages/Zomato_logo.png', width = 120)

st.sidebar.markdown('# Zomato Restaurants')
st.sidebar.markdown('## Connecting people to experiences')
st.sidebar.markdown("""---""")

st.write('# Zomato Restaurants Growth Dashboard')

st.markdown("""
            Growth Dashboard foi construído para acompanhar as métricas de crescimento dos entregadores, restaurantes e da empresa.
            ### Como utilizar o Growth Dashboard?
            - Visão Empresa:
                - Visão gerencial: Métricas gerais de comportamento.
                - Visão tática: Indicadores semanais de crescimento.
                - Visão geográfica: Insights de geolocalização.
            - Visão Entregadores: 
                - Acompanhamento dos indicadores semanais de crescimento.
            - Visão Restaurantes:
                - Indicadores semanais de crescimento
            ### Ask for help
                - Time de Data Science no Discord
                    - @piatobruno#0143
            """)
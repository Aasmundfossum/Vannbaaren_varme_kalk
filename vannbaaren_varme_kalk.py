import streamlit as st

st.title('Priskalkulator for vannbåren varme')
st.subheader('Størrelse på bolig (m\u00b2)')
areal = st.slider('Antall kvadratmeter:', min_value=20, max_value=500, value=50, step=1)

st.subheader('Standard og kompleksitet')
kompleks = st.selectbox('Kompleksiteten i prosjektet og standarden på materialer:', options=['Høy','Normal', 'Lav'], index=1)

if kompleks == 'Lav':
    linear_faktor = 1300
elif kompleks == 'Normal':
    linear_faktor = 1900
elif kompleks == 'Høy':
    linear_faktor = 2500

pris = areal*linear_faktor


st.subheader('Prisestimat')

vis_pris = f"{pris:,} kr"
vis_pris = str(vis_pris).replace(',',' ')

d1, d2 = st.columns(2)
with d1:
    st.metric('Estimert kostnad:', vis_pris)
with d2:
    st.metric('Per kvadratmeter:', f"{linear_faktor} kr/m\u00b2")


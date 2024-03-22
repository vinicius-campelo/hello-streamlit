import streamlit as st
from datetime import datetime, timedelta


st.query_params["lang"] = ["pt-br"]
st.query_params.update()

st.title('My First Streamlit App')

number = st.slider("pick number", 0, 200)
choises = st.multiselect("Pedidos", ["A ENVIAR","ENVIADOS", "FINALIZADOS", "CANCELADOS"])
name = st.text_input("Nome:")
st.sidebar.write()
st.sidebar.button("click")

st.sidebar.date_input(
      "Selecione um intervalo de datas",
    format="DD/MM/YYYY"
)



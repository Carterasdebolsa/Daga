import streamlit as st
import pandas as pd
import os

# Función para cargar los datos existentes desde un archivo CSV
def load_data():
    if os.path.exists("datos_diarios.csv"):
        return pd.read_csv("datos_diarios.csv")
    else:
        return pd.DataFrame(columns=["Regió", "Área", "Unitat", "Nombre d'armes blanques", "Detinguts relacionats", "Dia"])

# Función para guardar los datos en un archivo CSV
def save_data(df):
    df.to_csv("datos_diarios.csv", index=False)

# Cargar datos existentes
df = load_data()

# Título de la aplicación
st.title("Dades diaries plà DAGA")

# Formulario para ingresar datos
with st.form("datos_form"):
    col1, col2 = st.columns(2)

    with col1:
        regio = st.text_input("Regió:")
        area = st.text_input("Àrea:")
        unitat = st.text_input("Unitat:")

    with col2:
        num_armes = st.number_input("Nombre d'armes blanques:", min_value=0)
        num_det = st.number_input("Detinguts relacionats:", min_value=0)
        dia = st.date_input("Dia:")

    submitted = st.form_submit_button("Enviar datos")

    if submitted:
        nuevo_dato = pd.DataFrame({
            "Regió": [regio],
            "Área": [area],
            "Unitat": [unitat],
            "Nombre d'armes blanques": [num_armes],
            "Detinguts relacionats": [num_det],
            "Dia": [dia]
        })

        df = pd.concat([df, nuevo_dato], ignore_index=True)
        save_data(df)
        st.success("Dades enviades, gràcies company. Sobretot no repeteixis l'operació per no duplicar. Fins demà")

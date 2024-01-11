import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




st.title('Empleados pobretones')

# Carga de archivos
trabajadores = "csv/employees.csv"
trabajadores = pd.read_csv(trabajadores)

if st.checkbox("Pulsa para mostrar información de los empleados"):
    st.subheader("Tabla")
    st.write(trabajadores)

st.divider()


# Hacer columna para que salga mas bonito y no con salto de linea.

col1, col2, col3= st.columns(3)

with col1:
    color = st.color_picker("Selecciona un color", "#0069F9")
with col2: 
    nombre = st.toggle("Mostrar el nombre", True)
with col3:
    salario = st.toggle("Mostrar el salario", False)

#color = st.color_picker("Selecciona un color", "#0069F9")
#nombre = st.toggle("Mostrar el nombre", True)
#salario = st.toggle("Mostrar el salario", False)

if nombre:
    plt.barh(trabajadores["full name"], trabajadores["salary"], color=color)
    plt.xlim(0,4600)
else:
    plt.yticks([])  # Elimina las etiquetas del eje y
    plt.barh(trabajadores["full name"], trabajadores["salary"], color=color)
    plt.xlim(0,4600)

if salario:
    for i, v in enumerate(trabajadores["salary"]):
        plt.text(v + 3, i - 0.3, str(v)+"€")

st.pyplot(plt.gcf())
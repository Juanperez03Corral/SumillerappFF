
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chin Chin: Recomendador de vinos con doble recomendación por plato.
"""

import streamlit as st

# Función principal de recomendación con dos vinos por plato
def recomendar_vino(plato, edad, genero, region_favorita):
    if edad < 18:
        return {"mensaje": "Está prohibida la venta de alcohol en España a menores de 18 años."}, 0

    vinos_por_plato = {
        "Gazpacho andaluz": {
            "vinos": [
                {
                    "vino": "Pazo de Señoráns Albariño - Rías Baixas (España)",
                    "uva": "Albariño",
                    "cosecha": "2020",
                    "region": "Rías Baixas, Galicia",
                    "copa": 3.5,
                    "botella": 25.0,
                    "calidad": "Estándar",
                    "explicacion": "Fresco y afrutado, complementa la acidez del gazpacho y realza los sabores de los tomates y pepinos."
                },
                {
                    "vino": "Do Ferreiro Cepas Vellas - Rías Baixas (España)",
                    "uva": "Albariño",
                    "cosecha": "2019",
                    "region": "Rías Baixas, Galicia",
                    "copa": 6.0,
                    "botella": 45.0,
                    "calidad": "Alta gama",
                    "explicacion": "Un albariño complejo y mineral, ideal para sofisticar un plato fresco como el gazpacho."
                }
            ]
        },
        "Tortilla española": {
            "vinos": [
                {
                    "vino": "Marqués de Murrieta Rioja Reserva - Rioja (España)",
                    "uva": "Tempranillo, Mazuelo, Graciano",
                    "cosecha": "2018",
                    "region": "Rioja, La Rioja",
                    "copa": 5.0,
                    "botella": 35.0,
                    "calidad": "Estándar",
                    "explicacion": "Con cuerpo, armoniza bien con la textura de la tortilla y realza el sabor del huevo y la patata."
                },
                {
                    "vino": "La Rioja Alta Gran Reserva 904 - Rioja (España)",
                    "uva": "Tempranillo, Graciano",
                    "cosecha": "2011",
                    "region": "Rioja, La Rioja",
                    "copa": 7.5,
                    "botella": 60.0,
                    "calidad": "Alta gama",
                    "explicacion": "Un clásico elegante con notas complejas que enriquece la experiencia del plato tradicional."
                }
            ]
        }
    }

    recomendacion = vinos_por_plato.get(plato)
    if recomendacion:
        return recomendacion["vinos"], 1
    else:
        return {"mensaje": "No se encontró una recomendación para el plato seleccionado."}, 0

# Interfaz Streamlit
st.title("🍷 Chin Chin: Tu Sumiller Virtual")
st.subheader("Recomendación doble de vinos según tu plato y preferencias")

with st.form("formulario_usuario"):
    nombre = st.text_input("¿Cuál es tu nombre?")
    edad = st.number_input("¿Qué edad tienes?", min_value=0, step=1)
    genero = st.selectbox("¿Cuál es tu género?", ["Prefiero no decirlo", "Femenino", "Masculino", "Otro"])
    region_favorita = st.text_input("¿Cuál es tu región vitivinícola favorita?")
    plato = st.selectbox("Selecciona un plato", ["Gazpacho andaluz", "Tortilla española"])
    enviar = st.form_submit_button("Recomendar vino")

if enviar:
    resultado, exito = recomendar_vino(plato, edad, genero, region_favorita)
    if exito:
        st.success(f"🍷 Recomendaciones para {nombre} ({plato}):")
        for vino in resultado:
            st.write(f"### 🏷️ {vino['calidad']} - {vino['vino']}")
            st.write(f"- **Uva:** {vino['uva']}")
            st.write(f"- **Cosecha:** {vino['cosecha']}")
            st.write(f"- **Región:** {vino['region']}")
            st.write(f"- **Precio por copa:** {vino['copa']}€")
            st.write(f"- **Precio por botella:** {vino['botella']}€")
            st.write(f"- **¿Por qué este vino?:** {vino['explicacion']}")
            st.markdown("---")
    else:
        st.warning(resultado["mensaje"])

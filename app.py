import openai
import streamlit as st
import os

def evaluar_ensayo(ensayo, tipo):
    # Utiliza GPT-3 para evaluar el ensayo
    model_engine = "text-davinci-003"
    if tipo == "argumentativo":
        prompt = (f"Evaluar la calidad del ensayo argumentativo:\n{ensayo}\n\n"
                  "Criterios de evaluación: estructura, coherencia y argumentación. "
                  "Señalar los aspectos positivos y negativos y dar una calificación.")
    else:
        prompt = (f"Evaluar la calidad del ensayo expositivo:\n{ensayo}\n\n"
                  "Criterios de evaluación: claridad, precisión y coherencia. "
                  "Señalar los aspectos positivos y negativos y dar una calificación.")

    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
                                           temperature=0.5)
    respuesta = completions.choices[0].text

    # Devuelve la respuesta de GPT-3
    return respuesta

def main():
    st.title("Evaluador de ensayos con GPT-3")

    # Agrega un campo de texto para ingresar la API key de OpenAI
    openai_api_key = st.text_input("Ingresa tu API key de OpenAI")

    # Autenticación de OpenAI (utiliza la API key ingresada por el usuario)
    openai.api_key = openai_api_key

    tipo = st.selectbox("Selecciona el tipo de ensayo", ["argumentativo", "expositivo"])
    ensayo = st.text_area("Ingresa el ensayo a evaluar. Al finalizar, Ctrl+Enter")
    if ensayo:
        respuesta = evaluar_ensayo(ensayo, tipo)
        st.markdown(respuesta)

if __name__ == "__main__":
  main()

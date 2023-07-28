import os
from dotenv import load_dotenv
import openai

#Carga las variables de entornodesde el archivo ap.env, validar que falta para que funcione
#load_dotenv("../venv/ap.env")
#openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = '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'


#Usando metodo completion para obtener respuesta del modelo
response = openai.Completion.create(
    model='text-davinci-003',
    prompt='Decide si el sentimiento de un Tweet es positivo, neutral, o negativo. \
    \n\nTweet: \"Esta haciendo mucho calor, eso me molesta mucho.\
    \"\nSentiment:',
    #\n\nTweet: \"#LoNuevoEnPlatzi es el Platzibot :robot_face:. Un asistente creado con Inteligencia Artificial para acompañarte en tu proceso de aprendizaje.\
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
)

print(response.choices[0].text)








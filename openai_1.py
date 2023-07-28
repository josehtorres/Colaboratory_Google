import os
import openai

openai.api_key = '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'

#Usando metodo completion para obtener respuesta del modelo
response = openai.Completion.create(
    engine = 'text-davinci-003',
    prompt = 'Quien descubrio America?',
    max_tokens = 50
)

print(response.choices[0].text)








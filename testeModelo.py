#Código feito para realizar a transcrição do audio pela API da OpenIA
#Ecedi o limite de créditos da API então não pude continuar, este código ainda não ta rodando corretamente.

import requests

#OPENAI_API_KEY = "chave_api_openIA" #colar a chave correta
#OPENAI_API_URL = "https://api.openai.com/v1/audio/transcriptions"


audio_file_path = "/Users/sant/job/estudos/testeStatsales/testeVoz.mp3"

with open(audio_file_path, "rb") as audio_file:
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    files = {"file": audio_file}
    data = {"model": "whisper-1"}

    response = requests.post(OPENAI_API_URL, headers=headers, files=files, data=data)

# Processar a resposta
if response.status_code == 200:
    transcription = response.json()
    print("Transcription:", transcription.get("text", "No transcription text found."))
else:
    print(f"Erro {response.status_code}: {response.text}")
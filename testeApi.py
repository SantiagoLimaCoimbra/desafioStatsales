#Aqui estava tentanto execultar a API junto com o modelo de transcrição.
#Para enviar o arquivo é neacessário acessar: "http://127.0.0.1:8000/docs#/default/transcribe_audio_transcribe__post"
#mp4 e m4a estavam dando formato inválido, e 500 sever erro no mp3
#ainda não descobri como resolver, imagino que seja por conta dos créditos também.
#para rodar é: uvicorn testeApi:app --reload

from fastapi import FastAPI, UploadFile, File, HTTPException
import requests
import os

#OPENAI_API_KEY = "chave_api_openIA" #colar a chave correta
#OPENAI_API_URL = "https://api.openai.com/v1/audio/transcriptions"

app = FastAPI()

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    if file.content_type not in ["audio/mpeg", "audio/wav", "audio/mp4", "audio/webm"]: #só não da erro no mp3
        raise HTTPException(status_code=400, detail="Formato de áudio não suportado")
    
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(await file.read())
    
    try:
        # Enviar o áudio para a API da OpenAI
        with open(temp_file_path, "rb") as audio_file:
            headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
            files = {"file": audio_file}
            data = {"model": "whisper-1"}
            
            response = requests.post(OPENAI_API_URL, headers=headers, files=files, data=data)
            response.raise_for_status()
            
            result = response.json()
            return {"transcription": result.get("text", "Transcrição não disponível")}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao transcrever áudio: {str(e)}")
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
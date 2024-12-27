#Esta seria a forma mais simples de transcrever o audio já baixado na máquina,
#porém, estou com alguns problemas para instalar o whisper localente, então não
#pude rodar este código.

import whisper

modelo = whisper.load_model("base")
resposta = model.transcribe("testeVoz.mp3")

print(resposta)
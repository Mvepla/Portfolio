from flask import Flask, jsonify, render_template, request, send_file
from gtts import gTTS
import requests
import os 
from pymongo import MongoClient 
from pdfminer.high_level import extract_text 
from gridfs import GridFS
from PyPDF2 import PdfReader
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

#conexiones con BBDD
mongo_url ='mongodb+srv://falberola:5zZi7xSEYPPIdGgc@cluster0.hd9lmf3.mongodb.net/datadmin_fincas'
client = MongoClient(mongo_url)
db = client.get_database('datadmin_fincas')
resumen_collection = db['resumen'] 
audios_collection = db['audios'] 

@app.route('/', methods=['GET'])
def plantilla():
    return render_template('endpoints.html')

@app.route('/subir_pdf', methods=['POST'])
def prueba():
    if 'file' not in request.files:
        return "No se proporcionó ningún archivo"
    file = request.files['file']
    file_name = file.filename

    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    API_TOKEN = "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"
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    resumen = query({"inputs": text})
    contenido_resumen = resumen[0][next(iter(resumen[0]))]   

    texto = contenido_resumen
    tts = gTTS(text=texto, lang='es')
    tts.save("audio.mp3")   

    resumen_collection.insert_one({'resumen': contenido_resumen})

    local_audio_file = './audio.mp3'

    # Connect to the GridFS collection
    fs_pdf = GridFS(db, collection='pdfs')
    fs_audio = GridFS(db, collection='audios')

    with open(local_audio_file, 'rb') as audio_file:
        # Save the binary content to GridFS
        audio_file_id = fs_audio.put(audio_file, filename=f"{file_name}.mp3", metadata={'folder': 'audios'})
    pdf_file_id = fs_pdf.put(file, filename=file_name, metadata={'folder': 'pdfs'})


    return jsonify({'message': f'Archivo de audio "{file_name}" generado y guardado correctamente'}), 201

@app.route('/resumen', methods=['GET','POST'])
def resumen():
    document = resumen_collection.find_one()

    if document:
        resumen_texto = document.get('resumen')
    else:
        print("No se ha encontrado ningún resumen en la base de datos")

    return jsonify({'resumen': resumen_texto})

@app.route('/audio', methods=['GET','POST'])
def audio():
    fs_audio = GridFS(db, collection='audios')

    # Assuming there's only one audio file, retrieve it
    audio_file = fs_audio.find_one()

    if audio_file:
        # Set the appropriate response headers
        response_headers = {
            'Content-Type': 'audio/mp3',
            'Content-Disposition': f'attachment; filename={audio_file.filename}'
        }

        # Return the audio file as a response
        return send_file(audio_file, as_attachment=True, download_name=audio_file.filename, mimetype='audio/mp3')

    else:
        return "No audio files found in the collection."

if __name__ == '__main__':
    app.run(debug=True,port=8000)
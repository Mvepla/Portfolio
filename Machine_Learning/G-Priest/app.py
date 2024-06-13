from flask import Flask, request, render_template, jsonify
import cohere


app = Flask(__name__)

API_KEY= '******'


co = cohere.Client(API_KEY)

def generate_catholic_priest_response(user_prompt):
    contexto_inicial = """Eres un sacerdote católico que ayuda a las personas con sus dudas existenciales y problemas diarios. Proporcionas respuestas basadas en versículos de la Biblia, explicándolos de manera concisa y didáctica para que NO excedan los 150 tokens.
Estructura tus respuestas en párrafos bien formateados: introducción que contextualice la pregunta del usuario, cita del versículo relevante (incluyendo libro, capítulo y versículo), explicación breve y clara del versículo y su relación con la situación del usuario, y penitencia apropiada SOLO si el usuario menciona haber cometido un pecado o su duda tiene relacion con un pecado.
Utiliza versículos apropiados según la pregunta, de versiones de la Biblia aprobadas por la Iglesia Católica.
Mantén un tono didáctico y empático, asegurándote de que las respuestas sean comprensibles para personas sin conocimientos teológicos profundos.
Asegúrate de que las respuestas sean directas, con ejemplos y analogías cuando sea necesario, y que TODA la informacion de la respuesta no exceda los 150 tokens en total.
"""
    prompt_completo = f"{contexto_inicial}\n{user_prompt}"

    response = co.chat(
        model='command-r-plus',
        message=prompt_completo,
        prompt_truncation="auto",
        connectors=[{"id": "web-search"}],
    )
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_prompt = request.form['user_prompt']
    response = generate_catholic_priest_response(user_prompt)
    # Formatear la respuesta para que esté en párrafos
    formatted_response = response.replace("\n", "<br>")
    return jsonify({'response': formatted_response})

if __name__ == "__main__":
    app.run(debug=True)

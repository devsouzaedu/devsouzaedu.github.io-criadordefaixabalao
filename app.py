from flask import Flask, render_template, request
from PIL import Image, ImageDraw
import os

app = Flask(__name__)

def criar_faixa(altura, largura_cima, largura_baixo, num_gomos, logo_path):
    # Lógica para criar a faixa conforme fornecido anteriormente

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar_faixa', methods=['POST'])
def criar_faixa_route():
    altura = int(request.form['altura'])
    largura_cima = int(request.form['larguraCima'])
    largura_baixo = int(request.form['larguraBaixo'])
    num_gomos = int(request.form['numGomos'])
    logo = request.files['logo']
    logo.save('logo.png')  # Salva o logo como 'logo.png' localmente
    criar_faixa(altura, largura_cima, largura_baixo, num_gomos, 'logo.png')
    return 'Faixa criada com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import BancoLogin as BL
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    mensagem = ''
    if request.method == 'POST':
        mensagem = request.form.get('Usuario', '').strip()
        senha = request.form.get('Senha', '').strip()
        BL.main(usuario=mensagem, senha=senha)
        print(mensagem, senha)
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
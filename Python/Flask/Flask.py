from flask import Flask, render_template, request, redirect, url_for
import BancoLogin as BL
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    mensagem = request.args.get('mensagem', '')  
    if request.method == 'POST':
        action = request.form['action']
        if action == 'register':
            registrar_dados()
            return redirect(url_for('home', mensagem=''))
        if action == 'login':
            mensagem = 'Não existe esse login'
            return redirect(url_for('home', mensagem=mensagem))
            pass
    
    return render_template('index.html', mensagem=mensagem)
#arrumar a mesanagem que esta reperindo

def registrar_dados():
    mensagem = request.form.get('Usuario', '').strip()
    senha = request.form.get('Senha', '').strip()
    BL.main(usuario=mensagem, senha=senha)
    print(mensagem, senha)

if __name__ == '__main__':
    app.run(debug=True)
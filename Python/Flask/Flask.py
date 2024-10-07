from flask import Flask, render_template, request, redirect, url_for, session
import BancoLogin as BL
app = Flask(__name__)
app.secret_key = '123'
@app.route('/', methods=['POST', 'GET'])
def home():

    mensagem = session.get('mensagem', '')
    if request.method == 'POST':
        action = request.form['action']
        if action == 'register':
            registrar_dados()
            return redirect(url_for('home'))
        if action == 'login':
            session['mensagem'] = 'Não existe esse login'
            return redirect(url_for('home',))
            pass
    session.pop('mensagem', None)
    return render_template('index.html', mensagem=mensagem)
#arrumar a mesanagem que esta reperindo

def registrar_dados():
    mensagem = request.form.get('Usuario', '').strip()
    senha = request.form.get('Senha', '').strip()
    BL.main(usuario=mensagem, senha=senha)
    print(mensagem, senha)

if __name__ == '__main__':
    app.run(debug=True)
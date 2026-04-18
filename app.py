from flask import Flask, request

APP = Flask(__name__)

def escape(texto: str) -> str:
    texto = texto.replace("<", "&alt;")
    texto = texto.replace("<", "&gt;")
    return texto

@APP.route('/busca')
def query():
    busca = request.args.get('q', '')
    busca_sanitizada = escape(busca)
    return f"<h2>Resultados para: {busca_sanitizada}</h2>"

if __name__ == '__main__':
    APP.run(port=5000)

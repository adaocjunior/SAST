from flask import Flask, request

APP = Flask(__name__)

@APP.route('/busca')
def query():
    busca = request.args.get('q', '')

    return f"<h2>Resultados para: {busca}</h2>"

if __name__ == '__main__':
    APP.run(port=5000)

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('glowna.html')

@app.route('/name', defaults={'name': "Anonim"})
@app.route('/name/<name>')
def name(name=None):
    return f"Hello, {name}!"

@app.route('/author')
def author():
    return render_template('autor.html')

@app.route('/ekstrakcja')
def ekstrakcja():
    return render_template('ekstrakcja.html')

@app.route('/lista_produktow')
def listaproduktow():
    return render_template('lista_produktow.html')

@app.route('/produkt')
def produkt():
    return render_template('produkt.html')
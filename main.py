from flask import Flask, render_template, url_for
from random import randint

app = Flask(__name__)

meus_cartoes = ['Roxinho','Santander Play','C6']

@app.route('/')
def home():
    #Aqui dentro você pode colocar o HTML da sua página
    return render_template('home.html')

@app.route('/mywallet')
def my_wallet():
    return render_template('my_wallet.html',meus_cartoes=meus_cartoes)

@app.route('/cards')
def my_cards ():
    return render_template('my_cards.html',meus_cartoes=meus_cartoes)

if __name__ == "__main__" :
    app.run(debug=True)
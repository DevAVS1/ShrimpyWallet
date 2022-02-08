from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    #Aqui dentro você pode colocar o HTML da sua página
    return render_template('home.html')

@app.route('/mywallet')
def my_wallet():
    valor = randint(0,1000)
    return render_template('my_wallet.html')

if __name__ == "__main__" :
    app.run()
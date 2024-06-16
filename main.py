from flask import Flask, render_template, redirect, request
import mysql.connector

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods=['post'])
def login():
    
    
    email_user = request.form.get('email_user')
    senha = request.form.get('senha')

    with open("cursor") as usuariostemp:
        usuarios = mysql.load(usuariostemp)
        cont =  0
        for usuario in usuarios:
            cont += 1
            if usuario['email_user'] == email_user and usuario['senha'] == senha:
                return render_template("lobi.html")
            
            if cont >= len(usuarios):
                return render_template("index.html")





if __name__ in "__main__":
    app.run(debug=True)
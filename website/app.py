
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuration de la connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="database_pizza"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT nom from garnitures")
    garnitures = cursor.fetchall()
    cursor.close()

    cursor = db.cursor()
    cursor.execute("SELECT nom from sauces")
    sauces = cursor.fetchall()
    cursor.close() 

    cursor = db.cursor()
    cursor.execute("SELECT nom from croutes")
    croutes = cursor.fetchall()
    cursor.close() 
    return render_template('commandes.html', garnitures=garnitures, sauces=sauces, croutes=croutes)

if __name__ == '__main__':
    app.run(debug=True)


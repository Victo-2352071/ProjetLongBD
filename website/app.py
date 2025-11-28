
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuration de la connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="credit_social"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * from citoyen")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

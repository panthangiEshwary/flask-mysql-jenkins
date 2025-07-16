from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    conn = mysql.connector.connect(
        host='mysql',
        user='root',
        password='rootpass',
        database='testdb'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT message FROM greetings LIMIT 1;')
    result = cursor.fetchone()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


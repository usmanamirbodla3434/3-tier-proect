from flask import Flask, request, render_template
import mysql.connector
import time

app = Flask(__name__)

def get_db_connection():
    for i in range(15):
        try:
            conn = mysql.connector.connect(host="db", user="root", password="root_password", database="usman_db")
            return conn
        except:
            time.sleep(5)
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    name = request.form.get('name')
    email = request.form.get('email')
    exp = request.form.get('experience')
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS portal_logs (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), experience VARCHAR(255))")
        cursor.execute("INSERT INTO portal_logs (name, email, experience) VALUES (%s, %s, %s)", (name, email, exp))
        conn.commit()
        cursor.close()
        conn.close()
        return f"<body style='background:#020617; color:#c5a059; text-align:center; padding-top:100px; font-family:sans-serif;'><h1>Commit Successful!</h1><p style='color:white;'>Data for {name} has been synced with the database.</p><br><a href='/' style='color:#c5a059;'>Back to Portal</a></body>"
    return "DB Connection Failed."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

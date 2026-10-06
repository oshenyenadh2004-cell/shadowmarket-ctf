from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Initialize a basic database with one admin user
def init_db():
    conn = sqlite3.connect('ctf.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    # Clear existing data and insert admin
    c.execute('''DELETE FROM users''')
    c.execute('''INSERT INTO users VALUES ('admin', 'supersecret_backend_pass')''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # INTENTIONALLY VULNERABLE QUERY: Direct string concatenation
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        conn = sqlite3.connect('ctf.db')
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                return "<h1>Vendor Dashboard</h1><p>Welcome back. Flag: SHADOWMKT{SQL_BYP4SS_SUCC3SS}</p>"
            else:
                return "<h1>Access Denied</h1><p>Invalid credentials.</p>"
        except Exception as e:
            return f"<h1>Database Error</h1><p>{e}</p>"
        
    return '''
        <h2>ShadowMarket Vendor Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

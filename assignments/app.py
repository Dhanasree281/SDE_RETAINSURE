from flask import Flask, request, jsonify, redirect
import sqlite3
app = Flask(__name__)
DATABASE = 'urls.db'

# ✅ Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ✅ Function to create the table
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_id TEXT NOT NULL UNIQUE,
                clicks INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
@app.route('/')
def home():
    return "URL Shortener is working!"

# ✅ This part should be at the end
if __name__ == '__main__':
    init_db()          # create the table if not exists
    app.run(debug=True)

# Dictionary to store the shortened URLs
url_map = {}

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data['url']
    short_id = 'abc123'  # static short ID for testing
    url_map[short_id] = original_url
    return jsonify({'short_url': f'http://127.0.0.1:5000/{short_id}'})
@app.route('/')
def home():
    return "👋 Welcome to the URL Shortener API! Use /shorten to shorten your links."


@app.route('/<short_id>')
def redirect_url(short_id):
    if short_id in url_map:
        return redirect(url_map[short_id])
    return "Short URL not found", 404
from flask import Flask, request, jsonify, redirect, render_template

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    url = request.form.get('url') or request.get_json()['url']
    short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_map[short_id] = url
    return f"Short URL: http://127.0.0.1:5000/{short_id}"
# Show all shortened URLs
@app.route('/stats')
def stats():
    conn = get_db_connection()
    urls = conn.execute('SELECT original_url, short_id FROM urls').fetchall()
    conn.close()
    return render_template('stats.html', urls=urls)



if __name__ == '__main__':
    app.run(debug=True)

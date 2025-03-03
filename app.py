from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('mood_journal.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mood_entries
                 (id INTEGER PRIMARY KEY, date TEXT, mood TEXT, note TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entries')
def get_entries():
    conn = sqlite3.connect('mood_journal.db')
    c = conn.cursor()
    c.execute("SELECT date, mood, note FROM mood_entries ORDER BY date DESC")
    entries = [{'date': row[0], 'mood': row[1], 'note': row[2]} for row in c.fetchall()]
    conn.close()
    return jsonify(entries)

@app.route('/add-entry', methods=['POST'])
def add_entry():
    data = request.json
    mood = data.get('mood')
    note = data.get('note')
    date = datetime.now().strftime("%Y-%m-%d")

    if not mood or not note:
        return jsonify({'message': 'Mood and note are required!'}), 400

    conn = sqlite3.connect('mood_journal.db')
    c = conn.cursor()
    c.execute("INSERT INTO mood_entries (date, mood, note) VALUES (?, ?, ?)", (date, mood, note))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Entry added successfully!'})

@app.route('/mood-trend')
def mood_trend():
    conn = sqlite3.connect('mood_journal.db')
    c = conn.cursor()
    c.execute("SELECT date, mood FROM mood_entries ORDER BY date ASC")
    data = c.fetchall()
    conn.close()

    dates = [entry[0] for entry in data]
    moods = [entry[1] for entry in data]

    return jsonify({'dates': dates, 'moods': moods})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

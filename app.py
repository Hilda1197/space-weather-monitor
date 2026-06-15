from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('events.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/events')
def get_events():
    min_ky = request.args.get('min_ky', type=float)
    max_ky = request.args.get('max_ky', type=float)
    
    conn = get_db_connection()
    query = "SELECT * FROM interruptions WHERE 1=1"
    params = []
    
    if min_ky is not None:
        query += " AND ky_index >= ?"
        params.append(min_ky)
    if max_ky is not None:
        query += " AND ky_index <= ?"
        params.append(max_ky)
    
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/stats')
def get_stats():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT interruption_type, COUNT(*) as count FROM interruptions GROUP BY interruption_type", conn)
    conn.close()
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Attempt to reach across the Docker Network to log into PostgreSQL
        conn = psycopg2.connect(
            host="my-db",
            database="portfolio",
            user="akshay",
            password="supersecret"
        )
        db_status = "SUCCESS: The Python Brain is connected to the PostgreSQL Memory!"
        conn.close()
    except Exception as e:
        db_status = f"FAILED: Could not connect to database. Error: {str(e)}"

    return jsonify({
        "status": "success",
        "message": "Hello Akshay, your Python Backend is officially running!",
        "tier": "Backend API",
        "database_status": db_status
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

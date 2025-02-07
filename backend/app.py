from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# データベース接続関数
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="event_management",
        user="admin",
        password="admin"
    )
    conn.set_client_encoding('UTF8')  # エンコーディング設定
    return conn

# テスト用ルート
@app.route('/')
def index():
    return "Flask app is running!"

# 出欠情報を受け取るエンドポイント
@app.route('/attendance', methods=['POST'])
def handle_attendance():
    data = request.form
    print(f"Received data: {data}")  # デバッグ用ログ

    event_id = data.get('event_id')
    status = data.get('status')
    user_id = 1  # 仮のユーザーID

    if not event_id or not status:
        return jsonify({"error": "Invalid data"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO attendance (user_id, event_id, status) VALUES (%s, %s, %s)",
            (user_id, event_id, status)
        )
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Attendance saved successfully"}), 200
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"error": "Failed to save attendance"}), 500

if __name__ == '__main__':
    app.run(debug=True)

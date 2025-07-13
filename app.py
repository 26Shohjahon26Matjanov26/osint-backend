from flask import Flask, request, jsonify

app = Flask(__name__)

logs = []

@app.route('/track')
def track():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    query_id = request.args.get('id', 'NoID')

    log_entry = {
        'ip': ip,
        'user_agent': user_agent,
        'id': query_id
    }

    logs.append(log_entry)
    return "✅ Tracked", 200

@app.route('/getlogs')
def getlogs():
    return jsonify(logs)

@app.route('/clearlogs', methods=['POST'])
def clearlogs():
    logs.clear()
    return "🧹 Cleared", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

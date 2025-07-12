logs.append(log_entry)
    return "✅ OK", 200

# Loglarni ko‘rish
@app.route('/getlogs')
def getlogs():
    return jsonify(logs)

# Loglarni tozalash
@app.route('/clearlogs', methods=['POST'])
def clearlogs():
    logs.clear()
    return "🧹 Cleared", 200

# Flask serverni ishga tushirish
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

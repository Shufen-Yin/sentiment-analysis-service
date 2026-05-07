from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Shufen's Sentiment Analysis Service! (v2)"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    prediction = predict_sentiment(data['text'])
    return jsonify({
        "input": data['text'],
        "label": prediction['label'],
        "score": prediction['score']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Function to send data to external OpenRouter API
def get_data(tweet):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }

    data = {
        "model": "deepseek/deepseek-chat-v3.1",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"observed: {tweet} ,possible disasters: EarthQuake, Tsunami, Cyclone. Pick one from possible disaster by observing the observed. Give one word answer, no explanation."}
        ],
        "max_tokens": 1000,
        "stream": False
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        # Extract the answer text from response
        answer = result['choices'][0]['message']['content'].strip()
        return answer
    else:
        return f"Error: {response.status_code}, {response.text}"

# API endpoint to process input tweet
@app.route('/response',methods = ['POST'])
def process_data():
    data = request.get_json()
    ip = data.get('input')
    op = get_data(ip)
    return jsonify({"responce":op})


# Run the Flask microservice
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug = True)

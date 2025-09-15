import requests

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "deepseek/deepseek-chat-v3.1",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"observed: {tweet} ,possible disaters:EarthQuake,Tsunami,Cyclone,Pick one from possible disaster by observing the observed. Give one word answer no explaination"

}
    ],
    "max_tokens": 1000,  
    "stream": False
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['message']['content'])
else:
    print(f"Error {response.status_code}: {response.text}")

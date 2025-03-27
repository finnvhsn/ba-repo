import requests
import json

def get_response(prompt = "What is HPE?", model= "mistral-openorca",ip_adress="10.1.25.121"):
    chat_content = [
        {
            "role": "user",
            "content": "why is the sky blue?"
        }
    ]
    payload = {
    "model": model,
    "messages": chat_content,
    "stream": False
}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'http://{ip_adress}:11434/api/chat', data=json.dumps(payload), headers=headers)
 
    return response.json()['message']['content']
 
print(get_response())
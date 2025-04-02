import requests
import json

def query(prompt, model="codellama", ip_address="10.1.25.121"):
    #codellama is implemented as standard model, as far as no other is defined in argument.
    chat_content = [{"role": "user", "content": prompt}]
    payload = {
        "model": model,
        "messages": chat_content,
        "stream": False,
        "temperature": 0.0 #tells about creativity level of model in generating the solution. 0.0 temperature = very conservative
    }
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(f'http://{ip_address}:11434/api/chat', data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        return response.json()['message']['content']
    except requests.RequestException as e:
        return f"[ERROR] {str(e)}"

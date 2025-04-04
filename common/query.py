import requests
import json

def query(prompt, model="deepseek-coder:6.7b", ip_address="10.1.25.121"):
    chat_content = [{"role": "user", "content": prompt}]
    payload = {
        "model": model,
        "messages": chat_content,
        "stream": False,
        "temperature": 0.0
    }
    headers = {'Content-Type': 'application/json'}
    url = f"http://{ip_address}:11434/api/chat"

    try:
        #print(f"Sende Anfrage an {model} @ {ip_address} ...")
        response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()['message']['content']
    except requests.exceptions.Timeout:
        print("⏱️ Timeout: Der Server hat nicht rechtzeitig geantwortet.")
        return "[ERROR] timeout"
    except requests.exceptions.RequestException as e:
        print(f"Anfrage fehlgeschlagen: {e}")
        return f"[ERROR] {str(e)}"



import requests
import json

OLLAMA_HOST = "http://10.1.25.121:11434" 
MODEL_NAME = "starcoder2:15b"

def is_model_present(model_name):
    try:
        response = requests.get(f"{OLLAMA_HOST}/api/tags")
        response.raise_for_status()
        models = response.json().get("models", [])
        return any(model.get("name") == model_name for model in models)
    except Exception as e:
        print(f"Fehler beim Abrufen der Modell-Liste: {e}")
        return False

def pull_model(model_name):
    print(f"⬇️  Lade Modell: {model_name} ...")
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/pull",
            data=json.dumps({
                "model": model_name,
                "stream": False  # Setze auf True, wenn du Streaming-Ausgabe brauchst
            }),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        print(f"✅ Erfolgreich geladen: {response.json()}")
    except Exception as e:
        print(f"Fehler beim Download: {e}")

if __name__ == "__main__":
    if is_model_present(MODEL_NAME):
        print(f"✅ Modell '{MODEL_NAME}' ist bereits vorhanden.")
    else:
        pull_model(MODEL_NAME)

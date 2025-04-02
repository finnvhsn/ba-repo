import argparse
import requests
import json

def pull_model(model_name, host="localhost", port=11434):
    url = f"http://{host}:{port}/api/pull"
    payload = {"model": model_name}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), stream=True)
        response.raise_for_status()

        print(f"📥 Pulling model '{model_name}' from {host}:{port}...\n")
        for line in response.iter_lines():
            if line:
                status = json.loads(line)
                print("🔄", status.get("status", ""))
        print("\n✅ Model pull complete!")
    except requests.RequestException as e:
        print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pull a model from Ollama server")
    parser.add_argument("--model", required=True, help="Model name (e.g. starcoder2:15b)")
    parser.add_argument("--host", default="localhost", help="Host address of Ollama server (default: localhost)")
    parser.add_argument("--port", default=11434, type=int, help="Port of Ollama server (default: 11434)")

    args = parser.parse_args()
    pull_model(args.model, args.host, args.port)


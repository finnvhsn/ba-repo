# ba-repo
venv\Scripts\Activate.ps1

Localhost adress: 10.1.25.121

Used GPU on Virtual Machine:

NVDIA L40S 48GB

Potential Evaluation Models:
mixtral latest --> 46.7b URL: https://ollama.com/library/mixtral:latest
deepseek-r1 70.6b URL: https://ollama.com/library/deepseek-r1:70b
llama 3.3 70.6b URL: https://ollama.com/library/llama3.3:latest

Temperature: 0.0

for pulling models:
bash: curl http://10.1.25.121:11434/api/pull -d '{ "model": "qwen2.5-coder:7b" }' -H "Content-Type: application/json"


models pulled:
deepseek-coder:6.7b
codegemma:7b
deepseek-r1:7b
qwen2.5:7b
qwen2.5-coder:7b



delete Model from ollama server:
curl -X DELETE http://10.1.25.121:11434/api/delete -d '{ "model": "deepseek-r1:7b" }'


direkter zugriff:
curl http://10.1.25.121:11434/api/generate -d '{
  "model": "mistral:7b",
  "prompt": "write a python function that defies prime numbers in the range of 1 to 10",
  "temperature": 0.2
}'

Show all listed ollama models:
bash: curl http://10.1.25.121:11434/api/tags


delete table in db:
python db_commun.py --db humaneval.db --table "starcoder2:7b_results" --drop

# ba-repo
venv\Scripts\Activate.ps1

Localhost adress: 10.1.25.121

Used GPU on Virtual Machine:

NVDIA L40S 48GB


Coding Models:

starcoder2 7b URL: https://ollama.com/library/starcoder2:7b
wizardcoder latest = 6.74b URL: https://ollama.com/library/wizardcoder:latest
codellama latest 6.74b URL: https://ollama.com/library/codellama:latest
deepseek-coder latest 1.35b URL: https://ollama.com/library/deepseek-coder:latest


General Task Models:

mistral:7b 7.25b URL: https://ollama.com/library/mistral:7b 
llama 3.2 3.21b URL: https://ollama.com/library/llama3.2:latest
llama 3.3 70.6b URL: https://ollama.com/library/llama3.3:latest
gemma2:27b URL: https://ollama.com/library/gemma2:27b
gemma2 latest 9.24b URL:https://ollama.com/library/gemma2:latest
deepseek-r1 70.6b URL: https://ollama.com/library/deepseek-r1:70b



Potential Evaluation Models:
mixtral latest --> 46.7b URL: https://ollama.com/library/mixtral:latest
deepseek-r1 70.6b URL: https://ollama.com/library/deepseek-r1:70b
llama 3.3 70.6b URL: https://ollama.com/library/llama3.3:latest

Temperature: 0.0

for pulling models:
bash: curl http://10.1.25.121:11434/api/pull -d '{ "model": "codegemma:2b" }' -H "Content-Type: application/json"


models pullecurld:


deepseek-coder-v2:latest (16b)
codegemma:2b
gemma:2b
deepseek-v2:16b


delete Model from ollama server:
curl -X DELETE http://10.1.25.121:11434/api/delete -d '{ "model": "deepseek-r1:14b" }'


direkter zugriff:
curl http://10.1.25.121:11434/api/generate -d '{
  "model": "deepseek-coder-v2",
  "prompt": "write a python function that defies prime numbers in the range of 1 to 10",
  "temperature": 0.2
}'

Show all listed ollama models:
bash: curl http://10.1.25.121:11434/api/tags


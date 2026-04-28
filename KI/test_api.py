import json
import os
from urllib.request import Request, urlopen

api_key = os.environ.get("CHATAI_API_KEY")
if api_key is None:
    raise RuntimeError("CHATAI_API_KEY ist nicht gesetzt.")

url = "https://chat-ai.academiccloud.de/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
payload = {
    "model": "meta-llama-3.1-8b-instruct",
    "messages": [
        {
            "role": "user",
            "content": "Hallo! Bitte stelle dich kurz vor.",
        }
    ],
}

request = Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers=headers,
    method="POST",
)

with urlopen(request) as response:
    data = json.load(response)

print(data["choices"][0]["message"]["content"])
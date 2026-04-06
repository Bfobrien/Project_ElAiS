import requests


def standby():
    while True:
        user_prompt = input("\nElAiS is on standby, waiting for you... \nUSER INPUT: ")
        promptElais(user_prompt)

#Send a prompt to the Elais with provided information
def promptElais(input: str):
    # this is where Ollama operates from on the AI server.IP address may change once the network is set up.
    url = "http://10.0.30.3:11434/api/generate"

    payload = {
        "model": "Elais",
        "prompt": input,
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    print("\nElAiS: ", data["response"])


if __name__ == "__main__":
    standby()

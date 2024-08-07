# first line: 1
@cache(memory, "CLAIR_preferences")
def query_chat_model(user_prompt, system_prompt='', url='https://api.openai.com/v1/chat/completions', model_name='gpt-4-0125-preview'):
    print(f"Querying {model_name} API at {url}...")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        **model_kwargs
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

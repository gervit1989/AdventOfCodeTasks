with open('openai-token.txt','r') as file:
    token = file.readline().strip()

token = "sk-proj-" + token[:3:-1] if token.startswith('gpt:') else token
print(token)
import openai

openai.api_key = "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"

prompt = input("> ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": f"{prompt}"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)
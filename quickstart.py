import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    messages=[
        {
            "role": "user",
            "content": "What are strategies that I should use to improve my spanish speaking and writing ability using journaling. Be concise",
        }
    ],
)
print(message.content[0].text)
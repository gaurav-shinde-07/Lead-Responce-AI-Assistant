def extract_info(message, prompt, client):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt + message}],
        temperature=0
    )
    return response.choices[0].message.content

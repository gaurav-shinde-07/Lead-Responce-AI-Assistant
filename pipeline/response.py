def generate_response(data, questions, prompt, client):
    combined = f"{data}\n{questions}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt + combined}],
        temperature=0.5
    )
    return response.choices[0].message.content

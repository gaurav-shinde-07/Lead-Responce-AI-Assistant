def generate_questions(data, prompt, client):
    response = client.models.generate_content(
        model="models/gemini-1.5-flash",
        contents=prompt + str(data)
    )
    return response.text

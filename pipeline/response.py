def generate_response(data, questions, prompt, client):
    combined = f"{data}\n{questions}"
    response = client.models.generate_content(
        model="models/gemini-1.5-flash",
        contents=prompt + combined
    )
    return response.text

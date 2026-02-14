def extract_info(message, prompt, client):
    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt + message
    )
    return response.text

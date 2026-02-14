def extract_info(message, prompt, client):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt + message
    )
    return response.text

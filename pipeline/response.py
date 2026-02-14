def generate_response(data, questions, prompt, model):
    combined = f"{data}\n{questions}"
    response = model.generate_content(prompt + combined)
    return response.text

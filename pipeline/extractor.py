def extract_info(message, prompt, model):
    response = model.generate_content(prompt + message)
    return response.text

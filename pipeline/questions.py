def generate_questions(data, prompt, model):
    response = model.generate_content(prompt + str(data))
    return response.text

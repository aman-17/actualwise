import os
import openai
import json

openai.api_type = "azure"
openai.api_key = ""
openai.api_base = "https://test-gpt-4-ks.openai.azure.com"
openai.api_version = "2023-05-15"
openai.log = "debug"


with open('./questions.txt', 'r') as file:
    questions = [line.strip() for line in file]

def chunk_text(text, chunk_size=8192):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def process_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    chunks = chunk_text(text)
    messages = []
    for chunk in chunks:
        if len(chunk) > 8192:
            print(f"Warning: chunk is too large ({len(chunk)} tokens)")
            continue
        for question in questions:
            prompt = f"{chunk}\n{question}"
            messages.append({
                "role": "system",
                "content": "You are a helpful assistant."
            })
            messages.append({
                "role": "user",
                "content": prompt
            })
    return messages

def get_responses(messages):
    responses = []
    response = openai.ChatCompletion.create(
        deployment_id="test",
        messages=messages,
    )
    responses.append(response["choices"][0]["message"]["content"])
    return responses

def save_responses_to_file(responses, output_file):
    with open(output_file, 'w') as f:
        for response in responses:
            f.write(f"{response}\n{'-'*30}\n")

def process_files_in_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    for filename in files:
        file_path = os.path.join(folder_path, filename)
        output_file = os.path.join(folder_path, f'output_{filename}')
        messages = process_file(file_path)
        responses = get_responses(messages)
        print(responses)
        save_responses_to_file(responses, output_file)

folder_path = "./deid/"
process_files_in_folder(folder_path)

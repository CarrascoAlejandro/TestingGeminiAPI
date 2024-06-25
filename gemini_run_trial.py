import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDZjGnfnrbrMwcSiw0yojUvVTWQP7DHqcE")

model = genai.GenerativeModel('gemini-1.5-flash')

# GoogleAI invocation function
def run_trial():
    prompt = input("Enter a prompt: ")
    # Run the model
    return model.generate_content(prompt)


def run_trial_from_txt():
    with open('output/article_content.txt', 'r', encoding='utf-8') as file:
        prompt = file.read()
    print("Prompt\n", prompt)
    return model.generate_content("Escribe un resumen en 140 caracteres o menos sobre la siguiente noticia:\n" + prompt)

# Main
if __name__ == "__main__":
    print(run_trial_from_txt())


import openai
import os

openai.api_key = "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"
print(openai.api_key)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    print(response.choices[0].message["content"])
    return response.choices[0].message["content"]


topic = f"""Write an article on the purpose of Technology"""

prompt = f"""Your task is to generate an article on the ```{topic}```,
delimited by triple backticks."""

response = get_completion(prompt)
print(response)

import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]
MODEL = "text-davinci-003"

def create_completion(prompt):
	completion = openai.Completion.create(
    	prompt=prompt, model=MODEL, temperature=1, max_tokens=128
	)
	return completion

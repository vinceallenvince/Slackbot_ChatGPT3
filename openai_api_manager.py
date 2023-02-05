import openai

class OpenAIManager():

	def __init__(self, api_key, model):
		self.api_key = api_key
		self.model = model
		openai.api_key = api_key

	def __str__(self):
		return f"Model: {self.model}"

	def create_completion(self, prompt, temperature=1):
		completion = openai.Completion.create(
    		prompt=prompt, model=self.model, temperature=temperature, max_tokens=128
		)
		return completion
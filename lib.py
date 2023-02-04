import os
import openai

from google.cloud import secretmanager

def access_secret_version(secret_id, version_id="latest"):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/home-375920/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Return the decoded payload.
    return response.payload.data.decode('UTF-8')

openai.api_key = access_secret_version("OPENAI_API_KEY")
MODEL = "text-davinci-003"

def create_completion(prompt):
	completion = openai.Completion.create(
    	prompt=prompt, model=MODEL, temperature=1, max_tokens=128
	)
	return completion

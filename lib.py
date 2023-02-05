import os
import openai

from google.cloud import secretmanager

openai.api_key = access_secret_version("OPENAI_API_KEY")
MODEL = "text-davinci-003"

def access_secret_version(secret_id, version_id="latest"):

	project_id = os.environ["PROJECT_ID"]

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Return the decoded payload.
    return response.payload.data.decode('UTF-8')

def create_completion(prompt):
	completion = openai.Completion.create(
    	prompt=prompt, model=MODEL, temperature=1, max_tokens=128
	)
	return completion

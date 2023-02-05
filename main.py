import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from google.cloud import logging
logging_client = logging.Client()
logger = logging_client.logger("slackbot_gpt_logger")
logger.log_text("Starting app...")

from google.cloud import secretmanager
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

import openai
openai.api_key = access_secret_version("OPENAI_API_KEY")
MODEL = "text-davinci-003"

def create_completion(prompt):
	completion = openai.Completion.create(
    	prompt=prompt, model=MODEL, temperature=1, max_tokens=128
	)
	return completion

# Install the Slack app and get xoxb- token in advance from the OAuth & Permissions section of your app's config
# Bot tokens represent a bot associated with the app installed in a workspace. Unlike user tokens, they're not tied to a user's identity; they're just tied to your app.
app = App(token=access_secret_version("SLACK_BOT_GPT3_TOKEN"))
slack_app_gpt3_token = access_secret_version("SLACK_APP_GPT3_TOKEN")

@app.event("app_mention")
def event_test(event, say):
	
	user_id = event["user"]

	completion = create_completion(event["text"])
	completion_text = completion.choices[0].text

	text = f"<@{user_id}> {completion_text}"

	logger.log_text(f"completion response: {text}")

	say(text)

if __name__ == "__main__":
	#App-level tokens represent your app across organizations, including installations by all individual users on all workspaces in a given organization.
	#App-level token strings begin with xapp-. We sometimes refer to them as "zap!" tokens.
    logger.log_text("... app started")
    SocketModeHandler(app, slack_app_gpt3_token).start()

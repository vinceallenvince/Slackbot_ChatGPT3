import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from lib import create_completion
from lib import access_secret_version

from google.cloud import logging
logging_client = logging.Client()
logger = logging_client.logger("slackbot_gpt_logger")
logger.log_text("Starting app...")


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

import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from secrets import Secrets
secrets_mgr = Secrets(os.environ["PROJECT_ID"])

OPENAI_API_KEY = secrets_mgr.access_secret_version("OPENAI_API_KEY")
SLACK_BOT_GPT3_TOKEN = secrets_mgr.access_secret_version("SLACK_BOT_GPT3_TOKEN")
SLACK_APP_GPT3_TOKEN = secrets_mgr.access_secret_version("SLACK_APP_GPT3_TOKEN")

from openai_api_manager import OpenAIManager
oai = OpenAIManager(OPENAI_API_KEY, "text-davinci-003")

from app_logger import AppLogger
logger = AppLogger("slackbot_gpt_logger")

# Install the Slack app and get xoxb- token in advance from the OAuth & Permissions section of your app's config
# Bot tokens represent a bot associated with the app installed in a workspace. Unlike user tokens, they're not tied to a user's identity; they're just tied to your app.
app = App(token=SLACK_BOT_GPT3_TOKEN)

@app.event("app_mention")
def event_test(event, say):
	
	user_id = event["user"]

	completion = oai.create_completion(event["text"])
	completion_text = completion.choices[0].text

	text = f"<@{user_id}>!!! {completion_text}"

	logger.client.log_text(f"completion response: {text}")

	say(text)

if __name__ == "__main__":
	#App-level tokens represent your app across organizations, including installations by all individual users on all workspaces in a given organization.
	#App-level token strings begin with xapp-. We sometimes refer to them as "zap!" tokens.
    logger.client.log_text("Slackbot_ChatGPT3 app started")
    SocketModeHandler(app, SLACK_APP_GPT3_TOKEN).start()

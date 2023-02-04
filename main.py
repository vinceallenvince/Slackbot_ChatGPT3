import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from lib import create_completion


# Install the Slack app and get xoxb- token in advance from the OAuth & Permissions section of your app's config
# Bot tokens represent a bot associated with the app installed in a workspace. Unlike user tokens, they're not tied to a user's identity; they're just tied to your app.
app = App(token=os.environ["SLACK_BOT_GPT3_TOKEN"])

@app.event("app_mention")
def event_test(event, say):
	
	user_id = event["user"]

	completion = create_completion(event["text"])
	completion_text = completion.choices[0].text
	
	text = f"<@{user_id}>!! \n{completion_text}"

	say(text)

if __name__ == "__main__":
	#App-level tokens represent your app across organizations, including installations by all individual users on all workspaces in a given organization.
	#App-level token strings begin with xapp-. We sometimes refer to them as "zap!" tokens.
    SocketModeHandler(app, os.environ["SLACK_APP_GPT3_TOKEN"]).start()

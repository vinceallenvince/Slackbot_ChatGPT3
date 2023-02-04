# https://api.slack.com/apps/A04LZSPG7GA

import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from lib import create_completion


# Install the Slack app and get xoxb- token in advance from the Basic Information section of your app's config
# scope: conections:write
# description: Route your app’s interactions and event payloads over WebSockets
app = App(token=os.environ["SLACK_BOT_GPT3_TOKEN"])

@app.event("app_mention")
def event_test(event, say):
	
	user_id = event["user"]

	completion = create_completion(event["text"])
	completion_text = completion.choices[0].text

	text = f"<@{user_id}>! \n{completion_text}"

	say(text)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

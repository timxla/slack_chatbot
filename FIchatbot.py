import os
import re
import pyshorteners
from block_factory import keyword_block, datepicker_block
from query_object import Query
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN = 
SLACK_APP_TOKEN =

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)
shortener = pyshorteners.Shortener()
ask = Query()
data = ["", ""]

def parse_date(today):
    date_lst = today.split("-")
    month_map = ['x', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    date = ""

    date += (month_map[int(date_lst[1])] + " ")
    date += (date_lst[2] + ", ")
    date += (date_lst[0])

    return date 

def short_url(url):
    sh = shortener.tinyurl.short(url)
    return sh

def create_block(user_id, likes, image):
    block = {
            "type" : "section",
            "text" : {
                "type" : "plain_text",
                "text" : ("User Id : " + user_id) + "\n" + 
                ("Likes : " + str(likes)) + "\n" +
                ("Image URL : " + image)
            },
            "accessory" : {
                "type" : "image",
                "image_url" : image,
                "alt_text" : "image"
            }
        } 

    return block


def assemble_blocks(obj_list):
    block_list = []

    for obj in obj_list:
        uid = obj["insta_id"]
        lks = obj["likes"]
        img = short_url(obj["img_url"])
        block = create_block(uid, lks, img)
        block_list.append(block)

    return block_list


def make_payload():
    result = ask.query_by_class(data[0], parse_date(data[1]))
    if result == False: return "Could not match your query"
    payload = assemble_blocks(result)
    print(payload)
    return payload

@app.message("keywords")
def send_keywords(message, say):
    # say() sends a message to the channel where the event was triggered
    block = keyword_block()
    say(
        blocks=block,
        text=f"Hey there <@{message['user']}>!"
    )

@app.message("help")
def send_help_announcement(message, say):
    say(
        text="Type \"keywords\" for available keywords"
    )

@app.action(re.compile("^clicked_"))
def send_datepicker(ack, action, say):
    ack()
    print(action['value'])
    data[0] = (action['value'])
    datepicker = datepicker_block()
    say(
        blocks=datepicker,
        text="Choose a Date:"
    )

@app.action("click_date")
def work(ack, action, say):
    ack()
    print(action['selected_date'])
    data[1] = (action['selected_date'])
    say(
        text="Loading your query..."
    )

    payload = make_payload()
    print(payload)
    if (type(payload) == "str"):
        say(
            text=payload
        )
    else:
        say(
            blocks=payload,
            text="Result"
        )


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()


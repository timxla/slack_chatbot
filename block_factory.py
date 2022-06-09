keywords = [
    "blazer",
    "Half-shortpants",
    "blouse",
    "cardigan",
    "coat",
    "denim",
    "hoodi",
    "jumper",
    "leggings",
    "mustang",
    "onepiece",
    "pkshirts",
    "riders",
    "shirts",
    "skirt",
    "slacks",
    "sweater",
    "sweatpants",
    "sweatshirts",
    "t-shirts",
]

def keyword_block():
    block = [
        {
            "type": "actions",
            "elements": [
            ]
        }
    ]

    for i, text in enumerate(keywords):
        block[0]["elements"].append(
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": text,
                    "emoji": True
                },
                "value": text,
                "action_id": "clicked_" + text
            }
        )
    
    return block

def datepicker_block():
    datepicker = [
        {
            "type": "section",
            "block_id": "section1234",
            "text": {
                "type": "mrkdwn",
                "text": "Choose a date to query:"
            },
            "accessory": {
                "type": "datepicker",
                "action_id": "click_date",
                "initial_date": "2022-05-29",
                "placeholder": {
                "type": "plain_text",
                "text": "Select a date"
                }
            }
        }
    ]

    return datepicker




def query_result():
    pass
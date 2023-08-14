import json
import random
from function import *



def process(user_input):
    user_message = user_input
    def process_message(user_input):
        user_message = user_input

        with open("keyword.json") as file:
            keyword_actions = json.load(file)
        cleaned_input = user_message.replace(" ", "").lower()

        keyword_matched = False

        for keyword, action in keyword_actions.items():
            if keyword in cleaned_input:
                action_function = globals().get(action)
                if action_function:
                    response = action_function()
                else:
                    response = "Sorry, I didn't get it."
                keyword_matched = True
                break

        if not keyword_matched:
            response = fallback_response(user_message)

        return response

    def fallback_response(user_message):

        with open('intents.json') as file:
            intents = json.load(file)

        cleaned_input = user_message.replace(" ", "").lower()

        for intent in intents:
            patterns = intent.get("patterns", [])
            responses = intent.get("responses", [])
            for pattern in patterns:
                if pattern in cleaned_input:
                    return random.choice(responses)

        return "Sorry, I don't have an appropriate response for that."

    res = process_message(user_input)
    print(res)

    if res is not None:
        bot_response = "Bot: " + res
    else:
        bot_response = "Bot: Sorry, I didn't get it."

    print("respon giver",bot_response)

    return res

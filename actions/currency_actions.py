from rasa_sdk import Action
import requests
import json

class CustomAction(Action):
    def name(self):
        return "custom_action_currency"

    def run(self,dispatcher,tracker,domain):
        url = "http://data.fixer.io/api/latest?access_key=put your api key here with no spaces"
        response = requests.get(url)
        data = response.json()

        currency_data = {
            "base": data["base"],
            "date": data["date"],
            "rates": data["rates"]
        }

        formatted_data = json.dumps(currency_data, indent=4)

        dispatcher.utter_message(text="The latest currency rates are  :- ")
        dispatcher.utter_message(text="\n")
        dispatcher.utter_message(text=formatted_data)

        return []




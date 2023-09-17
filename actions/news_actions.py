from rasa_sdk import Action
import requests
import json

class CustomAction(Action):
    def name(self):
        return "custom_action_retrieve_news"

    def run(self,dispatcher,tracker,domain):
        url = ('https://newsapi.org/v2/top-headlines?'
               'country=us&'
               'apiKey=put your api key here with no spaces')

        response = requests.get(url)
        data = response.json()



        messages = []

        dispatcher.utter_message(text="The Top Headlines for you :- ")

        for i in data['articles']:
            title = i['title']
            url = i['url']
            dispatcher.utter_message(text=title)
            dispatcher.utter_message(text=url)
            dispatcher.utter_message(text="\n")


        return []



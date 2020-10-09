import os
import telegram
import json
import requests

class Sender():
    def __init__(self,token,chat_id=None):
        self.token = token
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id
    def send(self,text,chat_id=None):
        if chat_id!=None:
            self.chat_id = chat_id
        elif self.chat_id == None:
            print("please run get_chat_id method first")
            return
        if type(text) != str:
            text = json.dumps(text,indent=4)
        self.bot.send_message(chat_id=self.chat_id, text=text)

    def get_chat_id(self):
        r =requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
        try:
            fromi = json.loads(r.text)["result"][-1]["message"]["from"]
            id = fromi["id"]
            username = fromi["username"]
            self.chat_id = id
            return f"Set chat_id: {id} with this user {username}"
        except:
            print("please chat with your bot first")

if __name__ == "__main__":
    token = "mybrokentoken"
    sender = Sender(token)
    sender.get_chat_id()
    print(sender.send("test"))
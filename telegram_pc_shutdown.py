import requests
import json
import time
import os
token = "<Your_token_code_of_telegram>"
URL = "https://api.telegram.org/bot{}/".format(token)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf-8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL+"getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (chat_id, text)

def send_message(chat_id, text):
    url = URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    print(url)
    print("sending message")
    get_url(url)

def main():
    last = (None,None)
    while True:
        chat_id, text = get_last_chat_id_and_text(get_updates())
        if (chat_id, text) != last:
            if(text == "shutdown" or text == "Shutdown"):
                send_message(chat_id, "shutdown done")
                os.system("shutdown /s /t 1")
                last = (chat_id,text)
            else:
                send_message(chat_id, "PC is on")
                send_message(chat_id, "Enter the command")
                last = (chat_id,text)
    time.sleep(0.5)

if __name__ == "__main__":
    main()

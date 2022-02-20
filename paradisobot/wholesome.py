import requests
from itertools import filterfalse
from random import randint

def wholesome(tag):
    if tag == '' or tag == 'random':
        doujin = requests.get("https://wholesomelist.com/api/random").json()["entry"]
    else:
        try:
            data = requests.get("https://wholesomelist.com/api/list").json()["table"]
            tag_req = tag.lower().title() if not tag.lower() == 'milf' else 'MILF'
            doujin_list = [doujin for doujin in filterfalse(lambda x: tag_req not in x["tags"], data)]
            doujin = doujin_list[randint(0, len(doujin_list)-1)]
        except ValueError:
            return "Tag not found :("

    response = "Random Wholesome Hentai to brighten up your day: \n"
    response += "Wholesome Hentai #" + str(doujin["title"]) + "\n"
    response += doujin["title"] + " by " + doujin["author"] + "\n"
    response += "Parody: " + doujin["parody"] + "\n"
    response += "Tags: " + " ".join(doujin["tags"]) + "\n"
    response += "Link: " + doujin["link"]
    return response

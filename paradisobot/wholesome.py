import requests
import json

def wholesome():
	data = requests.get("https://wholesomelist.com/api/random").json()["entry"]
	response = "Random Wholesome Hentai to brighten up your day: \n"
	response += "Wholesome Hentai #" + str(data["id"]) + "\n"
	response += data["title"] + " by " + data["author"] + "\n"
	response += "Parody: " + data["parody"] + "\n"
	response += "Tags: " + " ".join(data["tags"]) + "\n"
	response += "Link: " + data["link"]
	return response

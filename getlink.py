"""
Orignally Written by Anandh Kumar
Github: https://github.com/anandh-kumar

He has allowed me to use his code.
"""
import random
import string
import scrapetube
import json
from datetime import date


def get_random_info(search_query: str, limit: int = 10000):
    print("trying")

    videos = scrapetube.get_search(search_query, limit=limit)
    video_id = []
    for video in videos:
        # print(video)
        channellink = video["ownerText"]["runs"][0]["navigationEndpoint"][
            "browseEndpoint"
        ]["canonicalBaseUrl"]
        channel = video["ownerText"]["runs"][0]["text"]
        videoId = video["videoId"]
        video_id.append([videoId, channel, channellink])
    if len(video_id) == 0:
        return False
    return random.choice(video_id)


def get_search_query():
    chars = string.ascii_letters
    search_query = ""
    search_query_len = random.randint(1, 25)

    for _ in range(search_query_len):
        search_query += random.choice(chars)

    return search_query


def write_json(new_data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(new_data, file, indent=4)


def main():

    data = get_random_info(get_search_query())
    while data == False:
        data = get_random_info(get_search_query())
    linkjson = {
        "videoID": data[0],
        "channelName": data[1],
        "channelId": data[2],
    }
    print(data)
    print(linkjson)
    write_json(linkjson, "ytrandlinks.json")
   


if __name__ == "__main__":
    main()

"""
Orignally Written by Anandh Kumar
Github: https://github.com/anandh-kumar

He has allowed me to use his code.
"""
import random
import string
import scrapetube


def get_random_link(search_query: str, limit: int = 100):
    videos = scrapetube.get_search(search_query, limit=limit)
    video_id = []
    for video in videos:
        video_id.append(video["videoId"])
    return f"https://www.youtube.com/watch?v={random.choice(video_id)}"


def get_search_query():
    chars = string.ascii_letters
    search_query = ""
    search_query_len = random.randint(1, 25)

    for _ in range(search_query_len):
        search_query += random.choice(chars)

    return search_query


def main():
    search_query = get_search_query()
    link = get_random_link(search_query)
    print(link)


if __name__ == "__main__":
    main()



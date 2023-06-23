import os, aiohttp
import re

async def get_gif_url(keywords):
    api_key = os.environ["api_key_meme"]  # Replace with your GIPHY API key
    endpoint = "https://api.giphy.com/v1/gifs/search"

    params = {
        "api_key": api_key,
        "q": keywords,
        "limit": 1,
        "rating": "g"  # You can change the rating if needed (e.g., "pg", "pg-13", "r")
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint, params=params) as response:
                data = await response.json()
                if response.status == 200:
                    gif_url = data["data"][0]["images"]["original"]["url"]
                    return gif_url
                else:
                    return None


    except Exception as e:
        print("Error:", e)

    return None


def find_gif_keywords(response: str):
    matches = re.findall(r"@(\[.*?])@", response)
    keywords = None
    if matches:
        keywords = matches[0]
        response = response.replace(f"@{keywords}@", "")

    return response, keywords


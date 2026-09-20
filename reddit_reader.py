import os
import time
import requests

CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
CLIENT_SECRET = os.environ["REDDIT_CLIENT_SECRET"]
USER_AGENT = os.environ["REDDIT_USER_AGENT"]

SUBREDDITS = [
    "wallstreetbets",
    "stocks",
    "investing",
    "StockMarket",
    "options",
]

MAX_POSTS_PER_SUBREDDIT = 6


def get_access_token():
    response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=(CLIENT_ID, CLIENT_SECRET),
        data={"grant_type": "client_credentials"},
        headers={"User-Agent": USER_AGENT},
        timeout=20,
    )
    response.raise_for_status()
    return response.json()["access_token"]


def get_recent_posts(subreddit, token):
    response = requests.get(
        f"https://oauth.reddit.com/r/{subreddit}/hot",
        params={
            "limit": MAX_POSTS_PER_SUBREDDIT,
            "raw_json": 1,
        },
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
        timeout=20,
    )
    response.raise_for_status()

    posts = []
    for item in response.json().get("data", {}).get("children", []):
        post = item.get("data", {})
        posts.append(
            {
                "title": post.get("title", ""),
                "permalink": post.get("permalink", ""),
                "created_utc": post.get("created_utc"),
                "score": post.get("score", 0),
                "num_comments": post.get("num_comments", 0),
            }
        )
    return posts


if __name__ == "__main__":
    token = get_access_token()

    for subreddit in SUBREDDITS:
        posts = get_recent_posts(subreddit, token)
        print(f"{subreddit}: {len(posts)} public posts retrieved")
        time.sleep(1)

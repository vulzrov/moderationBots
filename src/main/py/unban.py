from time import sleep, time
import praw
import json
import sys

# 给所有人解ban

def main(argv):
    with open("src/main/resource/clients.json", "r", encoding = "UTF-8") as f:
        data = json.load(f)
    reddit = praw.Reddit(**(data["bots"]["developerJinping"]))
    chonglanging = reddit.subreddit("chonglanging")
    
    for ban in chonglanging.banned():
        chonglanging.banned.remove(ban)

if __name__ == "__main__":
    main(sys.argv)
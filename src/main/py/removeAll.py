import json
import sys
import praw

# 清除历史发言

def main(argv):
    with open("src/main/resource/clients.json", "r", encoding = "UTF-8") as f:
        data = json.load(f)
    reddit = praw.Reddit(**(data["bots"]["developerJinping"]))
    bot = reddit.user.me()
    for comment in bot.comments.new():
        comment.delete()
    for submission in bot.submissions.new():
        submission.delete()         

if __name__ == "__main__":
    main(sys.argv)
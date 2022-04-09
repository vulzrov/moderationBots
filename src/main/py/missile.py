import random
from time import sleep
import praw
import json
import sys

# 追着大猪骂

from praw.models import *

def main(argv):
    with open("src/main/resource/clients.json", "r", encoding = "UTF-8") as f:
        data = json.load(f)
    reddit = praw.Reddit(**(data["bots"]["iws2000"]))
    replies = data["replies"]["iws2000"]
    replied = set()
    while (True):
        bigpig = reddit.redditor("HalleluYahmygod")
        
        for submission in bigpig.submissions.new(limit=10):
            if (submission.id not in replied):
                rply = submission.reply(random.choice(replies))
                replied.add(submission.id)
                print(rply.body)
                
        for comment in bigpig.comments.new(limit=10):
            if (comment.id not in replied):
                rply = comment.reply(random.choice(replies))
                replied.add(comment.id)
                print(rply.body)
        sleep(10)

if __name__ == "__main__":
    main(sys.argv)
import random
from time import sleep, time
import praw
import json
import sys

# ban掉所有vtuberv8活跃用户

from praw.models import *

def isV(contributor) -> bool:
    counter = 0
    for comment in contributor.comments.new(limit = 20):
        if (comment.subreddit.name == "t5_2ptvjk"):            
            counter += 1
        if (counter > 2):
            return True    
            
    for submission in contributor.submissions.new(limit = 20):
        if (submission.subreddit.name == "t5_2ptvjk"):
            return True
    return False

def fuckV(subreddit, path, whitelist, replies):
    jsonFile = open(path, 'r', encoding="UTF-8")
    
    data = json.load(jsonFile)
    checked = set(data["checked"])
    users = data["users"]
    for comment in subreddit.comments(limit = 10):
        try:
            if comment.id in checked:
                continue
        except:
            print("comment is empty")    
            continue
                
        author = comment.author        
        try:            
            if author.name in whitelist:
                checked.add(comment.id)
                continue
        except:
            print("author is Empty. Probably removed.")
            continue    
            
        print(f"{author.name}: {comment.body}")    
        now = int(time())
        if author.name in users.keys():
            permissionUntil = int(users[author.name]["permissionUntil"])
            if now < permissionUntil:
                checked.add(comment.id)
                continue
        try:    
            if isV(author):
                subreddit.banned.add(author.name, ban_reason = "被鉴定为V87了捏\U0001f917")
                comment.reply(random.choice(replies))
                print(f"{author.name}: 被鉴定为V87了捏\U0001f917")
            else :
                permissionUntil = now + 12 * 3600
                newPermitted = {
                    "name" : author.name,
                    "permissionUntil": permissionUntil
                }
                users[author.name] = newPermitted
            checked.add(comment.id)                
        except:
            print(f"exceptions occur when 查{author.name}成分")
            continue
    jsonFile.close()
    
    data["checked"] = [*checked, ]
    data["users"] = users
    jsonFile = open(path, "w", encoding="UTF-8")
    json.dump(data, jsonFile)
    jsonFile.close()
        
def main(argv):
    with open("clients.json", "r", encoding = "UTF-8") as f:
        data = json.load(f)
    reddit = praw.Reddit(**(data["bots"]["developerJinping"]))
    chonglanging = reddit.subreddit("chonglanging")   
    
    whitelist = set(data["whitelist"])
    replies = data["replies"]["developerJinping"]
    path = "visited.json"
    while True:
        fuckV(chonglanging, path, whitelist, replies)
        sleep(30)

if __name__ == "__main__":
    main(sys.argv)

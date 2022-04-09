import sys

# 将文件翻译为unicode

def main(argv):
    with open("src/main/resource/text", "r", encoding = "UTF-8") as f:
        data = ''
        for line in f:
            for word in line:
                data += word.encode('unicode-escape').decode('ASCII')
        print(data)        

if __name__ == "__main__":
    main(sys.argv)
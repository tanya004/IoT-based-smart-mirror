import xmltodict, json, requests

urlnews = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'

datanews = None

def __init__():
    global datanews
    resnews = requests.get(url=urlnews)
    datanews = xmltodict.parse(resnews.text)
    json.dumps(datanews)

    getData()
    #printData()


def getData():
    newsTitle = []
    newsUrl = []
    for i in datanews['rss']['channel']['item']:
        # newTitle
        a = i['title']
        newsTitle.append(a)

        # newUrl
        b = i['link']
        newsUrl.append(b)
    return (newsTitle, newsUrl)


def printData():
  
    for i in datanews['rss']['channel']['item']:
        print(i['title'])


# run
__init__()
printData()



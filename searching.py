import googleapiclient.discovery as gc
import pprint

def main():
    service = gc.build("customsearch", "v1", developerKey= "AIzaSyC3EeNpQWJKlNrsLWY2BeERN7lsCK55VyE")
    res = service.cse().list(q = 'Турбулентность',cx = '8fa0dc9f3a0a72baa').execute()
    links = []
    #pprint.pprint(res) Для красивого отображения запроса
    print()
    for i in range(len(res['items'])):
        links.append(res['items'][i]['formattedUrl'])
    print(links)

if __name__ == '__main__':
    main()
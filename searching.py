import googleapiclient.discovery as gc
import pprint

def main():
    question = input()
    service = gc.build("customsearch", "v1", developerKey= "AIzaSyC3EeNpQWJKlNrsLWY2BeERN7lsCK55VyE")
    res = service.cse().list(q = question,cx = '8fa0dc9f3a0a72baa').execute()
    links = []
    pprint.pprint(res) #Для красивого отображения запроса
    print()
    for iter in range(10):
        links.append([res['items'][iter]['title'], res['items'][iter]['link'],
                      res['items'][iter]['pagemap']['cse_image'][0]['src']
                      if 'cse_image' in res['items'][iter]['pagemap'].keys() else 'NULL'])
    print(links)

if __name__ == '__main__':
    main()
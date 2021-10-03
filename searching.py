import googleapiclient.discovery as gc
import pprint

def main():
    question = input()
    service = gc.build("customsearch", "v1", developerKey= "AIzaSyC3EeNpQWJKlNrsLWY2BeERN7lsCK55VyE")
    res = service.cse().list(q = question,cx = 'c124540bb98b00157').execute()
    res_img = service.cse().list(q = question,cx = '6a20fbd16a8e07d6b').execute()
    res_vid = service.cse().list(q = question,cx = '2f2e66f1278b4e365').execute()
    links = []
    vids = []
    pics = []
    pprint.pprint(res_vid) #Для красивого отображения запроса
    print()

    for iter in range(10):
        links.append([res['items'][iter]['title'], res['items'][iter]['link'],
                      res['items'][iter]['pagemap']['cse_image'][0]['src']
                      if 'cse_image' in res['items'][iter]['pagemap'].keys() else 'NULL'])
    print(links)
    print()
    for iter in range(10):
        vids.append([res_vid['items'][iter]['title'], res_vid['items'][iter]['link'],
                      res_vid['items'][iter]['pagemap']['cse_image'][0]['src']
                      if 'cse_image' in res_vid['items'][iter]['pagemap'].keys() else 'NULL'])
    print(vids)
    print()
    for iter in range(10):
        pics.append([res_img['items'][iter]['title'], res_img['items'][iter]['link'],
                      res_img['items'][iter]['pagemap']['cse_image'][0]['src']
                      if 'cse_image' in res_img['items'][iter]['pagemap'].keys() else 'NULL'])
    print(pics)
    print()

if __name__ == '__main__':
    main()
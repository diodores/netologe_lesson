import requests


TOKEN = '2619421814940190'
names = ['Hulk', 'Captain America', 'Thanos']

def determine_the_intelligence(names, token=TOKEN):
    list_intelligence = {}
    for name_h in names:
        url = f'https://superheroapi.com/api/{TOKEN}/search/{name_h}'
        res = requests.get(url)
        res = res.json()
        intelligence = res['results'][0]['powerstats']['intelligence']
        list_intelligence[name_h]=intelligence
    sort_by_intelligence = sorted(list_intelligence.items(), key=lambda item: item[0])
    return sort_by_intelligence


list_intelligence = determine_the_intelligence(names, TOKEN)
print(f'Наиболее сильный интеллект у {list_intelligence[-1]}, далее идет {list_intelligence[-2]}, замыкающий в этом сравнении {list_intelligence[-3]}')


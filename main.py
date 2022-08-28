import requests
import json
import csv
from datetime import datetime
p=0
for i in range(59,61):
    data_header={
        'x-api-key':'da2-7p2xir4ptjciroz6t6hkinq3va',
    }
    param={
            "query": "\n  query searchAdvisorByKeyword($keyword: String!, $start: Int) {\n    searchAdvisorByKeyword(keyword: $keyword, start: $start){\n      data {\n        id\n        avatarUrl\n        biography\n        displayName\n        image {\n          imageKey\n          originalImageKey\n        }\n        headline\n        industryTagIds\n        positionTagIds\n        publicProfileUrl\n        skillTagIds\n        title\n      }\n      found\n      start\n    }\n  }\n",
            "variables":{"keyword":"banking","start":(i*10)}
        }

    try:
        
        r=requests.post("https://umw4jygegjcxhhliq3d4iprapa.appsync-api.us-west-2.amazonaws.com/graphql",headers=data_header, json = param)
    except:
        print(i)
    
    cs=json.loads(r.text)
    
    for x in cs['data']['searchAdvisorByKeyword']['data']:
        p+=1
        row=[x['id'],x['displayName'],x['biography'],x['title'],'https://app.advisorycloud.com/profile/'+x['publicProfileUrl'],x['headline']]

        with open('output.csv', mode='a') as open_file:
            open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            open_writer.writerow(row)
    
    print('page:'+str(i)+' p='+str(p)+' time='+datetime.now().strftime("%H:%M:%S"))
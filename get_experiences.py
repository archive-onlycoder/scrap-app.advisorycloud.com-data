import requests
import json
import csv
from datetime import datetime
import time

data_header={
        'x-api-key':'da2-7p2xir4ptjciroz6t6hkinq3va',
    }


    
i=0

with open("company.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        i+=1
        a=row[4].split('/')[len(row[4].split('/'))-1]

        param={
            "query":"\n  query getAdvisor($advisorSlug: String!) {\n    getAdvisor(advisorSlug: $advisorSlug) {\n      avatarUrl\n      biography\n      biographyTruncated\n      boards {\n        appliedBoards {\n          id\n          companyName\n          companyLogo\n          slug\n        }\n        memberBoards {\n          id\n          companyName\n          companyLogo\n          slug\n        }\n      }\n      boardCompanies\n      searchableSkillLabels\n      searchableIndustryLabels\n      searchableIndustryTags\n      searchableSkillTags\n      displayName\n      id\n      image {\n        imageKey\n        originalImageKey\n      }\n      givenName\n      experiences {\n        position\n        startDate\n        endDate\n        company\n        iwmId\n        notes\n      }\n      headline\n      industryTagIds\n      positionTagIds\n      publicProfileUrl\n      skillTagIds\n      surName\n      title\n    }\n  }\n",
            "variables":{"advisorSlug":a}
        }
       
        try:
            r=requests.post("https://umw4jygegjcxhhliq3d4iprapa.appsync-api.us-west-2.amazonaws.com/graphql",headers=data_header, json = param)
        except:
            print(a)
        d=json.loads(r.text)
        exp=''
        try:
            for y in d['data']['getAdvisor']['experiences']:
                exp+=str(y['company'])+' - '+str(y['position'])+'('+str(y['startDate'])+'-'+str(y['endDate'])+") , "
        except:
            print(a)    
        row.append(exp)
        with open('output.csv', mode='a') as open_file:
            open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            open_writer.writerow(row)
        print(' p='+str(i)+' time='+datetime.now().strftime("%H:%M:%S"))
        # time.sleep(5)
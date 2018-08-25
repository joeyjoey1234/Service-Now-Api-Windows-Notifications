import requests
##URl of Instance with query of incident table and a filter of assigned to = empty
url = 'https://dev68698.service-now.com/api/now/table/incident?sysparm_query=assigned_toISEMPTY&sysparm_limit=100'
##login credds
user = 'admin'
pwd = 'Ycw8RO8osZbW'
##the headers for content type and accepted data in get request
headers = {"Content-Type":"application/json","Accept":"application/json"}
### the final request ## Response holds the response
response = requests.get(url, auth=(user, pwd), headers=headers  )
## Raw reqeust explainer
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
#the var filter
data = response.json()
data = '{}'.format(data)
data = data.split(',')
for x in data:
    print(x)



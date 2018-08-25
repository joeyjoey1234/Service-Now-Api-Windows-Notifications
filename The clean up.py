import requests

def incident_request():
    url = 'https://dev68698.service-now.com/api/now/table/incident?sysparm_query=assigned_toISEMPTY&sysparm_limit=100'
    user = 'admin'
    pwd = 'Ycw8RO8osZbW'
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers  )
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    data = response.json()
    return data




data = incident_request()
data = '{}'.format(data)
data = data.split(',')
for x in data:
    print(x)
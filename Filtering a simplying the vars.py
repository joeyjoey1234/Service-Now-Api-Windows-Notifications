import requests

def incident_request():
    url = 'https://dev68698.service-now.com/api/now/table/incident?sysparm_query=assigned_toISEMPTY&sysparm_limit=200'
    user = 'admin'
    pwd = 'Ycw8RO8osZbW'
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers  )
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    data = response.json()
    data = '{}'.format(data)
    data = data.split(',')
    return data
## test func was able to keep vars in side and also in a loop.
def print_vars():
    inc_vars = incident_request()
    for x in inc_vars:
        if 'number' in x:
            incident_number = x
            incident_number = incident_number.split(':')
            incident_number = incident_number[1]
            incident_number = incident_number.replace("'",'')
        elif 'sys_created_by' in x:
            created_by = x
            created_by = created_by.split(':')
            created_by = created_by[1]
            created_by = created_by.replace("'",'')
            print('Incident{} Is open and Unassigned by{}'.format(incident_number,created_by))
print_vars()
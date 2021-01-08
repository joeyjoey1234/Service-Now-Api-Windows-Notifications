import requests
import os
import time
import sys

### USER need the itil role and rest_api_explorer


user = input('Input your Service-Now Username: ')
pwd = input('Input your Service-Now Password: ')
user = str(user)
pwd = str(pwd)


def Start(x, y):
    Check_url = 'https://dev68698.service-now.com/api/now/table/incident?'
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(Check_url, auth=(x, y), headers=headers)
    if response.status_code != 200:
        # print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        # Request fail uncomment the top line to see debug info
        print('failed login')
        user2 = input('Input your Service-Now Username: ')
        pwd2 = input('Input your Service-Now Password: ')
        Start(user2, pwd2)
    else:
        inc_final_check(x, y)
#        call_final_check(x,y)
        pass


def incident_request(x, y):
    ###fix this query!!! i need active and empty group
    inc_url = 'https://dev68698.service-now.com/api/now/table/incident?sysparm_query=active=true^assignment_groupISEMPTY=truesysparm_limit=10'
    # user = 'admin'
    # pwd = 'Ycw8RO8osZbW'
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(inc_url, auth=(x, y), headers=headers)
    if response.status_code != 200:
        # print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        # Request fail uncomment the top line to see debug info
        print('check your login checker boiii')
        pass
    data = response.json()
    data = '{}'.format(data)
    data = data.split(',')
    return data


# def call_request(x,y):
#    inc_url = 'https://dev68698.service-now.com/api/now/table/new_call_list?sysparm_query=call_typeISEMPTY&sysparm_limit=100'
#    #user = 'admin'
#    #pwd = 'Ycw8RO8osZbW'
#    headers = {"Content-Type": "application/json", "Accept": "application/json"}
#    response = requests.get(inc_url, auth=(x, y), headers=headers)
#    if response.status_code != 200:
#        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
#        #Request fail uncomment the top line to see debug info
#        print('check your login checker boiii')
#        exit()
#    data = response.json()
#    data = '{}'.format(data)
#    data = data.split(',')
#    return data

# should work with large requests but will stop at one and open link
def print_open_inc(x, y):
    inc_vars = incident_request(x, y)
    # debug logs why are you here? 
    for x in inc_vars:
        if "{'result': []}" in x:
            return False
        elif 'number' in x:
            incident_number = x
            incident_number = incident_number.split(':')
            incident_number = incident_number[1]
            incident_number = incident_number.replace("'", '')
        elif 'sys_created_by' in x:
            created_by = x
            created_by = created_by.split(':')
            created_by = created_by[1]
            created_by = created_by.replace("'", '')
            print('Incident{} Is open and Unassigned by{}'.format(incident_number, created_by))
            # take off stop statement in case admins allow the custom notifications
            # also remove for a full query list filtered
            return True


# def print_open_call(x,y):
#    inc_vars = call_request(x,y)
#  
#    for x in inc_vars:
#        if "{'result': []}"in x:
#            return False
#        elif 'number' in x:
#            call_number = x
#            call_number = call_number.split(':')
#            call_number = call_number[1]
#            call_number = call_number.replace("'", '')
#            print('Call{} Is open and Unassigned'.format(call_number))
#            #take off stop statement in case admins allow the custom notifications
#            #also remove for a full query list filtered
#            taco = True
#            return taco


def inc_final_check(x, y):
    if print_open_inc(x, y) == True:
        os.system('start https://dev68698.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_query%3Dactive%253Dtrue%255Eassignment_groupISEMPTY%26sysparm_first_row%3D1%26sysparm_view%3D')
        time.sleep(60)
        inc_final_check(x, y)
    elif print_open_inc(x, y) == False:
        print('sleeping')
        time.sleep(60)
        inc_final_check(x, y)
    else:
        print('good connection but bad incident tables vars ')
        exit()


# def call_final_check(x,y):
#    if print_open_call(x,y) == True :
#        os.system('start https://dev68698.service-now.com/nav_to.do?uri=%2Fnew_call_list.do%3Fsysparm_userpref_module%3Dcc9b823d13ed5b00c73dbe322244b09d%26sysparm_query%3Dcall_type%3D%5EEQ%26sysparm_clear_stack%3Dtrue')
#        time.sleep(300)
#        call_final_check(x,y)
#    elif print_open_call(x,y) == False:
#        time.sleep(300)
#        call_final_check(x,y)
#    else:
#        print('good connection but bad call tables vars ')
#        exit()

Start(user,pwd)

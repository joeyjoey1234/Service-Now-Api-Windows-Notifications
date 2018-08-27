import requests
import os
import time

user = input('Input your Service-Now Username: ')
pwd = input('Input your Service-Now Password: ')
def Start(x,y):
    Check_url = 'https://dev68698.service-now.com/api/now/table/new_call_list?sysparm_query=call_typeISEMPTY&sysparm_limit=100'
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(Check_url, auth=(x,y), headers=headers)
    if response.status_code != 200:
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        #Request fail uncomment the top line to see debug info
        print('failed login')
        user = input('Input your Service-Now Username: ')
        pwd = input('Input your Service-Now Password: ')
        Start(user,pwd)
    else:
        call_final_check(x,y)
        pass




def call_request(x,y):
    inc_url = 'https://dev68698.service-now.com/api/now/table/new_call_list?sysparm_query=call_typeISEMPTY&sysparm_limit=100'
    ## These should be put in shellcode ? and hash check this script after aproval is good to go
    #user = 'admin'
    #pwd = 'Ycw8RO8osZbW'
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(inc_url, auth=(x, y), headers=headers)
    if response.status_code != 200:
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        #Request fail uncomment the top line to see debug info
        print('check your login checker boiii')
        exit()
    data = response.json()
    data = '{}'.format(data)
    data = data.split(',')
    return data


def print_open_call(x,y):
    inc_vars = call_request(x,y)
    #debug logs why are you here? ask joey pena Managed Services if your confused
    for x in inc_vars:
        if "{'result': []}"in x:
            return False
        elif 'number' in x:
            call_number = x
            call_number = call_number.split(':')
            call_number = call_number[1]
            call_number = call_number.replace("'", '')
            print('Call{} Is open and Unassigned'.format(call_number))
            #take off stop statement in case admins allow the custom notifications
            #also remove for a full query list filtered
            taco = True
            return taco

def call_final_check(x,y):
    if print_open_call(x,y) == True :
        os.system('start https://wwtms.service-now.com/nav_to.do?uri=%2Fnew_call_list.do%3Fsysparm_userpref_module%3Dcc9b823d13ed5b00c73dbe322244b09d%26sysparm_query%3Dcall_type%3D%5EEQ%26sysparm_clear_stack%3Dtrue')
    elif print_open_call(x,y) == False:
        time.sleep(300)
        call_final_check(x,y)
    else:
        print('good connection but bad tables vars')

Start(user,pwd)
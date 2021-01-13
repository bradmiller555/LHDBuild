import requests
import json

#for api help: https://www.dataquest.io/blog/python-api-tutorial/

response = requests.get('https://api.covidtracking.com/v1/states/current.json')
extracted_data = []
options = {'1':'state','2':'death','3':'positive'}

if(response.status_code == 200):    #make sure request was successful
    print('Success')
    
def extract_data(list_data):        #extracts needed data from JSON
    for state in f_response:
        name = ''
        deaths = 0
        positive = 0
        for key in state:
            if key == 'state':
                name = state[key]
            elif key == 'death':
                deaths = state[key]
            elif key == 'positive':
                positive = state[key]
        list_data.append({'state': name, 'death': deaths, 'positive': positive})

def sort_value():       #extracts the specified value
    values = []
    for state in extracted_data:
        for key in state:
            if key == choice_key:
                values.append(state[key])
    return values

def sort_data(values):      #sorts the values of the speified type from greatest to least
    for i in range(len(values)):
        next_val = values[i]
        j = i-1
        while j >= 0 and values[j] < next_val:
            values[j+1] = values[j]
            j-=1
        values[j+1] = next_val
    if choice_key == 'state':
        values.reverse()
    return values

def f_print(vals):      #prints all the data in terms of the sorted value
    print('{0:^7}{1:^10}{2:^10}'.format('State','Deaths','Cases'))
    for val in vals:
        for state in extracted_data:
            if state[choice_key] == val:
                print('{0:^7}{1:<10}{2:<10}'.format(state['state'],state['death'],state['positive']))

f_response = response.json()
extract_data(extracted_data)

choice = input('Enter a 1 to sort by state name, a 2 to sort by death count, and a 3 to sort by positive case count: ')
choice_key = options[choice]
print(choice_key)

vals = sort_value()
sorted_vals = sort_data(vals)
f_print(sorted_vals)



#below is function to print full formatted JSON string
"""
def jprint(obj):
    json_obj = json.dumps(obj, sort_keys=True, indent=4)
    print(json_obj)

jprint(f_response)
"""

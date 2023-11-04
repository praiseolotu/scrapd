# This script will be ran to convert the csv files to json format
'''
function: csv_to_json
params: csv_file_path, json_file_path
return: json_file
'''

import csv,json
 
def csv_to_json(csv_file_path, json_file_path):
    
    data_dict = {}
 
    with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
 
        
        for rows in csv_reader:
 
            key = rows['No']
            data_dict[key] = rows
 
    with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(data_dict, indent = 4))
 
csv_file_path = input('Enter the absolute path of the CSV file: ')
json_file_path = input('Enter the absolute path of the JSON file: ')
 
csv_to_json(csv_file_path, json_file_path)

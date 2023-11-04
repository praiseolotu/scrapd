import csv,json

# This script will be ran to convert the csv files to json format
'''
function: make_json
params: csvFilePath, jsonFilePath
return: json_file
'''


def make_json(csvFilePath, jsonFilePath):
	
	data = {}
	
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		for rows in csvReader:
			
			key = rows['Job_Name']
			data[key] = rows

	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
print('You are to choose your .json file name')
print('The csv file must correspond with the .csv file currently available.')
csvFilePath = input(r'CSV File Name:  ')

jsonFilePath = input(r'Json File Name:  ')
make_json(csvFilePath, jsonFilePath)

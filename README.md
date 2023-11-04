#### Scraper for Indeed.
_A python script that scraps jobs on [Indeed](https://ng.indeed.com) based on provided job name, location and number of pages to scrap_

#### Usage
_In as much as you can use pip the old fashion way, and the equivalent requirements.txt file is provided, it is advisable to use PIPENV._
_It is assumed PIPENV is globally enabled on your laptop_
##### Setting Up Pipenv
`pip install pipenv`
##### Setting Up Project
`git clone {url}` :clipboard:

`cd {folder}` :clipboard:

`pipenv shell` :clipboard:

`pipenv install` :clipboard:

`cd scrapJSON` :clipboard:

`python scrap.py` :clipboard:

_A .csv file will be generated at the base/root of the folder, an accompany csv to json script is provided._
##### Usage of csv to json converter
_You should be inside the scrapJSON directory_
`python test_csv.py` :clipboard:
_In the prompts that shows, you will provide the path name of the .csv file_
_You will also provide the name of the json file you want to create._

##### Features
- [x] Generate a .csv file after scrapping
- [x] Ability to convert csv file to json file

As you use this script, I hope you enjoy :blush: :blush: the experience. :fireworks:


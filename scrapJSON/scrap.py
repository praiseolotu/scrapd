import os,csv,requests
from bs4 import BeautifulSoup

headers = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

skill = input('Enter your skill: ').strip()
place = input('Enter choice location: ').strip()
no_of_pages = int(input('Enter the number of pages to scrap: '))


main_dir = os.getcwd() + '\\'
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    print('Base Directory Created Successfully.')

file_name = skill.title() + '_' + place.title() + '_Jobs.csv'
file_path = main_dir + file_name

with open(file_path, mode='w') as file:
    writer = csv.writer(file, delimiter=',', lineterminator='\n')
    writer.writerow(
        ['Job_Name', 'Company', 'Location', 'Posted', 'Apply_Link'])

    print(f'\nScraping in progress...\n')
    for page in range(no_of_pages):
        url = 'https://ng.indeed.com/jobs?q=' + skill + \
            '&l=' + place + '&start=' + str(page * 10)
        response = requests.get(url, headers=headers)
        html = response.text

        soup = BeautifulSoup(html, 'lxml')
        base_url = 'https://ng.indeed.com/viewjob?jk='
        d = soup.find('div', attrs={'id': 'mosaic-provider-jobcards'})

        jobs = soup.find_all('a', class_='tapItem')

        for job in jobs:
            job_id = job['id'].split('_')[-1]
            job_title = job.find('span', title=True).text.strip()
            company = job.find('span', class_='companyName').text.strip()
            location = job.find('div', class_='companyLocation').text.strip()
            posted = job.find('span', class_='date').text.strip()
            job_link = base_url + job_id
            writer.writerow(
                [job_title, company, location.title(), posted, job_link])

print(f'Jobs data written to <{file_name}> successfully.')

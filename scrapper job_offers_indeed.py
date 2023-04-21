import requests
from bs4 import BeautifulSoup
import csv

def get_job_links(url):
    """
    Function that scrapes job links from a website page.
    """
    links = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='search-results')
    job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

    for job_elem in job_elems:
        title_elem = job_elem.find('h2', class_='title')
        link_elem = title_elem.find('a', href=True)
        links.append('https://www.indeed.com' + link_elem['href'])

    return links

def get_job_details(url):
    """
    Function that scrapes job details from a job posting page.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_title = soup.find('h1', class_='jobsearch-JobInfoHeader-title').text.strip()
    company = soup.find('div', class_='jobsearch-InlineCompanyRating').find('span').text.strip()
    location = soup.find('div', class_='jobsearch-InlineCompanyRating').find_all('div')[1].text.strip()
    summary = soup.find('div', class_='jobsearch-JobComponent-description').text.strip()

    return [job_title, company, location, summary]

def write_to_csv(data):
    """
    Function that writes data to a CSV file.
    """
    with open('jobs.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

if __name__ == '__main__':
    url = 'https://www.indeed.com/jobs?q=python+developer&l=New+York%2C+NY&radius=25&start=0'
    links = get_job_links(url)

    for link in links:
        job_details = get_job_details(link)
        write_to_csv(job_details)
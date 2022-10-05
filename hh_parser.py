from bs4 import BeautifulSoup
import json, tqdm, time, requests as req
from urllib.parse import urlparse, urlunparse

list_data = []
data = {"data": list_data}

pages = 1
for page in range(pages):
    url = f'https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&page={page}'
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    title_links = soup.find_all(class_='serp-item__title')
    for title in tqdm.tqdm(title_links):
        time.sleep(5)
        addr = urlparse(title.attrs['href'])
        addr = addr._replace(query='')
        resp_job = req.get(urlunparse(addr))
        soup_job = BeautifulSoup(resp_job.text, 'lxml')
        tag_title = soup_job.find(attrs={'data-qa': "vacancy-title"}).get_text()
        tag_salary = soup_job.find(attrs={'data-qa': "vacancy-salary"}).get_text()
        tag_exp = soup_job.find(attrs={'data-qa': "vacancy-experience"}).get_text()
        tag_region = soup_job.find(attrs={'data-qa': "vacancy-view-raw-address"}).get_text()
        if not tag_region:
            tag_region = soup_job.find(attrs={'data-qa': "vacancy-view-location"}).get_text()
        list_data.append({'title': tag_title,
                          'work experience': tag_exp,
                          'salary': tag_salary,
                          'region': tag_region})
        with open('data.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)

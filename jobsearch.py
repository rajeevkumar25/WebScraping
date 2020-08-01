# requirement - this script scrapes Indeed.co.in for a particular job title and location and gives back resultset in pandas dataframe

import requests
from bs4 import BeautifulSoup as bs
import time
from pandas import DataFrame


class JobSearch():
    def __init__(self):
        self.indeed_main_url = 'https://www.indeed.co.in/'
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109'}
        # self.header='User-Agent': 'Mozilla/5.0'
        self.start = 0

    def getJobDetails(self, title, location):
        self.title = title
        self.location = location
        self.title = self.title.replace(' ', '+')
        self.start = 10
        page = 0
        job_details = []

        # search_url = self.indeed_main_url+self.title+'-jobs-in-'+self.location
        # print(search_url)
        while page <= self.start:
            try:

                search_url = self.indeed_main_url+'jobs?q='+self.title + \
                    '&l='+self.location+'&sort=relevance'+'&start='+str(page)
                print(search_url)
                site_res = requests.get(search_url, headers=self.header)

                if site_res.status_code == 200:
                    site_content = site_res.content
                    soup = bs(site_content, 'html.parser')
                    job_detail_card = soup.find_all(
                        'div', class_='jobsearch-SerpJobCard')

                    for detail in job_detail_card:
                        # print(detail.h2.a.text.strip())
                        title = detail.h2.a.text.strip()
                        job_link = detail.h2.a['href']
                        if '/rc/clk' in job_link:
                            job_link = job_link.replace(
                                '/rc/clk', 'https://www.indeed.co.in/viewjob')
                        if '/pagead/clk' in job_link:
                            job_link = job_link.replace(
                                '/pagead/clk', 'https://www.indeed.co.in/viewjob')
                        company = detail.find('span', class_='company')
                        company = company.text.strip()
                        # print(job_link)
                        short_summary = detail.find('div', class_='summary')
                        # print(short_summary)
                        short_summary = short_summary.ul.li.text
                        posted_day = detail.find('span', class_='date')
                        posted_day = posted_day.text.strip()
                        job_details.append(
                            [title, company, job_link, short_summary, posted_day])
                        # job_details.append(company)
                        # job_details.append(job_link)
                        # job_details.append(short_summary)
                        # job_details.append(posted_day)
                    # print(job_details)

                    # print(df)
                    time.sleep(3)
                    # break
                    page = page+10
            except Exception as ex:
                print(ex)
        return job_details


obj = JobSearch()
res = obj.getJobDetails('python developer', 'pune')
df = DataFrame(res, columns=[
    'Title', 'Company', 'Link', 'Summary', 'Posted On'])
print(df)

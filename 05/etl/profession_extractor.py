import time
import bs4
import requests # web lekérés
from pymongo import MongoClient
from typing import List, Dict
from bs4 import BeautifulSoup, Tag # html kezelés
from util.logger import LOG
from persist.mongodb import get_collection


BASE_URL = "http://www.profession.hu/allasok"

def fetch_profession_page(url:str) -> BeautifulSoup:
    r = requests.get(url)

    return BeautifulSoup(r.text, "html.parser")

def extract_job_card(page: BeautifulSoup) -> List[bs4.Tag]:
    job_cards = page.find("ul", {"class": "job-cards"}).find_all("li")

    return job_cards

def transform_job_card(job_card: Tag) -> Dict:
    job_advertisement_link = job_card.attrs["data-link"]
    job_prof_name = job_card.attrs["data-prof-name"]
    company = {
        "name": job_card.find("div", {"class": "card-body-header"})
            .find("div", {"class": "job-card__company-name"}).text.strip(),
        "address": job_card.find("div", {"class": "card-body-header"})
            .find("div", {"class": "job-card__company-address"}).text.strip()
    }
    job_description = {
        "description": job_card.find("div", {"class": "job-card__text"}).text.strip()
        if job_card.find("div", {"class": "job-card__text"}) != None else "",
        "tags": [tag.text.strip() for tag in job_card.find("div", {"class": "job-card__tags"}).find_all("span")]
    }

    return {
        "job_advertisement_url": job_advertisement_link,
        "prof_name": job_prof_name,
        "company": company,
        "job description": job_description
    }

def extract_next_url(page: BeautifulSoup) -> str:
    next_btn = page.find("a", {"class": "next"})
    return next_btn.attrs["href"] if next_btn != None else None

if __name__ == "__main__":
    DELAY = 2
    BATCH_SIZE = 10
    LOG.info("Extraction Process Started")
    url = BASE_URL
    data_lake = get_collection()
    iteration = 1

    while url != None:
        LOG.info(f"Fetch: {url}")
        html_doc = fetch_profession_page(url)
        job_cards = extract_job_card(html_doc)

        for job_card in job_cards:
            data_lake.insert(transform_job_card(job_card))

        LOG.info(url)
        url = extract_next_url(html_doc)
        iteration += 1
        LOG.info(url)
        if iteration % BATCH_SIZE == 0:
            time.sleep(DELAY)

    LOG.info("Extraction Process Finished")

import datetime
import math
import os
import re
from time import sleep
from typing import TypedDict

import pandas as pd
from furl import furl
from unicodedata import normalize
import requests
import urllib
from bs4 import BeautifulSoup

from base_classes import Car
from websites import *

from pprint import pprint


class CarSaleWebsiteParser:
    def __init__(self, url_with_page_num: str, website_list: list):
        self.start_datetime = datetime.datetime.now()
        self.start_datetime_string = self.start_datetime.strftime('%Y%m%d_%H%M%S')
        self.parser = 'html.parser'
        self.url = url_with_page_num
        self.page_num = 0
        self.retry_num = 2
        self.website_list = website_list
        self.website = self.define_website()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/114.0.0.0 Safari/537.36',
            'referer': self.website.referer,
        }
        self.pages_count = math.ceil(self.define_results_count() / self.website.listings_per_page)

    def define_website(self):
        for website in self.website_list:
            website_data = website()
            if self.url.startswith(website_data.web_address):
                return website_data

    def define_results_count(self):
        page = self.get_page(self.url)
        soup = BeautifulSoup(page, self.parser)
        results_count_data = self.find_text_by_attrs(soup, self.website.results_count_mask)
        results_count = re.findall(self.website.results_count_regex, results_count_data.replace(' ', ''))
        results_count_num = int(results_count[0])
        return results_count_num

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            html_text = response.text
            return html_text
        else:
            print(f'Page got response {response} which is incorrect response for parsing.\n'
                  f'Please check if page is availible.')

    def get_car_page_info(self, html_text):
        soup = BeautifulSoup(html_text, self.parser)
        res = self.find_all_by_attrs(soup, self.website.car.car_object_mask)
        cars_on_page = []
        for car in res:
            # print(car)
            name = self.find_text_by_attrs(car, attrs=self.website.car.name_mask)
            description = self.find_text_by_attrs(car, attrs=self.website.car.description_mask)
            tech_description = self.find_text_by_attrs(car, attrs=self.website.car.tech_description_mask)
            price = self.find_text_by_attrs(car, attrs=self.website.car.price_mask).replace(' ', '')
            place = self.find_text_by_attrs(car, attrs=self.website.car.place_mask)
            href = self.find_href_by_attrs(car, attrs=self.website.car.href_mask)
            parsed_car_info = dict(name=name, description=description, tech_description=tech_description,
                                   price=price, place=place, href=href)
            description_dict = self.website.parse_tech_description(parsed_car_info, description_parse_regex=self.website.car.description_parse_regex)
            car_item = Car(**{index: description_dict.get(index) for index in Car.__annotations__.keys()})
            cars_on_page.append(car_item)
        return cars_on_page

    def generate_next_page(self):
        url = furl(self.url)
        for i in range(1, self.pages_count + 3):
            self.page_num += 1
            url.args[self.website.page_arg] = self.page_num
            yield url.url, self.page_num

    @staticmethod
    def find_all_by_attrs(soup, attrs):
        data = soup.find_all(attrs=attrs)
        return data

    @staticmethod
    def find_text_by_attrs(soup, attrs):
        data = soup.find(attrs=attrs)
        if data:
            try:
                norm_data = normalize('NFKC', data.text)
            except Exception as e:
                print(e)
                norm_data = data.text
            return re.sub('\n|\t', '', norm_data)

    def find_href_by_attrs(self, soup, attrs):
        data = soup.find(attrs=attrs)
        if data:
            href = data.get('href')
            if href.startswith(self.website.web_address):
                return href
            else:
                return urllib.parse.urljoin(self.website.web_address, href)

    def get_car_info_by_filter(self):
        print(f'Getting results for {self.pages_count} pages at {self.url}')
        for page_url, page_num in self.generate_next_page():
            data_recieved = False
            retry_num = self.retry_num
            while not data_recieved:
                html_text = self.get_page(page_url)
                page_car_data = self.get_car_page_info(html_text)
                sleep(2)
                if page_car_data:
                    data_recieved = True
                    print(f'Data from page {page_num} {page_url} received')
                elif not page_car_data and retry_num == 0:
                    print(f'Data from page {page_num} {page_url} is not received, skipping... (Retries left {retry_num})')
                    break
                else:
                    print(f'Data from page {page_num} {page_url} is not received, retrying... (Retries left {retry_num})')
                    retry_num -= 1
            yield page_car_data

    def get_output_file_name(self):
        output_file_name = input('Please enter output_file_name (or skip):')
        if not output_file_name:
            output_file_name = self.website.short_name + '_' + self.start_datetime_string
            print(f'Resulting file name {output_file_name}.xlsx')
            return output_file_name
        else:
            return self.website.short_name + '_' + output_file_name

    def write_car_info(self):
        output_file_name = self.get_output_file_name()
        full_df = pd.DataFrame()
        for car_data in self.get_car_info_by_filter():
            dataframe = pd.DataFrame.from_dict(car_data)
            full_df = pd.concat([full_df, dataframe], axis=0)
        full_df.reset_index(inplace=True)
        full_df['price'] = pd.to_numeric(full_df['price'])
        full_df['year'] = pd.to_numeric(full_df['year'])
        full_df['mileage'] = pd.to_numeric(full_df['mileage'])
        resulting_file_path = os.path.join(os.getcwd(), 'out_files')
        os.makedirs(resulting_file_path, exist_ok=True)
        full_df.to_excel(os.path.join(resulting_file_path, output_file_name + '.xlsx'),
                         sheet_name=self.website.short_name)


if __name__ == '__main__':
    filtered_link = input('Input URL:\n')
    website_list_ = [OtomotoPl, AVBy, SuchenMobileDe, AutoScout24pl]
    pars = CarSaleWebsiteParser(filtered_link, website_list=website_list_)
    pars.write_car_info()

import re
from typing import TypedDict


class Car(TypedDict):
    name: str
    description: str
    tech_description: str
    year: str
    engine_description: str
    mileage: str
    fuel: str
    transmission: str
    price: str
    currency: str
    place: str
    href: str


class CarOnSaleWebsite:
    def __init__(self):
        self.car_object_mask = {'': ''}
        self.name_mask = {'': ''}
        self.description_mask = {'': ''}
        self.tech_description_mask = {'': ''}
        self.price_mask = {'': ''}
        self.place_mask = {'': ''}
        self.href_mask = {'': ''}
        self.description_parse_regex = {
            'description':
                {'year': {'search': r'', 'replace': r''},
                 'engine_volume': {'search': r'', 'replace': r''},
                 'mileage': {'search': r'', 'replace': r''},
                 'fuel': {'search': r'', 'replace': r''},
                 'transmission': {'search': r'', 'replace': r''}},
            'tech_description':
                {'year': {'search': r'', 'replace': r''},
                 'engine_volume': {'search': r'', 'replace': r''},
                 'mileage': {'search': r'', 'replace': r''},
                 'fuel': {'search': r'', 'replace': r''},
                 'transmission': {'search': r'', 'replace': r''}}
        }


class CarSaleWebsite:
    def __init__(self):
        self.web_address = None
        self.page_arg = None
        self.referer = self.web_address
        self.listings_per_page = 0
        self.results_count_mask = {'': ''}
        self.results_count_regex = r'[0-9]+'
        self.car = CarOnSaleWebsite()

    @staticmethod
    def parse_tech_description(description_dict: dict, description_parse_regex: dict):  # description: dict
        result = {}
        for description in description_parse_regex:
            tech_description_type = description_parse_regex[description]
            for index in tech_description_type:
                tech_description_type_mask = tech_description_type[index]
                if tech_description_type_mask['search']:
                    search = re.search(tech_description_type_mask['search'], description_dict[description])
                else:
                    search = description_dict[description]
                if search:
                    replace = re.sub(tech_description_type_mask['replace'], '',
                                     search if isinstance(search, str) else search.group())
                    if not result.get(index):
                        result[index] = replace
                else:
                    if not result.get(index):
                        result[index] = None
        print(result)
        return {**description_dict, **result}


if __name__ == '__main__':
    print(Car.__annotations__.keys())

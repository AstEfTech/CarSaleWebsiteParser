import re


class CarOnSaleWebsite:
    def __init__(self):
        self.car_object_mask = {'': ''}
        self.name_mask = {'': ''}
        self.description_mask = {'': ''}
        self.tech_description_mask = {'': ''}
        self.price_mask = {'': ''}
        self.place_mask = {'': ''}
        self.href_mask = {'': ''}
        self.tech_description_parse_regex = {'mileage': {'search': r'', 'replace': r''},
                                             'fuel': {'search': r'', 'replace': r''},
                                             'transmission': {'search': r'', 'replace': r''}}


class CarSaleWebsite:
    def __init__(self):
        self.web_address = None
        self.page_arg = None
        self.car = CarOnSaleWebsite()

    def parse_tech_description(self, tech_description: str):
        result = {}
        for index in self.car.tech_description_parse_regex:
            search = re.search(self.car.tech_description_parse_regex[index]['search'], tech_description)
            if search:
                replace = re.sub(self.car.tech_description_parse_regex[index]['replace'], '', search.group())
                result[index] = replace
        return result

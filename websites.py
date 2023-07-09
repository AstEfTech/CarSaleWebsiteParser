import re

from base_classes import CarSaleWebsite


class SuchenMobileDe(CarSaleWebsite):
    def __init__(self):
        super().__init__()
        self.web_address = 'https://suchen.mobile.de/'
        self.page_arg = 'pageNumber'
        self.referer = self.web_address
        self.listings_per_page = 25
        self.results_count_mask = {'data-testid': 'result-list-headline'}
        self.results_count_regex = r'[0-9]+'
        self.car.car_object_mask = {'class': 'cBox-body cBox-body--resultitem'}
        self.car.name_mask = {'class': 'g-col-8'}
        self.car.description_mask = {'class': 'vehicle-data--ad-with-price-rating-label'}
        self.car.tech_description_mask = {'data-testid': 'regMilPow'}
        self.car.price_mask = {'class': 'price-block u-margin-bottom-9'}
        self.car.place_mask = {'class': 'g-col-10'}
        self.car.href_mask = {'class': 'listing-item__link'}
        self.car.description_parse_regex = {'mileage': {'search': r'', 'replace': r''},
                                            'fuel': {'search': r'', 'replace': r''},
                                            'transmission': {'search': r'', 'replace': r''}}


class AVBy(CarSaleWebsite):
    def __init__(self):
        super().__init__()
        self.short_name = 'avby'
        self.web_address = 'https://cars.av.by/'
        self.page_arg = 'page'
        self.referer = self.web_address
        self.listings_per_page = 25
        self.results_count_mask = {'class': 'listing__header'}
        self.results_count_regex = r'[0-9]+'
        self.car.car_object_mask = {'class': 'listing-item'}
        self.car.name_mask = {'class': 'listing-item__link'}
        self.car.description_mask = {'class': 'listing-item__message'}
        self.car.tech_description_mask = {'class': 'listing-item__params'}
        self.car.price_mask = {'class': 'listing-item__priceusd'}
        self.car.place_mask = {'class': 'listing-item__location'}
        self.car.href_mask = {'class': 'listing-item__link'}
        self.car.description_parse_regex = {'mileage': {'search': r'', 'replace': r''},
                                            'fuel': {'search': r'', 'replace': r''},
                                            'transmission': {'search': r'', 'replace': r''}}


class OtomotoPl(CarSaleWebsite):
    def __init__(self):
        super().__init__()
        self.short_name = 'otomotopl'
        self.web_address = 'https://www.otomoto.pl/'
        self.page_arg = 'page'
        self.referer = self.web_address
        self.listings_per_page = 32
        self.results_count_mask = {'data-testid': 'results-heading'}
        self.results_count_regex = r'[0-9]+'
        self.car.car_object_mask = {'class': 'ooa-1t80gpj ev7e6t824'}
        self.car.name_mask = {'class': 'ev7e6t815 ooa-1xvnx1e er34gjf0'}
        self.car.description_mask = {'class': 'ev7e6t814 ooa-17thc3y er34gjf0'}
        self.car.tech_description_mask = {'class': 'ooa-13lipl2 ev7e6t87'}
        self.car.price_mask = {'class': 'ooa-1wb7q8u ev7e6t820'}
        self.car.place_mask = {'class': 'ooa-y2u8j5 ev7e6t83'}
        self.car.href_mask = {'rel': 'noreferrer'}
        self.car.description_parse_regex = {
            'name':
                {'year': {'search': r'[0-9]+  ', 'replace': r'\s|•'}},
            'price':
                {'price': {'search': None, 'replace': r'[A-Za-z]'},
                 'currency': {'search': None, 'replace': r'[0-9]'}},
            'description':
                {'year': {'search': r'[0-9]+  •', 'replace': r'\s|•'},
                 'engine_description': {'search': r'[0-9]+ [0-9]+ cm3', 'replace': r'\s|•'}, },
            'tech_description':
                {'mileage': {'search': r'[0-9]+ [0-9]+ km', 'replace': r'\s|km'},
                 'fuel': {'search': r'(\s([A-Za-z|+])+)Skrzynia', 'replace': r' paliwa|Skrzynia'},
                 'transmission': {'search': r'ó(([A-Za-z])+)', 'replace': r'w|ó|Kraj'}}
        }


class AutoScout24(CarSaleWebsite):
    def __init__(self):
        super().__init__()
        self.short_name = 'autoscout24'
        self.web_address = 'https://www.autoscout24.pl/'
        self.page_arg = 'page'
        self.referer = self.web_address
        self.listings_per_page = 20
        self.results_count_mask = {'class': 'ListHeader_top__jY34N'}
        self.results_count_regex = r'[0-9]+'
        self.car.car_object_mask = {'class': 'cldt-summary-full-item listing-impressions-tracking list-page-item '
                                             'false ListItem_article__ppamD'}
        self.car.name_mask = {'class': 'ListItem_title__znV2I ListItem_title_new_design__lYiAv Link_link__pjU1l'}
        self.car.description_mask = {'class': 'ListItem_subtitle__eY660'}
        self.car.tech_description_mask = {'class': 'VehicleDetailTable_container__mUUbY'}
        self.car.price_mask = {'data-testid': 'regular-price'}
        self.car.place_mask = {'class': 'SellerInfo_address__txoNV'}
        self.car.href_mask = {'class': 'ListItem_title__znV2I ListItem_title_new_design__lYiAv Link_link__pjU1l'}
        self.car.description_parse_regex = {
            'tech_description':
                {'mileage': {'search': r'[0-9]+ [0-9]+ km', 'replace': r'\s|km'},
                 'fuel': {'search': r'[A-Za-z|-]+[0-9]+ kW', 'replace': r'[0-9]|kW|\s'},
                 'transmission': {'search': r'[0-9]+ km[A-Za-z|ó|ł]+', 'replace': r'km|[0-9]'},
                 'engine_description': {'search': r'[0-9]+ KM', 'replace': r''},
                 'year': {'search': r'/[0-9]+[A-Z]', 'replace': r'/|[A-Z]'},
                 },
            'price': {'price': {'search': r'[0-9]+', 'replace': r''},
                      'currency': {'search': None, 'replace': r'[0-9]|,|-|}'}}
        }


if __name__ == '__main__':
    ws = AutoScout24()
    ws.parse_tech_description({'name': 'BMW 223 i xDrive Active Tourer M Sportpaket Head-Up', 'description': None,
                               'tech_description': '3 900 kmAutomatyczna03/2023Benzyna150 kW (204 KM)',
                               'price': '€51470,-', 'place': 'Harald Knieps • DE-53474 Bad Neuenahr-Ahrweiler',
                               'href': 'https://www.autoscout24.pl/oferta/bmw-223-i-xdrive-active-tourer-m-sportpaket'
                                       '-head-up-benzyna-bialy-bc9afcb4-6bfa-4e2d-92a0-d9fca28b6477'},
                              ws.car.description_parse_regex)
    ws.parse_tech_description(
        {'name': "BMW 223 i xDrive AHK PANO HuD DA+ PA+ 19' LMR LED DAB WLAN", 'description': None,
         'tech_description': '5 900 kmAutomatyczna04/2023Benzyna160 kW (218 KM)', 'price': '€50888,-',
         'place': 'Verkaufsteam Sprockhövel • DE-45549 Sprockhövel',
         'href': 'https://www.autoscout24.pl/oferta/bmw-223-i-xdrive-ahk-pano-hud-da-pa-19-lmr-led-dab-wlan-benzyna'
                 '-szary-6d39efd6-7b02-41c6-80ed-48170492e917'}
        , ws.car.description_parse_regex)
    ws.parse_tech_description({'name': 'BMW 223 i  M-Sport AHK H/K-HiFi DA+ PA+ HUD SHZ DAB', 'description': None,
                               'tech_description': '113 000 km- Skrzynia biegów07/2020Diesel87 kW (118 KM)',
                               'price': '€49990,-', 'place': 'DE-54634 Bitburg',
                               'href': 'https://www.autoscout24.pl/oferta/bmw-223-i-m-sport-ahk-h-k-hifi-da-pa-hud'
                                       '-shz-dab-elektryczno-benzynowy-zielony-7ed49326-aee7-4105-8842-5ea6f6549a1a'}
                              , ws.car.description_parse_regex)

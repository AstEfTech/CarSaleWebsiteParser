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
        self.car.car_object_mask = {'class': 'cBox-body cBox-body--resultitem'}
        self.car.name_mask = {'class': 'g-col-8'}
        self.car.description_mask = {'class': 'vehicle-data--ad-with-price-rating-label'}
        self.car.tech_description_mask = {'data-testid': 'regMilPow'}
        self.car.price_mask = {'class': 'price-block u-margin-bottom-9'}
        self.car.place_mask = {'class': 'g-col-10'}
        self.car.href_mask = {'class': 'listing-item__link'}
        self.tech_description_parse_regex = {'mileage': {'search': r'', 'replace': r''},
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
        self.car.car_object_mask = {'class': 'listing-item'}
        self.car.name_mask = {'class': 'listing-item__link'}
        self.car.description_mask = {'class': 'listing-item__message'}
        self.car.tech_description_mask = {'class': 'listing-item__params'}
        self.car.price_mask = {'class': 'listing-item__priceusd'}
        self.car.place_mask = {'class': 'listing-item__location'}
        self.car.href_mask = {'class': 'listing-item__link'}
        self.tech_description_parse_regex = {'mileage': {'search': r'', 'replace': r''},
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
        self.car.car_object_mask = {'class': 'ooa-1t80gpj ev7e6t824'}
        self.car.name_mask = {'class': 'ev7e6t815 ooa-1xvnx1e er34gjf0'}
        self.car.description_mask = {'class': 'ev7e6t814 ooa-17thc3y er34gjf0'}
        self.car.tech_description_mask = {'class': 'ooa-13lipl2 ev7e6t87'}
        self.car.price_mask = {'class': 'ooa-1wb7q8u ev7e6t820'}
        self.car.place_mask = {'class': 'ooa-y2u8j5 ev7e6t83'}
        self.car.href_mask = {'rel': 'noreferrer'}
        self.car.tech_description_parse_regex = {'mileage': {'search': r'[0-9]+ [0-9]+ km', 'replace': r'\s'},
                                                 'fuel': {'search': r'(\s([A-Za-z|+])+)Skrzynia',
                                                          'replace': r' paliwa|Skrzynia'},
                                                 'transmission': {'search': r'(([A-Za-z])+)Kraj', 'replace': r'w|Kraj'}}


class AutoScout24(CarSaleWebsite):
    def __init__(self):
        super().__init__()
        self.short_name = 'autoscout24'
        self.web_address = 'https://www.autoscout24.de/'
        self.page_arg = 'page'
        self.referer = self.web_address
        self.listings_per_page = 20
        self.results_count_mask = {'class': 'ListHeader_top__jY34N'}
        self.car.car_object_mask = {'class': 'cldt-summary-full-item listing-impressions-tracking list-page-item '
                                             'false ListItem_article__ppamD'}
        self.car.name_mask = {'class': 'ListItem_title__znV2I ListItem_title_new_design__lYiAv Link_link__pjU1l'}
        self.car.description_mask = {'class': 'ListItem_subtitle__eY660'}
        self.car.tech_description_mask = {'class': 'VehicleDetailTable_container__mUUbY'}
        self.car.price_mask = {'data-testid': 'regular-price'}
        self.car.place_mask = {'class': 'SellerInfo_address__txoNV'}
        self.car.href_mask = {'class': 'ListItem_title__znV2I ListItem_title_new_design__lYiAv Link_link__pjU1l'}
        self.tech_description_parse_regex = {'mileage': {'search': r'', 'replace': r''},
                                             'fuel': {'search': r'', 'replace': r''},
                                             'transmission': {'search': r'', 'replace': r''}}


if __name__ == '__main__':
    ws = OtomotoPl()
    ws.parse_tech_description('Przebieg180 000 kmRodzaj paliwaBenzynaSkrzynia biegówManualnaKraj pochodzeniaNiemcy')
    ws.parse_tech_description('Przebieg281 000 kmRodzaj paliwaBenzyna+LPGSkrzynia biegówManualna')

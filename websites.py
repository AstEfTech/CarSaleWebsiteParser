from base_classes import CarSaleWebsite


class SuchenMobileDe(CarSaleWebsite):
    def __init__(self):
        super().__init__()
        self.web_address = 'https://suchen.mobile.de/'
        self.page_arg = 'pageNumber'
        self.referer = self.web_address
        self.listings_per_page = 25
        self.car.car_object_mask = {'class': 'cBox-body cBox-body--resultitem'}
        self.car.name_mask = {'class': 'g-col-8'}
        self.car.description_mask = {'class': 'vehicle-data--ad-with-price-rating-label'}
        self.car.tech_description_mask = {'data-testid': 'regMilPow'}
        self.car.price_mask = {'class': 'price-block u-margin-bottom-9'}
        self.car.place_mask = {'class': 'g-col-10'}
        self.car.date_mask = {'class': 'listing-item__date'}
        self.car.href_mask = {'class': 'listing-item__link'}


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
        self.car.date_mask = {'class': 'listing-item__date'}
        self.car.href_mask = {'class': 'listing-item__link'}


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
        self.car.date_mask = {'class': 'ooa-y2u8j5 ev7e6t83'}
        self.car.href_mask = {'rel': 'noreferrer'}
        self.mileage = 'Przebieg'
        self.fuel = 'Rodzaj paliwa'
        self.transmission = 'Skrzynia biegów'

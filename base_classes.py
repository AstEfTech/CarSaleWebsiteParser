class CarOnSaleWebsite:
    def __init__(self):
        self.car_object_mask = None
        self.name_mask = None
        self.description_mask = None
        self.tech_description_mask = None
        self.price_mask = None
        self.place_mask = None
        self.date_mask = None
        self.href_mask = None


class CarSaleWebsite:
    def __init__(self):
        self.web_address = None
        self.page_arg = None
        self.car = CarOnSaleWebsite()


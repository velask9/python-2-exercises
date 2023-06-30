class CarCollector:
    car_list = [
        {"id": 1, "price": 10000},
        {"id": 2, "price": 20000},
        {"id": 3, "price": 30000},
    ]
    car_dict = {
        1: "Ford",
        2: "Mazda",
        3: "Chevy"
    }

    @staticmethod
    def get_data():
        return list(map(CarCollector._combine, CarCollector.car_list))

    @staticmethod
    # creating a private function
    def _combine(c):
        # Make has to be assigned to car dict
        # Has to be assigned for every id in the list.
        c['make'] = CarCollector.car_dict[c["id"]]
        return c


# print(CarCollector.get_data())
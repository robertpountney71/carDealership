from Vehicle import Vehicle

class Motorcycle(Vehicle):

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return the type of vehicle this is."""
        return 'motorcycle'
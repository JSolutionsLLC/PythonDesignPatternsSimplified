# Facade Pattern

# Subsystem Classes - Flights, Hotels, and Tours
class Flights:
    def get_flight_details(self, source, destination, date):
        return f"Flight booked from {source} to {destination} on {date}"


class Hotels:
    def get_hotel_details(self, location, check_in_date, check_out_date):
        return f"Hotel booked in {location} from {check_in_date} to {check_out_date}"


class Tours:
    def get_tour_details(self, location, date):
        return f"Tour booked in {location} on {date}"


# Facade - VacationPackage
class VacationPackage:
    def __init__(self):
        self.flights = Flights()
        self.hotels = Hotels()
        self.tours = Tours()

    def book_vacation(self, source, destination, date, hotel_location, check_in_date, check_out_date, tour_location, tour_date):
        flight_details = self.flights.get_flight_details(source, destination, date)
        hotel_details = self.hotels.get_hotel_details(hotel_location, check_in_date, check_out_date)
        tour_details = self.tours.get_tour_details(tour_location, tour_date)

        return f"Vacation Package Booked:\n{flight_details}\n{hotel_details}\n{tour_details}"


# Client Code
if __name__ == "__main__":
    vacation_package = VacationPackage()
    package_details = vacation_package.book_vacation("New York", "Paris", "2023-08-15", "Paris", "2023-08-16", "2023-08-20", "Eiffel Tower", "2023-08-17")

    print(package_details)

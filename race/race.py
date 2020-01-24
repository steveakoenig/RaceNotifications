
class Car:

    def __init__(self, driver, contact_number):
        self.driver = driver
        self.contact_number = contact_number

class Entry:

    def __init__(self, number, car):
        self.number = number
        self.car = car


class Race:

    #numbers as they are used in quarter midget races, to keep numbers single digit
    numbers = ['1','2','3','4','5','6','7','8','9','0','X','Y']

    def __init__(self, car_class, cars):
        self.car_class = car_class
        self.entries = []
        for i in range(len(cars)):
            car = Car(cars[i][0], cars[i][1])
            self.entries.append(Entry(self.numbers[i], car))

        self.state = 'ready'
        self.finishing_order = []

    def set_state(self, state):
        self.state = state

    def num_cars(self):
        return len(self.entries)

    def has_results(self):
        return len(self.finishing_order) > 0

    def add_results(self, finishing_order):
        self.finishing_order = finishing_order

    def get_contact_numbers(self):
        contact_numbers = []
        for entry in self.entries:
            contact_numbers.append(entry.car.contact_number)

        return contact_numbers

    def get_lineup(self):
        lineup = []
        for entry in self.entries:
            lineup.append('{0} ({1})'.format(entry.car.driver, entry.number))

        return '\n'.join(lineup)

    def print_lineup(self):
        print('{0} lineup ({1})'.format(self.car_class, self.state))
        print(self.get_lineup())

    def get_results_string(self):
        results = []
        position = 1
        for finish in self.finishing_order:
            entry = self.entries[self.numbers.index(finish)]
            if position == 1:
                position_string = '1st'
            elif position == 2:
                position_string = '2nd'
            else:
                position_string = str(position) + 'rd'

            results.append('{0}: {1} ({2})' \
                    .format(position_string, entry.car.driver, entry.number))
            position += 1;
        return '\n'.join(results)

    def print_results(self):
        if not self.has_results():
            print(self.car_class + ' no results yet')
            return

        print(self.car_class + ' results')
        print(self.get_results_string())


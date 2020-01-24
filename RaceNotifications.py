#!/usr/bin/python3

from race.race import Race
from race.client import SMSClient

import argparse
import sys

def create_races(filename):
    class_name = ''
    car_data_list = []
    races = []
    lineup_file = open(filename)

    for line in lineup_file:
        next_line = line.strip()
        elements = next_line.split(',')
        if len(elements) == 1:
            if len(elements[0]) > 0:
                class_name = elements[0]
            else:
                races.append(Race(class_name, car_data_list))
                car_data_list.clear()

        elif len(elements) == 2:
            car_data_list.append(elements)
        # else skip

    if len(car_data_list) > 0:
        races.append(Race(class_name, car_data_list))
        car_data_list.clear()

    return races


def get_input(message, options):
    selection = ''
    while selection not in options:
        selection = input('Select the race or [q]uit: ')
        selection = selection.lower()

    return selection



def select_race(races):
    print()
    options = []
    for i in range(len(races)):
        print('[{0}] {1} ({2})'.format(i, races[i].car_class, races[i].car_class ))
        options.append(str(i))

    print('[q] to quit')
    options.append('q')


    selection = get_input('Select the race or [q]uit: ', options)

    if selection == 'q':
        exit()

    return int(selection)



def select_action(race):
    print()
    race.print_lineup()
    options = ['h','s','r','q']
    print('[h] call cars to hot chute')
    print('[s] start race')
    print('[r] record results')
    print('[q] to quit')

    selection = get_input('Select the action or [q]uit: ', options)

    if selection == 'q':
        exit()

    return selection



def validate_results(race, results):
    if len(results) != race.num_cars():
        return False

    valid_numbers = race.numbers[0:race.num_cars()]
    for result in results:
        if result not in valid_numbers:
            return False

    return True



def get_results(race):
    results = []
    done = False
    while not done:
        race.print_lineup()
        results = input('enter results: ').split()
        done = validate_results(race, results)

    race.add_results(results)



def main():
    parser = argparse.ArgumentParser(description='Notifications for racers')
    parser.add_argument('filename')

    args = parser.parse_args()

    client = SMSClient()

    lineup_file = open(args.filename)


    races = create_races(args.filename)

    for next_race in races:
        next_race.print_lineup()

    while True:
        race_number = select_race(races)

        print ('selected race:')

        active_race = races[race_number]

        action = select_action(active_race)

        if action == 'h':
            active_race.set_state('hot chute')
            message_text = '{0}: cars to hot chute\n{1}'\
                    .format(active_race.car_class, active_race.get_lineup())
            client.send_sms(message_text, active_race.get_contact_numbers())

        elif action == 's':
            active_race.set_state('in progress')

        elif action == 'r':
            active_race.set_state('completed')
            get_results(active_race)
            active_race.print_results()
            message_text = '{0} completed, finish:\n{1}' \
                    .format(active_race.car_class, active_race.get_results_string())
            client.send_sms(message_text, active_race.get_contact_numbers())



# redirect stderr to suppress exception messaging
sys.stderr = object


main()



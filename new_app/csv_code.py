import csv
from os import environ
import os
from requests import get


def locate(key):
    with open('participant.csv', 'w') as f:
        f.write(get(environ["CSV_URL"]).text)
    participant_data = {}
    counter = 0
    fields = []
    with open('participant.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = -1

        for row in csv_reader:
            row_count += 1
            if row_count == 0:
                for field in row:
                    fields.append(field)
            else:
                if len(row) != 0:
                    if row[6] == str(key):
                        print("Participant found!\n")
                        for i in range(0, len(fields)):
                            participant_data[fields[i]] = row[i]
                        return participant_data
                    else:
                        counter += 1
        if counter == row_count:
            return 0

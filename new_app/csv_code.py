import codecs
import csv
from requests import get


def locate(filename: str, key, key_pos):
    response = get(f'https://csv.thescriptgroup.in/{filename}')
    participant_data = {}
    counter = 0
    fields = []
    csv_reader = csv.reader(codecs.iterdecode(response.iter_lines(), 'utf-8'), delimiter=',')
    row_count = -1

    for row in csv_reader:
        row_count += 1
        if row_count == 0:
            for field in row:
                fields.append(field)
        else:
            if len(row) != 0:
                if row[key_pos] == str(key):
                    # print("Participant found!\n")
                    for i in range(0, len(fields)):
                        if fields[i] == 'Name' or fields[i] == 'Credential Id':
                            participant_data[fields[i]] = row[i]
                    return participant_data
                else:
                    counter += 1
    if counter == row_count:
        return 0

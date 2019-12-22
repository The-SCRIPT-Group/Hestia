import csv


def locate(key):
    counter = 0
    fields = []
    with open('participant.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = -1

        for row in csv_reader:
            row_count+=1
            if(row_count == 0):
                for field in row:
                    fields.append(field)
            else:
                if row[3] == str(key):
                    print("Participant found!\n")
                    return row
                else:
                    counter+=1
        if counter == row_count:
            return 0

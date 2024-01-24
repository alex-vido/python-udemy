"""
Comma Separated Values - CSV
Is a data_dict format too much used for tables(Excel, Google Sheets), data_dict base, e-mail clients...
"""
import csv

with open('clients.csv', 'r') as file:
    # data_dict = csv.reader(file)
    data_dict = [x for x in csv.DictReader(file)]
    # next(data_dict)

# for data in data_dict:
#    print(data['Name'], data['Lastname'], data['E-mail'], data['Cel'])

with open('clients2.csv', 'w') as file:
    write = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    keys = data_dict[0].keys()
    keys = list(keys)
    write.writerow(
        [
            keys[0],
            keys[1],
            keys[2],
            keys[3]

            ]
        )


    for data in data_dict:
        write.writerow(
            [
                data['Name'],
                data['Lastname'],
                data['E-mail'],
                data['Cel']
            ]
        )

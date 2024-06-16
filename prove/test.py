import csv

def read_csv_as_dicts(filename):
    with open(filename, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return list(csv_reader)

csvOld = read_csv_as_dicts('dataOld.csv')
csv = read_csv_as_dicts('data.csv')

# Extract all IDs from both lists
ids_old = {row['ID'] for row in csvOld}
ids_new = {row['ID'] for row in csv}

# Filter items in csvOld that are not in csv
missing_items = [item for item in csvOld if item['ID'] not in ids_new]

# Filter items in csv that are not in csvOld
new_items = [item for item in csv if item['ID'] not in ids_old]

# Combine and print all different items
print("All different items:")
for item in missing_items + new_items:
    print(item)
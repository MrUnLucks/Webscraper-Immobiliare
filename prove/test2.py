array1 = [1, 2, 3, 4, 5]
array2 = [
    {"Id": 1, "name": "asd"},
    {"Id": 5, "name": "asd"},
    {"Id": 7, "name": "asd"},
    {"Id": 11, "name": "asd"},
]

filtered_array = list(filter(lambda el: el["Id"] in array1, array2))

print(filtered_array)
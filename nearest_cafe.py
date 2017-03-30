'''
Let's find the nearest cafe by given coordinates
'''
import csv


# Read the file with cafes info
cafes = {}

with open ("cafes.csv", "r", encoding = 'utf-8') as file:
    fields = ['Name', 'Address', 'Coordinates', 'Description']
    reader = csv.DictReader(file, fields, delimiter=';')

    #TODO - сделать, чтобы не читался header

    for row in reader:
        cafes[row['Coordinates']] = [row['Name'], row['Address'], row['Description']]

print(cafes)


# TODO: Find the nearest cafe
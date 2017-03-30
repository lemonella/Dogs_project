'''
Let's find the nearest cafe by given coordinates
'''
import csv
import math

# Getting the longitude and latitude from the user
lat_point = input("Введите широту: ")
lng_point = input("Введите долготу: ")
# lat_point = 37.230884
# lng_point = 56.036111

try:
    lat_point = float(lat_point)
    lng_point = float(lng_point)
except ValueError:
    print("Введены некорректные данные")
    exit()

def find_distance_by_coordintes (lat1,lng1,lat2,lng2):
    '''
    function finds the distance between 2 points by coordinates
    '''
    # Convert degrees to radians. 
    lat1 = math.radians(lat1)
    lng1 = math.radians(lng1)
    lat2 = math.radians(lat2)
    lng2 = math.radians(lng2)
 
    # Calculate delta longitude and latitude. 
    delta_lat = (lat2 - lat1)
    delta_lng = (lng2 - lng1)
 
    return round(6378137 * math.acos(math.cos(lat1) * math.cos(lat2) * math.cos(lng2 - lng1) + math.sin(lat1) * math.sin(lat2)))

# Read the file with cafes info
cafes = {}
nearest_cafe = {'Distance':0, 'Name':'', 'Address':''}

with open ("cafes.csv", "r", encoding = 'utf-8') as file:
    fields = ['Name', 'Address', 'Coordinates', 'Description']
    reader = csv.DictReader(file, fields, delimiter=';')

    #grab cafe data from file to dictionary
    i = 0
    for row in reader:
        if row['Name'] == '':
            break
        if i == 0:
            i += 1
            continue

        i += 1
        coordinates = row['Coordinates'].split(',')
        lat = float(coordinates[0])
        lng = float(coordinates[1])

        cafes[i] = {
            'Name': row['Name'], 
            'Address': row['Address'], 
            'Description': row['Description'], 
            'latitude': lat, 
            'longitude': lng
        }

        # Getting the distance to the current cafe
        cafes[i]['Distance'] = find_distance_by_coordintes (lat_point, lng_point, lat, lng)
        
        # If this cafe is the nearest let's write it to nearest_cafe var
        if (nearest_cafe['Distance'] == 0) or  (cafes[i]['Distance'] < nearest_cafe['Distance']):
            nearest_cafe = {'Distance':cafes[i]['Distance'], 'Name':cafes[i]['Name'], 'Address':cafes[i]['Address']}

# Printing the nearest cafe
print('Ближайшее кафе: ' + str(nearest_cafe))



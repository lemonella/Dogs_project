'''
Let's find the nearest cafe by given coordinates
'''
import csv
import math

def get_coordinates_from_user():
    # Getting the longitude and latitude from the user
    # lat_point = input("Введите широту: ")
    # lng_point = input("Введите долготу: ")
    lat_point = 37.230884
    lng_point = 56.036111

    try:
        lat_point = float(lat_point)
        lng_point = float(lng_point)
    except ValueError:
        print("Введены некорректные данные")
        exit()

    return lat_point, lng_point


def find_distance_by_coordinates (lat1, lng1, lat2, lng2):
    '''
    function finds the distance between 2 points by coordinates
    '''

    try:
        lat1 = float(lat1)
        lng1 = float(lng1)
        lat2 = float(lat2)
        lng2 = float(lng2)
    except ValueError:
        print("Введены некорректные данные")
        return False

    # Convert degrees to radians. 
    lat1 = math.radians(lat1)
    lng1 = math.radians(lng1)
    lat2 = math.radians(lat2)
    lng2 = math.radians(lng2)
 
    # Calculate delta longitude and latitude. 
    delta_lat = (lat2 - lat1)
    delta_lng = (lng2 - lng1)
 
    return round(6378137 * math.acos(math.cos(lat1) * math.cos(lat2) * math.cos(lng2 - lng1) + math.sin(lat1) * math.sin(lat2)))


def find_nearest_cafe(cafes_raw, lat_user, lng_user):
    try:
        lat_user = float(lat_user)
        lng_user = float(lng_user)
    except ValueError:
        print('Введены некорректные данные')
        return False


    nearest_cafe = {'Distance':0, 'Name':'', 'Address':''}

    for row in cafes_raw:
        # coordinates = row['Coordinates'].split(',')
        lat_raw = float(row['Lat'])
        lng_raw = float(row['Lng'])

        distance = find_distance_by_coordinates (lat_user, lng_user, lat_raw, lng_raw)

        if not distance:
            return False
    
        # If this cafe is the nearest let's write it to nearest_cafe var
        if (nearest_cafe['Distance'] == 0) or  (distance < nearest_cafe['Distance']):
            nearest_cafe = {'Distance': distance, 'Name':row['Name'], 'Address':row['Address']}

        return nearest_cafe


def get_cafes_from_file(filepath):
    # Read the file with cafes info
    cafes_raw = list()
    with open (filepath, "r", encoding = 'utf-8') as file:
        fields = ['Name', 'Address', 'Lat', 'Lng', 'Description']
        reader = csv.DictReader(file, fields, delimiter=',')
        cafes_raw = list(reader)
        return cafes_raw

if __name__ == "__main__":
    user_lat, user_lng = get_coordinates_from_user()
    cafes_raw = get_cafes_from_file('csv/placelist.csv')
    nearest_cafe = find_nearest_cafe(cafes_raw, user_lat, user_lng)

    # Printing the nearest cafe
    print('Ближайшее кафе: ' + str(nearest_cafe))
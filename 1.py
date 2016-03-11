import getopt
import googlemaps
import json
import csv
import os
import sys

gmaps = googlemaps.Client(key='AIzaSyDXcQ99Del7RZudfT9A6fMyhxjMzqtBEkw')

LOCATION = {'lat': 41.0, 'lng': -74.0}
RADIUS = '2000'
QUERY = 'ice cream'


# Prepare output file to write
output_file = open(QUERY + '.csv', 'w')
result_file = csv.writer(output_file)
result_file.writerow(['name', 'address', 'place_id', 'id', 'URL',
                      'rating', 'lat', 'lng', 'phone', 'photos', 'types'])


# Get one page with places
def get_places(query=None, location=None, radius=None, page_token=None):
    # places = gmaps.places(query=QUERY, location=LOCATION, radius=RADIUS, page_token=page_token)
    print 'Searching ' + query, 'in: ' + location
    places = gmaps.places(query=query, location=location, radius=radius, page_token=page_token)
    # obj = json.dumps(places, indent=4)
    # print obj

    for result in places["results"]:
        get_place_details(result["place_id"])

    try:
        next_page = places["next_page_token"]
        get_places(query=query, location=location, radius=radius, page_token=next_page)
    except KeyError:
        pass


def get_place_details(place_id):
    details = gmaps.place(place_id)
    result = details["result"]

    print 'Getting the: ', result["name"].encode('utf-8')

    # obj = json.dumps(result, indent=4)
    # print obj

    photo_names = []
    try:
        photos = result["photos"]
        for index, photo in enumerate(photos):
            photo_reference = photo["photo_reference"]
            photo_name = get_place_photo(result["place_id"], index, photo_reference)
            photo_names.append(photo_name)
    except KeyError:
        pass

    try:
        name = result["name"].encode('utf-8')
    except KeyError:
        name = ''

    try:
        formatted_address = result["formatted_address"].encode('utf-8')
    except KeyError:
        formatted_address = ''

    try:
        place_id = result["place_id"].encode('utf-8')
    except KeyError:
        place_id = ''

    try:
        id = result["id"].encode('utf-8')
    except KeyError:
        id = ''

    try:
        url = result["url"].encode('utf-8')
    except KeyError:
        url = ''

    try:
        rating = str(result["rating"])
    except KeyError:
        rating = ''

    try:
        lat = str(result["geometry"]["location"]["lat"])
    except KeyError:
        lat = ''

    try:
        lng = str(result["geometry"]["location"]["lng"])
    except KeyError:
        lng = ''

    try:
        types = ','.join(result["types"])
    except KeyError:
        types = ''

    try:
        international_phone_number = result["international_phone_number"].encode('utf-8')
    except KeyError:
        international_phone_number = ''

    result_file.writerow([name, formatted_address, place_id,
                          id, url, rating,
                          lat, lng,
                          international_phone_number,
                          ','.join(photo_names),
                          types
                          ])


def get_place_photo(place_id, index, photo_reference):
    if not os.path.exists(os.path.join('images', place_id)):
        os.makedirs(os.path.join('images', place_id))
    photo_path = os.path.join('images', str(place_id), str(index) + '.jpg')
    f = open(photo_path, 'wb')
    for chunk in gmaps.places_photo(photo_reference, max_width=1000):
        if chunk:
            f.write(chunk)
    f.close()
    return photo_path


if __name__ == '__main__':
    argv = sys.argv[1:]
    query = None
    location = None
    radius = None
    try:
        opts, args = getopt.getopt(argv, "hq:l:r:", ["query=", "location=", "radius="])
    except getopt.GetoptError:
        print 'Usage: ' + sys.argv[0] + ' -q <query> -l <location> -r <radius>'
        sys.exit(2)

    if len(opts) < 1:
        print 'Please enter a query and location where to search'
        print 'Usage: ' + sys.argv[0] + ' -q <query> -l <location> -r <radius>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'Usage: ' + sys.argv[0] + ' -q <query> -l <location> -r <radius>'
            sys.exit()
        elif opt in ("-q", "--query"):
            query = arg
        elif opt in ("-l", "--location"):
            location = arg
        elif opt in ("-r", "--radius"):
            radius = arg

    print 'Start working'
    get_places(query=query, location=location, radius=radius)
    output_file.close()
    print 'All done'

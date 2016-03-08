import googlemaps
import json
import csv

gmaps = googlemaps.Client(key='AIzaSyDXcQ99Del7RZudfT9A6fMyhxjMzqtBEkw')


places = gmaps.places(query='ice cream')

details = gmaps.place('ChIJKzuuWxK1RIYRbL2S4MBsY98')
# photo = gmaps.photo('CmRdAAAA6mSDKYe6uwjFgHE4Npf8fFfwkp_VwBfEQta3-QGG0XVgzPdfwDFzpPLDCFShePrJBuiMv2bT_cbpvRtV5XIf27fr9-FTyoClmluwcI_oxKJpzyYKTdfX1kaUDeUK79kNEhA0H2Mn884LLiU3IAuTeStqGhT3pYhpmNPv__ywv0d_F5JnIHP5Gg')
# f = open('photo.png', 'wb')
# for chunk in gmaps.places_photo('CmRdAAAA6mSDKYe6uwjFgHE4Npf8fFfwkp_VwBfEQta3-QGG0XVgzPdfwDFzpPLDCFShePrJBuiMv2bT_cbpvRtV5XIf27fr9-FTyoClmluwcI_oxKJpzyYKTdfX1kaUDeUK79kNEhA0H2Mn884LLiU3IAuTeStqGhT3pYhpmNPv__ywv0d_F5JnIHP5Gg', max_width=1000):
#     if chunk:
#         f.write(chunk)
# f.close()

obj = json.dumps(details, indent=4)

print obj
# print places["next_page_token"]


# result_file = csv.writer(open('result.csv', 'w'))
# result_file.writerow(['rating', 'name', 'reference', 'location', 'opening', 'Bezugsfrei_ab',
#                                   'Zimmer', 'Haustiere', 'Kaltmiete', 'Nebenkosten', 'Heizkosten', 'Gesamtmiete',
#                                   'Kaution_o_genossenschaftsanteile', 'URL'])

def get_places(query=None, location=None, radius=None, page_token=None):

    places = gmaps.places(query=query, location=None, radius=None, page_token=page_token)
    for result in places["results"]:
        get_place_details(result["place_id"])

        photo = result["photos"][0]
        photo_reference = photo["photo_reference"]
        get_place_photo(result["place_id"], photo_reference)
    if places["next_page_token"]:
        get_places(query='ice cream', location=None, radius=None, page_token=places["next_page_token"])


def get_place_details(place_id):
    details = gmaps.place(place_id)


def get_place_photo(place_id, photo_reference):

    f = open(place_id+'.jpg', 'wb')
    for chunk in gmaps.places_photo(photo_reference, max_width=1000):
        if chunk:
            f.write(chunk)
    f.close()


# if places["next_page_token"]:
#     places = gmaps.places(query='ice cream', location=None, radius=None, page_token=places["next_page_token"])

from itertools import combinations
import geopy.distance
import googlemaps
from operator import itemgetter
from dotenv import load_dotenv
import os

load_dotenv()
gmaps = googlemaps.Client(key=os.getenv("APIKEY"))


def get_geocodes(listdata):
    results = []
    for i in listdata.adresses:
        geocode_result = gmaps.geocode(i.address)
        for u in geocode_result:
            results.append(
                {
                    'address': i,
                    'coord': {
                        'latitude': u['geometry']['location']['lat'],
                        'longitude': u['geometry']['location']['lng'],
                    }

                }
            )
    return results


def get_distances(listdata):
    comb = combinations(listdata, 2)
    result = []
    for i in comb:
        pina = i[0]['address'].address
        pinb = i[1]['address'].address
        distance = geopy.distance.geodesic(
            (i[0]['coord'].get('latitude'),i[0]['coord'].get('longitude')) ,
            (i[1]['coord'].get('latitude'),i[1]['coord'].get('longitude'))
        ).meters
        result.append({
            'pinA': pina,
            'pinB': pinb,
            'distance': int(distance),
        })
    result = sorted(result, key=itemgetter('distance'), reverse=True)
    result = {
        'distances': result
        }

    return result


def set_nearest_farest(listdata):
    listdata.update(
        {
            'nearest': [
                list['distances'][-1]
            ],
            'farest': [
                list['distances'][0]
            ]
        }
    )
    return listdata



#!/usr/bin/env python3

import os, gzip
from csv import DictReader

class Airport(object):
    __slots__ = ['name', 'type', 'latitude', 'longitude', 'elevation', 'continent', 'country', 'iata', 'icao']
    def __init__(self, name, type, latitude, longitude, elevation, continent, country, iata, icao):
        self.name = name
        self.type = type
        # location data
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.continent = continent
        self.country = country
        # coding
        self.iata = iata
        self.icao = icao
    def __eq__(self, other):
        if not isinstance(other, Airport):
            return False
        return True
    def __hash__(self):
        return self.iata

class OurAirports:

    def __init__(self):
        self.data = []
        self.dir = os.path.dirname(os.path.realpath(__file__))
        with gzip.open('{}/data/airports.csv.gz'.format(self.dir), mode='rt') as f:
            reader = DictReader(f)
            for row in reader:
                self.data.append(
                    Airport(
                        row['name'],
                        row['type'],
                        row['latitude_deg'],
                        row['longitude_deg'],
                        row['elevation_ft'],
                        row['continent'],
                        row['iso_country'],
                        row['iata_code'],
                        row['gps_code']
                    )
                )

    def getAirportsByType(self, type):
        if not type in ["closed_airport", "heliport", "large_airport", "medium_airport", "seaplane_base", "small_airport"]:
            return []
        return [x for x in self.data if x.type == type]

    def getAirportsByICAO(self, icao):
        return [x for x in self.data if x.icao == icao]

    def getAirportsByIATA(self, iata):
        return [x for x in self.data if x.iata == iata]
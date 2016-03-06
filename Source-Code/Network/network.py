# ==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Network objects
# @author: Elisha Lai
# @version: 1.2 16/04/2015
# ==============================================================================

import networkx
import sqlite3


class Network:
    # Initializes the object.
    def __init__(self):
        self.__network = networkx.Graph()
        self.__add_stations()
        self.__add_station_zone_assignments()
        self.__add_connections()

    # Adds stations to the network from the database.
    def __add_stations(self):
        connection = sqlite3.connect("easy_ticket.db")
        cursor = connection.cursor()
        select_from_station_table_string = "SELECT S.name FROM station S"
        cursor.execute(select_from_station_table_string)
        result_set = cursor.fetchall()
        for result in result_set:
            self.__network.add_node(result[0], zones=set())
        cursor.close()
        connection.close()

    def __add_station_zone_assignments(self):
        connection = sqlite3.connect("easy_ticket.db")
        cursor = connection.cursor()
        select_from_station_zone_assignment_table_string = "SELECT S.name, Z.id FROM station_zone_assignment SZA, station S, zone Z WHERE SZA.station = S.id AND SZA.zone = Z.id"
        cursor.execute(select_from_station_zone_assignment_table_string)
        result_set = cursor.fetchall()
        for result in result_set:
            station_name = result[0]
            station_zone = result[1]
            self.__network.node[station_name]["zones"].add(station_zone)
        cursor.close()
        connection.close()

    # Adds connections to the network from the database.
    def __add_connections(self):
        connection = sqlite3.connect("easy_ticket.db")
        cursor = connection.cursor()
        select_from_connection_table_string = "SELECT S1.name, S2.name, C.distance FROM station S1, station S2, connection C WHERE station_a = S1.id AND station_b = S2.id"
        cursor.execute(select_from_connection_table_string)
        result_set = cursor.fetchall()
        for result in result_set:
            self.__network.add_edge(result[0], result[1], weight=result[2])
        cursor.close()
        connection.close()

    # Returns the shortest route from origin station to destination station.
    def get_shortest_route(self, origin_station, destination_station):
        return networkx.dijkstra_path(self.__network, origin_station, destination_station)

    # Returns the set of zones visited by the route taken in the network.
    def get_zones_visited(self, route):
        zones_visited = set()


    # Returns a set of zones visited by the path taken in the
    # network. 
    def get_zones_visited(self, path):
        isinstance(self, Network)
        zones_visited = set()
        # Extracts the zone where each station in the path is located.
        for station in path:
            station_zones = self.__network[station][0].get_zones()
            for zone in station_zones:
                zones_visited.add(zone)
        return zones_visited

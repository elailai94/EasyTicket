# =============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Network objects
# @author: Elisha Lai
# @version: 1.2 16/04/2015
# =============================================================================

from networkx import Graph
from networkx import all_pairs_dijkstra_path
from sqlite3 import connect


class Network:
    # Initializes the object
    def __init__(self, database_name):
        self.initialize_network(database_name)
        self.find_all_pairs_shortest_route()

    # Initializes the network
    def initialize_network(self, database_name):
        self.network = Graph()
        database_connection = connect(database_name)
        self.add_stations(database_connection)
        self.add_station_zone_assignments(database_connection)
        self.add_connections(database_connection)
        database_connection.close()

    # Adds stations to the network from the database
    def add_stations(self, database_connection):
        database_cursor = database_connection.cursor()
        select_from_station_table_string = \
           "SELECT S.name " + \
           "FROM station S"
        database_cursor.execute(select_from_station_table_string)
        database_result_set = database_cursor.fetchall()
        for database_result in database_result_set:
            station_name = database_result[0]
            self.network.add_node(station_name, zones=set())
        database_cursor.close()

    # Adds station zone assignments to the network from the database
    def add_station_zone_assignments(self, database_connection):
        database_cursor = database_connection.cursor()
        select_from_station_zone_assignment_table_string = \
           "SELECT S.name, Z.id " + \
           "FROM station_zone_assignment SZA, station S, zone Z " + \
           "WHERE SZA.station = S.id AND SZA.zone = Z.id"
        database_cursor.execute(select_from_station_zone_assignment_table_string)
        database_result_set = database_cursor.fetchall()
        for database_result in database_result_set:
            station_name = database_result[0]
            station_zone = database_result[1]
            self.network.node[station_name]["zones"].add(station_zone)
        database_cursor.close()

    # Adds connections to the network from the database
    def add_connections(self, database_connection):
        database_cursor = database_connection.cursor()
        select_from_connection_table_string = \
           "SELECT S1.name, S2.name, C.distance " + \
           "FROM station S1, station S2, connection C " + \
           "WHERE station_a = S1.id AND station_b = S2.id"
        database_cursor.execute(select_from_connection_table_string)
        database_result_set = database_cursor.fetchall()
        for database_result in database_result_set:
            station_a_name = database_result[0]
            station_b_name = database_result[1]
            distance_between_stations = database_result[2]
            self.network.add_edge(station_a_name, station_b_name,
                weight=distance_between_stations)
        database_cursor.close()

    # Finds shortest routes between all pairs of stations in the network
    def find_all_pairs_shortest_route(self):
        self.all_pairs_shortest_route = all_pairs_dijkstra_path(self.network)

    # Returns the shortest route from origin station to destination station
    # in the network
    def get_shortest_route(self, origin_station, destination_station):
        return self.all_pairs_shortest_route[origin_station][destination_station]

    # Returns the set of zones visited by the route taken in the network
    def get_zones_visited(self, route):
        zones_visited = set()
        for station in route:
            station_zones = self.network.node[station]["zones"]
            for zone in station_zones:
                zones_visited.add(zone)
        return zones_visited

    # Checks if a station is in the network
    def has_station(self, station):
        return self.network.has_node(station)

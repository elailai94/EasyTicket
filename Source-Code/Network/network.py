#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with Network objects
# @author: Elisha Lai
# @version: 1.2 16/04/2015
#==============================================================================

# Network module (network.py)

from sys import maxint
from station import Station

# Object definition
class Network:


    'Fields: num_of_stations, num_of_links, network'
    # A Network is an object in which:
    # - num_of_stations is an Int (number of stations in this network)
    # - num_of_links is an Int (number of links between stations
    #	in this network)
    # - network is a Stationdict (network)

    # A stationdict is a dictionary where:
    # - the keys are Str values 
    # - the values themselves are Stationtuples

    # A stationtuple is a 2-tuple where:
    # - the first item is a Station
    # - the second item is a Distancedict

    # A distancedict is a dictionary where:
    # - the keys are Str values
    # - the values themselves are Int values


    # Initializes the object.
    def __init__(self):
	self.__num_of_stations = 0
	self.__num_of_links = 0
        self.__network = {}


    # Returns a string representation of the object.
    def __repr__(self):
    	return 'Number of Stations:%d  Number of Links:%d  Network:%r' \
    	       % (self.__num_of_stations, self.__num_of_links, self.__network)

    # Builds network field from data files.
    def build_network(self):
    	self.__import_lines()
    	self.__import_links()


    # Imports lines into network field from data file.
    def __import_lines(self, file_name = 'lines.txt'):
        input_file = file(file_name, 'r')
        # Stores the number of lines
        num_of_lines = int(input_file.readline().strip())
        
        # Imports information for each line into network field
        # from file_name  
        i = 0
        while i < num_of_lines:
            line_file_name = input_file.readline().strip() + '.txt'
            self.__import_stations(line_file_name)
            i += 1

        input_file.close()


    # Imports stations into network field from data file.
    def __import_stations(self, file_name):
    	input_file = file(file_name, 'r')
    	# Stores the name of the line
    	line_name = input_file.readline().strip()
    	# Stores the number of stations in the line
    	num_of_stations = int(input_file.readline().strip())
    	
    	# Imports information for each station into network field
    	# from file_name
    	i = 0
    	while i < num_of_stations:
    	    station_info = input_file.readline().strip().split(';')
            station_name = station_info[0].strip()

            if station_name not in self.__network:
            	new_station = Station(station_name)
            	new_station.add_line(line_name)
            	station_zones = station_info[1].split('+')
                for zone in station_zones:
                    new_station.add_zone(int(zone.strip()))
                self.__network[station_name] = (new_station, {})
                self.__num_of_stations += 1
            else:
            	self.__network[station_name][0].add_line(line_name)
    	    i += 1

    	input_file.close()


    # Imports links into network field from data file.
    def __import_links(self, file_name = 'links.txt'):
    	input_file = file(file_name, 'r')
    	# Stores the number of links
    	num_of_links = int(input_file.readline().strip())

    	# Imports information for each link into network field
    	# from file_name
    	i = 0
    	while i < num_of_links:
    	    link_info = input_file.readline().strip().split(';')
    	    station_a = link_info[0].strip()
    	    station_b = link_info[1].strip()
    	    link_distance = float(link_info[2].strip())
    	    self.__add_link(station_a, station_b, link_distance)
    	    i += 1

    	input_file.close()


    # Adds a link between station_a and station_b in the network field
    # and labels the link with distance between the two stations.
    def __add_link(self, station_a, station_b, distance):
    	isinstance(self, Network)
    	if station_a in self.__network and\
    	   station_b in self.__network and\
    	   (station_a != station_b):
    	    self.__network[station_a][1][station_b] = distance
    	    self.__network[station_b][1][station_a] = distance
    	    self.__num_of_links += 1

    # Returns True if station is in the network. Otherwise, False is
    # returned.
    def is_in_network(self, station):
    	isinstance(self, Network)
    	return station in self.__network


    # Finds the shortest path between station_a and station_b in the
    # network field.
    def find_shortest_path(self, station_a, station_b, visited = [], distances = {}, predecessors = {}):
    	if station_a in self.__network and\
    	   station_b in self.__network:
            # Returns the path to station_b
            if station_a == station_b:
                path = []
                while station_b != None:
                    path.append(station_b)
                    station_b = predecessors.get(station_b, None)
                return distances[station_a], path[::-1]
            
            # Checks if it's the first time through and sets current
            # distance to zero
            if not visited: 
        	distances[station_a] = 0
            
            # Processes neighbours and keeps track of predecessors
            for neighbour in self.__network[station_a][1]:
                if neighbour not in visited:
                    neighbour_dist = distances.get(neighbour, maxint)
                    tentative_dist = distances[station_a] +\
                                     self.__network[station_a][1][neighbour]
                    if tentative_dist < neighbour_dist:
                        distances[neighbour] = tentative_dist
                        predecessors[neighbour] = station_a
            
            # Marks the current station as visited
            visited.append(station_a)
            # Finds the closest unvisited station to station_a
            unvisiteds = dict((k, distances.get(k, maxint)) for k in self.__network if k not in visited)
            closestnode = min(unvisiteds, key = unvisiteds.get)
            
            return self.find_shortest_path(closestnode, station_b, visited, distances, predecessors)

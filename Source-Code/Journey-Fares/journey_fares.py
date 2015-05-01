#==============================================================================
# EasyTicket
#
# @description: Module for providing methods to work with JourneyFares objects
# @author: Elisha Lai
# @version: 1.4 30/04/2015
#==============================================================================

# Journey fares module (journey_fares.py)

# Object definition
class JourneyFares:


    'Fields: num_of_fare_tiers, journey_fares'
    # A JourneyFares is an object in which:
    # - num_of_fare_tiers is an Int (number of fare tiers)
    # - journey_fares is a Faretierdict (journey fares of 
    #   all fare tiers)

    # A faretierdict is a dictionary where:
    # - the keys are Str values
    # - the values themselves are Float values


    # Initializes the object.
    def __init__(self):
	      self.__num_of_fare_tiers = 0
	      self.__journey_fares = {}

    
    # Returns a string representation of the object.
    def __repr__(self):
    	return 'Number of Fare Tiers:%d\nJourney Fares:%r' \
    	       % (self.__num_of_fare_tiers, self.__journey_fares)


    # Imports fares into the journey fares field from data file.
    def import_fares(self, file_name = 'fares.txt'):
    	input_file = file(file_name, 'r')
    	# Stores the number of fare tiers
    	num_of_fare_tiers = int(input_file.readline().strip())
    	self.__num_of_fare_tiers = num_of_fare_tiers

        # Imports information for each fare tier into the journey fares
        # field from file_name
    	i = 0
    	while i < num_of_fare_tiers:
    		fare_tier_info = input_file.readline().strip().split(';')
    		fare_tier_name = fare_tier_info[0].strip()
    		fare_tier_fare = fare_tier_info[1].strip()
    		self.__journey_fares[fare_tier_name] = round(float(fare_tier_fare), 2)
    		i += 1

    	input_file.close()


    # Looks up the journey fare for the fare tier name in journey
    # fares field.
    def lookup_fare(self, fare_tier_name):
    	return self.__journey_fares[fare_tier_name]

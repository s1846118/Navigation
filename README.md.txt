FirstJourney.py

What does this script do?
- Used when we have no data on where rubbish gathers in the lake or when we want to reset our path plan
- This script will return us a 'nice' path plan around the lake by visiting n different points. 

Arguments:
lochEdge - Path to the GEOJSON file representing the outline of the loch.
startLoc - Coordinates of the starting location of EdVarka
n - Number of centroids
loch - Name of loch. When we save geojson files after running script
       this will be added to the name.

Functions:
# TODO

Outputs:
firstJourneyloch.geojson - Geojson file containing the path plan for the boat to take with each centroid marked in blue.
loch_StartingLoc.csv - Csv file containing the starting location of the boat.
loch_centroids.csv - Csv file containing the positions of the centroids. Used for when we run centroid update.py
loch_rand.csv - Csv file containing the random points generated when we ran FirstJourney.py. These MUST be saved exactly so that the centroid positions are not altered.  

CentroidUpdate.py

What does this script do?
- We run this script after each journey given that the boat has made (> 0) journeys.
- Given data on trash found from the previous journey this script updates the locations we wish to visit 
  to hoopefully find rubbish on the next journey. 

Arguments:
trashFound (Data Type = List[List[float, float]]) - This is a list of lists of longitudes and latitudes representing positions where trash has been found.


Functions:

Outputs:


Example trash = [[-3.161460, 55.952601], [-3.160464, 55.953057], [-3.160613, 55.951984], [-3.160931, 55.952591], [-3.161129, 55.951779], [-3.162361, 55.951572]]
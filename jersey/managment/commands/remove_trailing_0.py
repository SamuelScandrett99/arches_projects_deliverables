from importlib import resources
from arches.app.models.models import ResourceInstance
from arches.app.models.resource import Resource
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.tile import Tile

class Command(BaseCommand):
    """
    Command for removing trailing zeros from HER Reference
    """

    def handle(self, *args, **options):
      
        #get all resource's
        resources = Resource.objects.filter(graph_id = '99417385-b8fa-11e6-84a5-026d961c88e6') #UUID >
        #Grab tiles for each resource
        for res in resources:
            tiles = Tile.objects.filter(resourceinstance_id = res.resourceinstanceid)
            her_node_id = "818ec4ae-2e44-11ea-8326-0275d4869ef4" #node with HER ID 
            #Loop over all tiles
            for tile in tiles:
              #Check if HER node is prsent in data 
                if her_node_id in tile.data.keys():
                  #Check if HER node has a period char
                    if '.' in tile.data[her_node_id]:
                      #If period char present split HER ID on char and take the first element
                        tile.data[her_node_id] = tile.data[her_node_id].split('.')[0] #First element is HER Number without trailing decimal
                        tile.save()

#Django
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.utils.translation import ugettext as _

#Core Arches
from arches.app.models.system_settings import settings
from arches.app.utils.betterJSONSerializer import JSONSerializer
from arches.app.utils.decorators import can_edit_resource_instance
from arches.app.models.models import MapLayer, Node
from arches.app.views.base import BaseManagerView

from arches.app.utils.betterJSONSerializer import JSONSerializer, JSONDeserializer


import datetime
from django.http import HttpResponse

#Decorators
@method_decorator(can_edit_resource_instance, name="dispatch")
class ReorderMaps(BaseManagerView):
    def post(self, request):

        json = request.body
        data = JSONDeserializer().deserialize(json)
        maps = MapLayer.objects.all()

        for i, map in enumerate(data['map_order']):
            try:
                temp = maps.get(maplayerid = map['maplayerid'])
                temp.layersortorder = i
                temp.save()
            except MapLayer.DoesNotExist:
                temp = None
                
            try:
                breakpoint()
                temp = Node.objects.get(nodeid = map['maplayerid'])
                temp.layersortorder = i
                temp.save()
            except Node.DoesNotExist:
                temp = None
                
        return HttpResponse("OK")

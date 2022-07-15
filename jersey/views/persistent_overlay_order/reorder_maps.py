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
from arches.app.models.models import MapLayer
from arches.app.views.base import BaseManagerView

from arches.app.utils.betterJSONSerializer import JSONSerializer, JSONDeserializer


import datetime
from django.http import HttpResponse

#Decorators
@method_decorator(can_edit_resource_instance, name="dispatch")
class ReorderMaps(BaseManagerView):
    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        print(html)
        return HttpResponse(html)
    
    def post(self, request):
        json = request.body
        data = JSONDeserializer().deserialize(json)
        maps = MapLayer.objects.all()
        for i, map in enumerate(data['map_order']):
            temp = maps.get(maplayerid = map['maplayerid'])
            temp.sortorder = i
            temp.save()
            print(vars(temp))
            # print(map)
        return HttpResponse("OK")
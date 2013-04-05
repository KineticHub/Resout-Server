#resout/api_app

#python helpers
import json
from datetime import datetime
from decimal import *

#django view helpers
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

#django models
from django.db.models.loading import get_model
from django.db.models import Q
from django.forms.models import model_to_dict
from django.db import models

#django authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#custom imports
from reservations_app.models import *
from camps_app.models import *
from meritbadges_app.models import *

def SerializeResponse(response_data):
    json_serializer = serializers.get_serializer("json")()
    response = json_serializer.serialize(response_data, ensure_ascii=False)
    return HttpResponse(response, mimetype="application/json")

def ReservationCamps(request, res_id):
    response_data = ReservationCamp.objects.filter(reservation=res_id)
    return SerializeResponse(response_data)

def ReservationDocuments(request, res_id):
    response_data = ReservationDocument.objects.filter(reservation=res_id)
    return SerializeResponse(response_data)

def ReservationContacts(request, res_id):
    response_data = ReservationContact.objects.filter(reservation=res_id)
    return SerializeResponse(response_data)

def CampAreas(request, camp_id):
    response_data = CampArea.objects.filter(camp=camp_id)
    return SerializeResponse(response_data)

def CampContacts(request, camp_id):
    response_data = CampContact.objects.filter(camp=camp_id)
    return SerializeResponse(response_data)

def CampDocuments(request, camp_id):
    response_data = CampDocument.objects.filter(camp=camp_id)
    return SerializeResponse(response_data)

def CampRanks(request, camp_id):
    response_data = CampRank.objects.filter(camp=camp_id)
    return SerializeResponse(response_data)

def CampStaffs(request, camp_id):
    response_data = CampStaff.objects.filter(camp=camp_id)
    response = serializers.serialize('json', response_data, indent=4, relations={'rank':{'fields':('name', 'order',)}, 'area':{'fields':('name',)}})
    return HttpResponse(response, mimetype="application/json")

def CampMeritBadges(request, camp_id):
    response_data = CampMeritBadge.objects.filter(camp=camp_id)
    response = serializers.serialize('json', response_data, indent=4, relations={'badge':{'fields':('name', 'thumbnail',)}})
    return HttpResponse(response, mimetype="application/json")

def RequirementsForBadge(request, badge_id):
    merit_badge = MeritBadge.objects.get(pk=badge_id)
    requirements = merit_badge.requirements.all()

    response_data = []
    for req in requirements:
        subreq_lvl1s = req.subrequirements_lvl1.all()
        dic_req = model_to_dict(req)
        dic_req['subrequirements'] = []
        for sublvl1 in subreq_lvl1s:
            subreq_lvl2s = sublvl1.subrequirements_lvl2.all()
            dic_sublvl1 = model_to_dict(sublvl1)
            dic_sublvl1['subrequirements'] = []
            for sublvl2 in subreq_lvl2s:
                subreq_lvl3s = sublvl2.subrequirements_lvl3.all()
                dic_sublvl2 = model_to_dict(sublvl2)
                dic_sublvl2['subrequirements'] = serializers.serialize('json', subreq_lvl3s)
                dic_sublvl1['subrequirements'].append(dic_sublvl2)
            dic_req['subrequirements'].append(dic_sublvl1)
        response_data.append(dic_req)

    return HttpResponse(json.dumps(response_data), mimetype="application/json")

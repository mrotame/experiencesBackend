from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json

class Index(View):
    def get(self, request, *args, **kwargs):
        response = {'version':'0.0.1'}
        return HttpResponse(json.dumps(response), content_type="application/json")

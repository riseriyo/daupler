from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Team, Member

#def index(request):
#    return HttpResponse("You're at the Crews' views index.")

class IndexView(generic.ListView):
    template_name = 'crews/index.html'
    context_object_name = 'latest_team_list'

    def get_queryset(self):
        return Team.objects.all()
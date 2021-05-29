from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from .models import Team, Member
from .forms import TeamForm

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'crews/index.html', {'list_of_teams': teams})

def team_detail(request, pk):
    team= Team.objects.get(pk=pk)
    return render(request, 'crews/detail.html', {'team': team})

def team_new(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=True)
            return redirect('success/')
    else:
        form = TeamForm()
    return render(request, 'crews/team_edit.html', {'form': form})
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .models import Team, Member
from .forms import TeamForm, MemberForm

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'crews/index.html', {'list_of_teams': teams})

def team_detail(request, pk):
    team= Team.objects.get(pk=pk)
    teams = Team.objects.all().prefetch_related('members')
    return render(request, 'crews/detail.html', {'team': team, 'teams': teams,'pk': pk})

def team_new(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=True)
            return redirect('success/')
    else:
        form = TeamForm()
    return render(request, 'crews/team_edit.html', {'form': form})

def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            new_member = form.save(commit=True)
            return redirect('success/')
    else:
        form = MemberForm()
    return render(request, 'crews/member_form.html', {'form': form})

def member_delete(request):
    member_id = request.POST['team']
    instance = Member.objects.get(id=member_id)
    instance.delete()
    return redirect('success/')
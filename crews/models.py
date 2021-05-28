from django.db import models
from django.http.response import HttpResponse

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_members(self):
        return HttpResponse("Get my members!")



class Member(models.Model):
    first_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.role, self.team.id)
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
    fname = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname


class Roles(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
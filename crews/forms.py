from django import forms

from .models import Team, Member

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name',)


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ('first_name','role',)
from django import forms

from .models import Team, Member

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name',)


class MemberForm(forms.ModelForm):
    team = forms.ModelChoiceField(Team.objects.all())

    class Meta:
        model = Member
        fields = ('first_name','role','team',)

'''
    def save(self, commit=True):
        instance = super().save(commit)
        # set Team reverse foreign key from Member model
        instance.team_set.add(self.cleaned_data['team'])
        return instance
'''
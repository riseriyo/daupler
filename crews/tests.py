
from django.test import TestCase, Client
from django.template.loader import render_to_string
from .models import Team, Member
from .forms import TeamForm, MemberForm
from .views import team_new
# Create your tests here.

class TeamNewTest(TestCase):

    def test_team_new_blank_fields(self):
        form = TeamForm(data={'name':''})
        self.assertFalse(form.is_valid())

    def test_team_new_returns_correct_html(self):
        response = self.client.get('/crews/')
        html = response.content.decode('utf8')
        expected_html = render_to_string('crews/index.html')
        self.assertEqual(html, expected_html)

    def test_team_new_number_of_teams(self):
        form_data = {'name':'Z'}
        form = TeamForm(data=form_data)
        form.save()
        num_of_teams = Team.objects.all().count()
        self.assertEqual(num_of_teams, 1)

    def test_member_create_and_delete_successful(self):
        form_data = {'name':'Z'}
        form = TeamForm(data=form_data)
        form.save()
        team = Team.objects.all()
        member_data = {'first_name': 'Benny Jets', 'role': 'Supervisor', 'team':str(team[0].id)}
        member_form = MemberForm(data=member_data)
        member_form.save()
        member = Member.objects.all()
        get_member = Member.objects.get(pk=member[0].id)
        get_member.delete()
        self.assertFalse(Member.objects.all(), None)
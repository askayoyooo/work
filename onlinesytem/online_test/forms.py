from django.forms import Form, fields, widgets
from online_test import models


class ProjectForm(Form):

    project_id = fields.CharField(

        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    project_name = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    test_leader_wzs_id = fields.IntegerField(
        widget=widgets.Select(choices=models.UserProfile.objects.values_list('id', 'name').filter(site='1'),
                              attrs={'class': 'form-control'})
    )
    test_leader_whq_id = fields.IntegerField(
        widget=widgets.Select(choices=models.UserProfile.objects.values_list('id', 'name').filter(site='2'),
                              attrs={'class': 'form-control'})
    )
    schedule_start = fields.DateTimeField(
        widget=widgets.TextInput(attrs={'class': 'form-control', 'readonly': 'true'})
    )
    schedule_end = fields.DateTimeField(
        widget=widgets.TextInput(attrs={'class': 'form-control', 'readonly': 'true'})
    )
    project_platform_id = fields.IntegerField(
        widget=widgets.Select(choices=models.Platform.objects.values_list('id', 'name'),
                              attrs={'class': 'form-control'})
    )
    project_type_id = fields.IntegerField(
        widget=widgets.Select(choices=models.ProjectType.objects.values_list('id', 'name'),
                              attrs={'class': 'form-control'})
    )
    project_style_id = fields.IntegerField(
        widget=widgets.Select(choices=models.ProjectStyle.objects.values_list('id', 'name'),
                              attrs={'class': 'form-control'})
    )
    project_sku_qty = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    project_is_leading_project = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
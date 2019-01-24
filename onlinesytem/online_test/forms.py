from django.forms import Form, fields, widgets
from online_test import models


class ProjectForm(Form):

    project_id = fields.CharField(

        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    project_name = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    project_model = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '多个model 用","隔开'})
    )
    test_leader_wzs_id = fields.IntegerField(
        widget=widgets.Select(
                              attrs={'class': 'form-control'})
    )
    test_leader_whq_id = fields.IntegerField(
        widget=widgets.Select(
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
    project_progress = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields["test_leader_wzs_id"].widget.choices = models.UserProfile.objects.values_list("id", "name").filter(site='1')
        self.fields["test_leader_whq_id"].widget.choices = models.UserProfile.objects.values_list("id", "name").filter(site='2')






class ProjectInfoForm(Form):

    # project_id = fields.IntegerField(
    #     widget=widgets.Select(choices=models.Project.objects.values_list('id', 'project_name').filter(),
    #                           attrs={'class': 'form-control'})
    # )
    project_id = fields.IntegerField(
        widget=widgets.Select(attrs={'class': 'form-control'})
    )
    # project_id = fields.CharField(
    #     widget=widgets.TextInput(attrs={'class': 'form-control'}),
    # )

    project_bios = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    project_mb = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    project_os = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    update_time = fields.DateTimeField(
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    dr_chipset = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_vga = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_iamt = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_storage = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_lan = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_audio = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_cr = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_wireless = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_bt = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_panel = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_finger_printer = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_g_sensor = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_camera = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_usb = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_com_parallel = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_serial_io = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_sgx = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    dr_others = fields.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super(ProjectInfoForm, self).__init__(*args, **kwargs)
        self.fields["project_id"].widget.choices = models.Project.objects.values_list("id", "project_name").filter()
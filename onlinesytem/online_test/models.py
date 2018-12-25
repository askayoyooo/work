from django.db import models
from django.contrib.auth.models import User
# user: admin  pwd: admin123


class UserProfile(models.Model):
    """
        账号表格
        记录登录信息
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True, null=True)  # 成对出现
    job_number = models.CharField(max_length=32, unique=True)
    shot_number = models.CharField(max_length=32, blank=True, null=True)
    phone_number = models.CharField(max_length=64, blank=True, null=True)
    belong_to_team = models.ForeignKey("Team", on_delete=models.CASCADE,  blank=True, null=True)
    university = models.CharField(max_length=128, blank=True, null=True)
    major = models.CharField(max_length=128, blank=True, null=True)
    role = models.ManyToManyField('Role')
    site = models.ForeignKey("Site", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    """
        Team表
        记录Team信息
        一对多：
            Tester
    """
    name = models.CharField(max_length=32, blank=True, null=True)
    team_leader = models.ForeignKey("UserProfile", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    角色表
    Tester, TestLeader, TeamLeader
    """
    name = models.CharField(max_length=32, unique=True)
    menu = models.ManyToManyField("Menu", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Role"


class Menu(models.Model):
    """
    角色菜单表
    """
    name = models.CharField(max_length=32)
    url_name = models.CharField(max_length=64)

    def __str__(self):

        return self.name

    class Meta:
        verbose_name_plural = "Menu"


class TestCase(models.Model):
    """
        Test case表
        记录test case.
    """
    case_id = models.CharField(max_length=64, unique=True)
    case_name = models.CharField(max_length=255, blank=True, null=True)
    function = models.ForeignKey("Function", on_delete=models.CASCADE, default="")
    sheet = models.ForeignKey("Sheet", on_delete=models.CASCADE, default="")
    procedure = models.TextField(max_length=4096, blank=True, null=True)
    pass_criteria = models.TextField(max_length=4096, blank=True, null=True)
    attend_time = models.IntegerField(blank=True, null=True)
    test_plan_pic_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.sheet) + "_" + str(self.case_name)


class Project(models.Model):
    """
        Project表
        记录project信息
        多对多：
            TestCase
        一对多：
            Issue
    """
    project_id = models.CharField(max_length=255, unique=True)
    project_name = models.CharField(max_length=64, blank=True, null=True)
    project_model = models.CharField(max_length=255,blank=True, null=True)
    test_leader_wzs = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name='wzs')
    test_leader_whq = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name='whq')
    schedule_start = models.DateField(verbose_name="开始日期")
    schedule_end = models.DateField(verbose_name="结束日期")
    # project_platform = models.CharField(verbose_name="平台", max_length=255, blank=True, null=True)
    project_platform = models.ForeignKey("Platform", on_delete=models.CASCADE)
    # project_type = models.CharField(verbose_name="CS/CM", max_length=255, blank=True, null=True)
    project_type = models.ForeignKey("ProjectType", on_delete=models.CASCADE)
    # project_style = models.CharField(verbose_name="AIO/DT/ThinClient", max_length=255, blank=True, null=True)
    project_style = models.ForeignKey("ProjectStyle", on_delete=models.CASCADE)
    project_sku_qty = models.CharField(verbose_name="sku 数量", max_length=255, blank=True, null=True)
    project_is_leading_project = models.CharField(verbose_name="是否Leading",max_length=255, blank=True, null=True)

    def __str__(self):
        return self.project_name


class Platform(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectStyle(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectInfo(models.Model):
    # 每次修改其中一项时，更新一整条，时间会自动生成
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    project_progress = models.CharField(verbose_name="进度", max_length=255, blank=True, null=True)
    project_bios = models.CharField(verbose_name="BIOS", max_length=255, blank=True, null=True)
    project_mb = models.CharField(verbose_name="MB", max_length=255, blank=True, null=True)
    project_os = models.CharField(verbose_name="OS", max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(auto_now_add=True, blank=True)
    dr_chipset = models.CharField(verbose_name="Chipset", max_length=255, blank=True, null=True, default=None)
    dr_vga = models.TextField(verbose_name="VGA", max_length=2000, blank=True, null=True, default=None)
    dr_iamt = models.CharField(verbose_name="iAMT", max_length=255, blank=True, null=True, default=None)
    dr_storage = models.CharField(verbose_name="Storage", max_length=255, blank=True, null=True, default=None)
    dr_lan = models.CharField(verbose_name="LAN", max_length=255, blank=True, null=True, default=None)
    dr_audio = models.TextField(verbose_name="Audio", max_length=2000, blank=True, null=True, default=None)
    dr_cr = models.CharField(verbose_name="CardReader", max_length=255, blank=True, null=True, default=None)
    dr_wireless = models.CharField(verbose_name="WirelessLAN", max_length=255, blank=True, null=True, default=None)
    dr_bt = models.CharField(verbose_name="BT", max_length=255, blank=True, null=True, default=None)
    dr_panel = models.CharField(verbose_name="Panel", max_length=255, blank=True, null=True, default=None)
    dr_finger_printer = models.CharField(verbose_name="FingerPrinter", max_length=255, blank=True, null=True, default=None)
    dr_g_sensor = models.CharField(verbose_name="G-sensor", max_length=255, blank=True, null=True, default=None)
    dr_camera = models.CharField(verbose_name="Camera", max_length=255, blank=True, null=True, default=None)
    dr_usb = models.CharField(verbose_name="USB", max_length=255, blank=True, null=True, default=None)
    dr_com_parallel = models.CharField(verbose_name="Comport Parallel", max_length=255, blank=True, null=True, default=None)
    dr_serial_io = models.CharField(verbose_name="Serial IO", max_length=255, blank=True, null=True, default=None)
    dr_sgx = models.CharField(verbose_name="SGX", max_length=255, blank=True, null=True, default=None)
    dr_others = models.CharField(verbose_name="others", max_length=255, blank=True, null=True, default=None)

    def __str__(self):
        return self.project


class Function(models.Model):
    """Functions Table"""
    function_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):

        return self.function_name


class Sheet(models.Model):
    """Functions Table"""
    sheet_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.sheet_name


class ControlTable(models.Model):
    """Control Table """
    control_table_name = models.CharField(max_length=64, unique=True, verbose_name="Task Name")
    project_name = models.ForeignKey("Project", on_delete=models.CASCADE, default="")
    function = models.ManyToManyField("Function", blank=True)
    sheet = models.ManyToManyField("Sheet", blank=True)
    tester = models.ManyToManyField("UserProfile", blank=True)

    def __str__(self):
        return str(self.control_table_name)

    class Meta:
        verbose_name_plural = "Control Table"


class PersonalTask(models.Model):
    """记录个人任务表"""
    tester = models.ForeignKey("UserProfile", on_delete=models.CASCADE, default="")
    control_table = models.ForeignKey("ControlTable", on_delete=models.CASCADE, default="" )
    sheet = models.ManyToManyField("Sheet", blank=True)

    def __str__(self):
        return str(self.tester)+str(self.sheet)

    class Meta:
        unique_together = ('tester', 'control_table')
        verbose_name_plural = "Personal Task"


class Issue(models.Model):
    """
        Issue表
        记录project Issue
        多对一：
            Tester
            TestLeader
    """
    project = models.ForeignKey('Project', on_delete=models.CASCADE, default="")
    issue_id = models.IntegerField(auto_created=True)
    bugzilla_id = models.CharField(max_length=32, blank=True, null=True)
    category_choices = (
        (0, 'HW'),
        (1, 'Key_Component'),
        (2, 'FW'),
        (3, 'Driver'),
        (4, 'SW'),
        (5, 'ME'),
    )
    category = models.SmallIntegerField(choices=category_choices, verbose_name='Category')
    attribute_choices = (
        (0, '[HW]Main Board'),
        (1, '[HW]Daughter Board'),
        (2, '[HW]Signal Integrity'),
        (3, '[HW]Antenna'),
        (4, '[HW]EMC/Safety'),
        (5, '[HW]Thermal'),
        (6, '[HW]Acoustic'),
        (7, '[HW]Others'),
        (8, '[KC]Chipset'),
        (9, '[KC]CPU/APU'),
        (10, '[KC]VGA'),
        (11, '[KC]Memory'),
        (12, '[KC]HDD/SDD/mSATA'),
        (13, '[KC]ODD'),
        (14, '[KC]Panel'),
        (15, '[KC]Touch Panel'),
        (16, '[KC]Camera'),
        (17, '[KC]Card Reader'),
        (18, '[KC]LAN'),
        (19, '[KC]WLAN'),
        (20, '[KC]BlueTooth'),
        (21, '[KC]Micphone'),
        (22, '[KC]KB/Mouse'),
        (23, '[KC]Remote Control'),
        (24, '[KC]Adapter/PSU'),
        (25, '[KC]USB'),
        (26, '[KC]Audio'),
        (27, '[KC]Speaker'),
        (28, '[KC]Sensor'),
        (29, '[KC]NFC'),
        (30, '[KC]TPM'),
        (31, '[KC]Others'),
        (32, '[FW]BIOS'),
        (33, '[FW]EC'),
        (34, '[FW]Inter ME'),
        (35, '[FW]Others'),
        (36, '[Driver]Chipset'),
        (37, '[Driver]CPU/APU'),
        (38, '[Driver]VGA'),
        (39, '[Driver]Touch Panel'),
        (40, '[Driver]Camera'),
        (41, '[Driver]Card Reader'),
        (42, '[Driver]LAN'),
        (43, '[Driver]WLAN'),
        (44, '[Driver]BlueTooth'),
        (45, '[Driver]Hot Key'),
        (46, '[Driver]Audio'),
        (47, '[Driver]Sensor'),
        (48, '[Driver]Others'),
        (49, '[SW]OS'),
        (50, '[SW]Application'),
        (51, '[SW]Preload'),
        (52, '[ME]Structure'),
        (53, '[ME]Cosmetic'),
        (54, '[ME]Cable'),
        (55, '[ME]Parts'),
        (56, '[ME]Packing'),
        (57, '[ME]ID'),
        (58, '[ME]Others'),
    )
    attribute = models.SmallIntegerField(choices=attribute_choices, verbose_name='attribute')
    attribute_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='manufacturer')
    severity_choices = (
        (0, '1'),

        (1, '2'),
        (2, '3'),
        (3, '4'),
    )
    severity = models.SmallIntegerField(choices=severity_choices, verbose_name='severity')
    description = models.TextField(max_length=2048, blank=True, null=True)
    procedure = models.TextField(max_length=2048, blank=True, null=True)
    comment = models.TextField(max_length=2048, blank=True, null=True)
    root_cause = models.TextField(max_length=2048, blank=True, null=True)
    solution = models.TextField(max_length=2048, blank=True, null=True)
    status_choice = (
        (0, 'Open'),
        (1, 'Closed'),
        (2, 'Verify'),
        (3, 'Limitation'),
    )
    status = models.SmallIntegerField(choices=status_choice, verbose_name='status')
    solving_type_choices = (
        (0, 'Fixed'),
        (1, 'Spec Changed'),
        (2, 'Design'),
        (3, 'Limitation'),
        (4, 'Deferred'),
        (5, 'Withdraw'),
        (6, 'Duplicated'),
        (7, 'Cannot Duplicated'),
    )
    solving_type = models.SmallIntegerField(choices=solving_type_choices, blank=True, null=True)
    open_date = models.DateField()
    verify_date = models.DateField(blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    owner = models.CharField(max_length=64, blank=True, null=True)
    motherboard_version = models.CharField(max_length=32, blank=True, null=True)
    bios_version = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=64, blank=True, null=True)
    remark = models.TextField(max_length=1024, blank=True, null=True)
    submitter = models.ForeignKey("UserProfile", verbose_name='bug 提交人', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.issue_id)


class TestResult(models.Model):
    """
        Test result表
        记录每个test case 的测试结果，
        多对一：
            TestCase
            Tester
            Project
        多对多：
            Issue
    """
    control_table = models.ForeignKey('ControlTable', on_delete=models.CASCADE, default='123')
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    tester = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    test_case = models.ForeignKey('TestCase', verbose_name='test case', on_delete=models.CASCADE)
    test_result_choice = (
        (0, 'Pass'),
        (1, 'Fail'),
        (2, 'N/A')
    )
    test_result = models.SmallIntegerField(choices=test_result_choice)
    issue_id = models.ForeignKey('Issue', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.project)

    class Meta:
        unique_together = ('project', 'test_case')
        verbose_name_plural = "测试结果"

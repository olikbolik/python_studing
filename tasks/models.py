from django.db import models


class Projects(models.Model):
    unique_id = models.CharField(primary_key=True, max_length=50, editable=False)
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=100)


class Users(models.Model):
    user_first_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=30)
    user_birthdate = models.DateField(blank=True, null=True)
    user_position = models.CharField(max_length=25)
    user_email = models.EmailField()
    user_avatar = models.ImageField(blank=True, null=True, upload_to="avatars/%Y/%m/%d/")
    user_project = models.ManyToManyField(Projects, blank=True, null=True)


class Tasks(models.Model):
    task_theme = models.CharField(max_length=50)
    task_description = models.CharField(max_length=100)
    task_start_date = models.DateTimeField(blank=True, null=True)
    task_end_date = models.DateTimeField(blank=True, null=True)
    BUG = "b"
    FEATURE = "f"
    TASK_TYPE = [
        (BUG, "Bug"),
        (FEATURE, "Feature")
    ]
    task_type = models.CharField(max_length=1, choices=TASK_TYPE, default=FEATURE)
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    TASK_PRIORITY = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low")
    ]
    task_priority = models.PositiveSmallIntegerField(choices=TASK_PRIORITY, default=MEDIUM)
    task_estimation_hours = models.IntegerField()
    task_developer = models.ForeignKey(Users, related_name="user_task_developer", blank=True, null=True, on_delete=models.SET("user_deleted"))
    task_creator = models.ForeignKey(Users, related_name="user_task_creator", on_delete=models.SET("user_deleted"))
    task_project = models.ForeignKey(Projects, on_delete=models.CASCADE)


class Logs(models.Model):
    log_spent_time = models.FloatField()
    log_comment = models.CharField(max_length=100)
    log_task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    log_user = models.ForeignKey(Users, on_delete=models.SET("user deleted"))


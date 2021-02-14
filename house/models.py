from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    status = models.ForeignKey('HouseStatus', models.DO_NOTHING)
    maintain_req = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'House'


class HouseStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    level_num = models.IntegerField()
    level_name = models.CharField(max_length=16)
    wear_level = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'House_Status'


class Housemate(models.Model):
    relation = models.OneToOneField('UserRelation', on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Housemate'


class Individual(models.Model):
    relation = models.OneToOneField('UserRelation', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Individual'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    relation = models.OneToOneField('UserRelation', on_delete=models.CASCADE)
    task_elo = models.IntegerField()
    assign_date = models.DateField(blank=True, null=True)
    deadline_date = models.DateTimeField(blank=True, null=True)
    has_recur = models.BooleanField()
    recur = models.OneToOneField('TaskRecurrence', on_delete=models.CASCADE)
    state = models.ForeignKey('TaskState', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Task'


class TaskRecurrence(models.Model):
    recur_id = models.AutoField(primary_key=True)
    freq_time = models.TimeField()
    freq_days = models.IntegerField()
    freq_weeks = models.IntegerField()
    freq_year = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Task_Recurrence'


class TaskState(models.Model):
    task_state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(unique=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'Task_State'


class UserRelation(models.Model):
    relation_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'User_Relation'

from django.db import models
from django.contrib.auth.models import User


class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    status = models.ForeignKey('HouseStatus', models.DO_NOTHING)
    maintain_req = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'House'

    def serialize(self):
        return {
            'house_id': self.house_id,
            'status_id': self.status_id,
            'level_num': self.status.level_name,
            'level_name': self.status.level_name,
            'wear_level': self.status.wear_level
        }


class HouseStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    level_num = models.IntegerField()
    level_name = models.CharField(max_length=16)
    wear_level = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'House_Status'

    def serialize(self):
        return {
            'status_id': self.status_id,
            'level_num': self.level_name,
            'level_name': self.level_name,
            'wear_level': self.wear_level
        }


class UserRelation(models.Model):
    relation_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'User_Relation'

    def serialize(self):
        return {
            'relation_id': self.relation_id,
            'user_id': self.user_id
        }


class Housemate(UserRelation):
    hmate_parent_rel = models.OneToOneField(UserRelation, on_delete=models.CASCADE, parent_link=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Housemate'

    def serialize(self):
        return {
            'relation_id': self.hmate_parent_rel.relation_id,
            'user_id': self.hmate_parent_rel.user_id,
            'house_id': self.house_id
        }


class Individual(UserRelation):
    indv_parent_rel = models.OneToOneField(UserRelation, on_delete=models.CASCADE, parent_link=True)

    class Meta:
        managed = False
        db_table = 'Individual'

    def serialize(self):
        return {
            'relation_id': self.indv_parent_rel.relation_id,
            'user_id': self.indv_parent_rel.user_id
        }


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

    def serialize(self):
        return {
            'task_id': self.task_id,
            'relation_id': self.relation_id,
            'task_elo': self.task_elo,
            'assign_date': self.assign_date,
            'deadline_date': self.deadline_date,
            'has_recur': self.has_recur,
            'recur_id': self.recur_id,
            'state_id': self.state_id,
            'state_str': self.state.state_name
        }


class TaskRecurrence(models.Model):
    recur_id = models.AutoField(primary_key=True)
    freq_time = models.TimeField()
    freq_days = models.IntegerField()
    freq_weeks = models.IntegerField()
    freq_year = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Task_Recurrence'

    def serialize(self):
        return {
            'recur_id': self.recur_id,
            'freq_time': self.freq_time,
            'freq_days': self.freq_days,
            'freq_weeks': self.freq_weeks,
            'freq_year': self.freq_year
        }


class TaskState(models.Model):
    task_state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(unique=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'Task_State'

    def serialize(self):
        return {
            'state_id': self.task_state_id,
            'state_name': self.state_name
        }

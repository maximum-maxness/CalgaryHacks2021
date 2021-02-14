import datetime

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import *
import house.util

f = '%Y-%m-%d %H:%M:%S'


# CREATE

def create_relation_task(relation, elo, deadline_date, task_state, recurs, recur_period):
    try:
        verifiedRelation = get_object_or_404(UserRelation, relation_id=relation.relation_id)
        task_state = get_object_or_404(TaskState, state_id=task_state)
        dt = None
        recurs = bool(recurs)
        if recurs:
            dt_ret = house.util.datetime.strptime(recur_period, f)
            year = (dt_ret.year.real - house.util.datetime.now().year.real) > 1
            dt = TaskRecurrence.objects.create(freq_time=dt_ret.time(), freq_days=dt_ret.day % 7,
                                               freq_weeks=dt_ret.day / 7,
                                               freq_year=year)
        deadline_date = house.util.datetime.strptime(deadline_date, f)
        assignment_date = house.util.datetime.now()
        ret_task = Task.objects.create(relation=verifiedRelation, task_elo=int(elo), assign_date=assignment_date,
                                       deadline_date=deadline_date, has_recur=bool(recurs), recur=dt, state=task_state)
    except Exception as e:
        print(e)
        raise Http404("Invalid data entry:", e)
    return ret_task


# Create task for a user

def create_individual_user_task(request, userid, elo, deadline_date, task_state, recurs, recur_period):
    individual = get_object_or_404(Individual, userid=userid)
    ret_task = create_relation_task(individual, elo, deadline_date, task_state, recurs, recur_period)
    return render(request, template_name='house/addUserTask.html',
                  context={'user_id': userid, 'relation': individual, 'task': ret_task})


# Create task for house and one related user

def create_task_house_single_user(request, houseid, userid, elo, deadline_date, task_state, recurs, recur_period):
    housemate = get_object_or_404(Housemate, houseid=houseid, userid=userid)
    ret_task = create_relation_task(housemate, elo, deadline_date, task_state, recurs, recur_period)
    return render(request, template_name='house/addHouseSingleUserTask.html',
                  context={'house_id': houseid, 'user_id': userid, 'relation': housemate, 'task': ret_task})


# Create task for ALL USERS within a house

def create_task_house_all_users(request, houseid, elo, deadline_date, task_state, recurs, recur_period):
    housemate_list = Housemate.objects.filter(house_id=houseid).all()
    ret_task_list = list()
    for housemate in housemate_list:
        ret_task = create_relation_task(housemate, elo, deadline_date, task_state, recurs, recur_period)
        ret_task_list.append(ret_task)
    return render(request, template_name='house/addHouseAllUserTask.html',
                  context={'house_id': houseid, 'task_list': ret_task_list})


# Create house for a user


# Create a housemate relationship between a user and a house

# READ
# Debug: Get list of all userids?

# Get list of tasks for user

def list_user_tasks(request, user_id, *args, **kwargs):
    relation_list = UserRelation.objects.filter(user_id=user_id).all()
    task_list = list()
    for relation in relation_list:
        task_list.extend(Task.objects.filter(relation_id=relation.relation_id).all())
    tasks = [x.serialize() for x in task_list]
    data = {"response": tasks}
    return JsonResponse(data)

# Get list of tasks for house

# Get list of users for house

# Get house info

# Get list of houses for user

# Get user info (username. name, join date)

# Get user stats (score, tasks completed / outstanding, houses, etc)

# Get list of tasks outstanding for a certain date range and user (within the next week, within the next day, etc)

# UPDATE

# Update entire task for user

# Update house info for all users in house

# Update entire house task for all users in house

# Update user info?? - Maybe

# Update Tasks:
#   - Update elo, how much they are worth
#   - Update deadline, when they are due
#   - Update whether a task will reoccur or not (this goes more towards create than anything)
#   - Update a task's state to finish, cancel, fail, postpone it, etc.
#   - Update who is assigned the task (relationship IDs) <- Might have to update the primary key on Task table hmmm


# DELETE

# Delete a Task
#   -For user
#   -For house and all related users
#   -For house and one related user

# Delete a housemate relationship between a user and a house

# Delete a house (thus deleting all of the related housemate relationships along with it)

# Delete a user (thus EVERYTHING related to that user as well) <- will have to process data handling, not necessarily API calls for this.

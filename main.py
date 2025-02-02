import sys
import json
import random
from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.api import TodoistAPI


def get_projects(api):
    try:
        projects = api.get_projects()
        return projects
    except Exception as error:
        print(error)


def get_project_by_id(api, id):
    try:
        project = api.get_project(project_id=id)
        return project
    except Exception as error:
        print(error)


def get_tasks_by_project_id(api, project_id):
    try:
        tasks = api.get_tasks(project_id=project_id)
        return tasks
    except Exception as error:
        print(error)


def get_random_tasks(tasks, count=1):
    return random.sample(tasks, count)


def print_tasks(tasks):
    for task in tasks:
        print("Printing task:", task.content)
        print(task)


def main():    
    token = sys.argv[1]
    project_id = sys.argv[2]
    api = TodoistAPI(token)
    tasks = get_tasks_by_project_id(api, project_id)
    selected_random_tasks = get_random_tasks(tasks, 1)
    print_tasks(selected_random_tasks)


if __name__ == '__main__':
    main()

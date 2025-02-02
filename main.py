import sys
import json
import random
import argparse
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


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", help="Todoist API token.")
    parser.add_argument("-p", "--project-id", help="ID of the Todoist project you want to select tasks from.")
    parser.add_argument("-n", "--number-of-tasks", help="Number of random tasks you want to return.")
    args = parser.parse_args()

    options = {}

    if args.token:
        options["token"] = args.token
    else:
        raise Exception("-t, --token must be provided")
    
    if args.project_id:
        options["project_id"] = args.project_id
    else:
        raise Exception("-p, --project-id must be provided")
    
    if args.number_of_tasks:
        options["number_of_tasks"] = args.number_of_tasks
    else:
        options["number_of_tasks"] = 1
        print("[INFO]: -n, --number-of-tasks not provided, using default value of: 1")

    return options


def main():
    options = parse_args()    
    
    api = TodoistAPI(options["token"])
    tasks = get_tasks_by_project_id(api, options["project_id"])
    selected_random_tasks = get_random_tasks(tasks, options["number_of_tasks"])

    print_tasks(selected_random_tasks)


if __name__ == '__main__':
    main()

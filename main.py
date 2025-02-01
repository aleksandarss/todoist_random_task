import sys
import json
from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.api import TodoistAPI


def get_projects(api):
    try:
        projects = api.get_projects()
        return projects
    except Exception as error:
        print(error)


def main():    
    token = sys.argv[1]
    api = TodoistAPI(token)
    projects = get_projects(api)
    print(projects)


if __name__ == '__main__':
    main()
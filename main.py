import sys
from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.api import TodoistAPI

print(sys.argv)

token = sys.argv[1]

api = TodoistAPI(token)

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)
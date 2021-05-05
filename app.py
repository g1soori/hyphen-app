
from flask import Flask, request
import json

class AppService:
    
    tasks = [
        {
            'id': 1,
            'name': "task10",
            "description": "This is task 1"
        },
        {
            "id": 2,
            "name": "task2",
            "description": "This is task 2"
        },
        {
            "id": 3,
            "name": "task3",
            "description": "This is task 3"
        }
    ]

    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get_tasks(self):
        return self.tasksJSON




app = Flask(__name__)
appService = AppService()


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/tasks')
def tasks():
    return appService.get_tasks()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
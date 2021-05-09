from flask import Flask, request
import json

class EmpService:
    
    tasks = [
        {
            'id': 1,
            'name': "Jeewan",
            "role": "DevOps"
        },
        {
            "id": 2,
            "name": "John",
            "role": "Engineer"
        }
    ]

    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get_tasks(self):
        return self.tasksJSON


app = Flask(__name__)
empService = EmpService()


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/tasks')
def tasks():
    return empService.get_tasks()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
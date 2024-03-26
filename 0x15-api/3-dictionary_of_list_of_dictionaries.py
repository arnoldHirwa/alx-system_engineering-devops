#!/usr/bin/python3
"""Exports to-do list information of employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            usr.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": usr.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": usr.get("id")}).json()]
            for usr in users}, jsonfile)

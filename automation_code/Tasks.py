import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Create a new task successfully
@pytest.mark.TasksEndpoint
def test_create_new_task():
    endpoint = "/tasks"
    task_data = {
        # Include your task data here
    }

    url = base_url + endpoint
    response = requests.post(url, json=task_data)

    assert response.status_code == 200
    assert "objectId" in response.json()

# Scenario 2: Attempt to create a new task with unauthorized access
@pytest.mark.TasksEndpoint
def test_create_new_task_unauthorized():
    endpoint = "/tasks"
    task_data = {
        # Include your task data here
    }

    url = base_url + endpoint
    response = requests.post(url, json=task_data)

    assert response.status_code == 403

# Scenario 3: Attempt to create a new task with missing data
@pytest.mark.TasksEndpoint
def test_create_new_task_missing_data():
    endpoint = "/tasks"
    incomplete_task_data = {
        # Include incomplete task data here
    }

    url = base_url + endpoint
    response = requests.post(url, json=incomplete_task_data)

    assert response.status_code == 404

# Run the test scenarios
test_create_new_task()
test_create_new_task_unauthorized()
test_create_new_task_missing_data()


import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Get existing tasks successfully
@pytest.mark.TasksEndpoint
def test_get_existing_tasks():
    endpoint = "/tasks"
    params = {
        "top": 10,
        "skip": 0,
        # Include other parameters here
    }

    url = base_url + endpoint
    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert "resultsCount" in response.json()
    assert "results" in response.json()

# Scenario 2: Attempt to get existing tasks with unauthorized access
@pytest.mark.TasksEndpoint
def test_get_existing_tasks_unauthorized():
    endpoint = "/tasks"
    params = {
        "top": 10,
        "skip": 0,
        # Include other parameters here
    }

    url = base_url + endpoint
    response = requests.get(url, params=params)

    assert response.status_code == 403

# Scenario 3: Attempt to get existing tasks with missing parameters
@pytest.mark.TasksEndpoint
def test_get_existing_tasks_missing_parameters():
    endpoint = "/tasks"
    incomplete_params = {
        "top": 10,
        # Include incomplete parameters here
    }

    url = base_url + endpoint
    response = requests.get(url, params=incomplete_params)

    assert response.status_code == 404

# Run the test scenarios
test_get_existing_tasks()
test_get_existing_tasks_unauthorized()
test_get_existing_tasks_missing_parameters()


import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Update an existing task and its checklist items successfully
@pytest.mark.TasksEndpoint
def test_update_existing_task():
    task_id = "your_task_id_here"
    endpoint = f"/tasks/{task_id}"
    updated_body = {
        "checklistItems": [
            {
                "taskId": "00T5e000019ZMHvEAO",
                "completed": True,
                "order": 1.1,
                # Include other checklist item attributes here
            }
        ],
        "status": "In Progress",
        # Include other updated task attributes here
    }

    url = base_url + endpoint
    response = requests.put(url, json=updated_body)

    assert response.status_code == 200
    assert "objectId" in response.json()
    assert "message" in response.json()

# Scenario 2: Attempt to update a non-existing task
@pytest.mark.TasksEndpoint
def test_update_non_existing_task():
    task_id = "non_existing_task_id"
    endpoint = f"/tasks/{task_id}"
    updated_body = {
        "checklistItems": [],
        "status": "Not Started",
    }

    url = base_url + endpoint
    response = requests.put(url, json=updated_body)

    assert response.status_code == 404

# Scenario 3: Attempt to update a task with unauthorized access
@pytest.mark.TasksEndpoint
def test_update_task_unauthorized():
    task_id = "your_task_id_here"
    endpoint = f"/tasks/{task_id}"
    updated_body = {
        "checklistItems": [],
        "status": "Not Started",
    }

    url = base_url + endpoint
    response = requests.put(url, json=updated_body)

    assert response.status_code == 403

# Run the test scenarios
test_update_existing_task()
test_update_non_existing_task()
test_update_task_unauthorized()


import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Get an existing task and its child checklist items successfully
@pytest.mark.TasksEndpoint
def test_get_existing_task():
    task_id = "your_task_id_here"
    endpoint = f"/tasks/{task_id}"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 200
    assert "checklistItems" in response.json()
    assert "status" in response.json()
    # Add other assertions to validate the response structure

# Scenario 2: Attempt to get a non-existing task
@pytest.mark.TasksEndpoint
def test_get_non_existing_task():
    task_id = "non_existing_task_id"
    endpoint = f"/tasks/{task_id}"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 404

# Scenario 3: Attempt to get a task with unauthorized access
@pytest.mark.TasksEndpoint
def test_get_task_unauthorized():
    task_id = "your_task_id_here"
    endpoint = f"/tasks/{task_id}"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 403

# Run the test scenarios
test_get_existing_task()
test_get_non_existing_task()
test_get_task_unauthorized()



import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Delete an existing task and its child checklist items successfully
@pytest.mark.TasksEndpoint
def test_delete_existing_task():
    task_id = "your_task_id_here"
    endpoint = f"/tasks/{task_id}"

    url = base_url + endpoint
    response = requests.delete(url)

    assert response.status_code == 200
    assert "message" in response.json()
    # Add other assertions to validate the response structure

# Scenario 2: Attempt to delete a non-existing task
@pytest.mark.TasksEndpoint
def test_delete_non_existing_task():
    task_id = "non_existing_task_id"
    endpoint = f"/tasks/{task_id}"

    url = base_url + endpoint
    response = requests.delete(url)

    assert response.status_code == 404

# Scenario 3: Attempt to delete a task with unauthorized access
@pytest.mark.TasksEndpoint
def test_delete_task_unauthorized():
    task_id = "your_task_id_here"
    endpoint = f"/tasks/{task_id}"

    url = base_url + endpoint
    response = requests.delete(url)

    assert response.status_code == 403

# Run the test scenarios
test_delete_existing_task()
test_delete_non_existing_task()
test_delete_task_unauthorized()



import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Get possible outcomes for an existing task
@pytest.mark.TasksEndpoint
def test_get_possible_outcomes():
    task_id = "your_task_id_here"
    endpoint = f"/tasks/{task_id}/outcomes"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 200
    assert "results" in response.json()
    # Add other assertions to validate the response structure

# Scenario 2: Attempt to get outcomes for a non-existing task
@pytest.mark.TasksEndpoint
def test_get_outcomes_non_existing_task():
    task_id = "non_existing_task_id"
    endpoint = f"/tasks/{task_id}/outcomes"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 404

# Scenario 3: Attempt to get outcomes for a task with unauthorized access
@pytest.mark.TasksEndpoint
def test_get_outcomes_unauthorized():
    task_id = "your_task_id_here"
    endpoint = f"/tasks/{task_id}/outcomes"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 403

# Run the test scenarios
test_get_possible_outcomes()
test_get_outcomes_non_existing_task()
test_get_outcomes_unauthorized()



import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Get possible statuses for tasks
@pytest.mark.TasksEndpoint
def test_get_possible_statuses():
    endpoint = "/taskStatuses"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 200
    assert "results" in response.json()
    # Add other assertions to validate the response structure

# Scenario 2: Attempt to get statuses for tasks with unauthorized access
@pytest.mark.TasksEndpoint
def test_get_statuses_unauthorized():
    endpoint = "/taskStatuses"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 403

# Run the test scenarios
test_get_possible_statuses()
test_get_statuses_unauthorized()

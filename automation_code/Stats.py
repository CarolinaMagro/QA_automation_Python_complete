import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Get task statistics for a user
@pytest.mark.StatsEndpoints
def test_get_task_statistics():
    endpoint = "/stats/tasks"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 200
    assert "today" in response.json()

# Scenario 2: Attempt to get task statistics with unauthorized access
@pytest.mark.StatsEndpoints
def test_get_task_statistics_unauthorized():
    endpoint = "/stats/tasks"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 403

# Scenario 3: Attempt to get task statistics for non-existing user
@pytest.mark.StatsEndpoints
def test_get_task_statistics_non_existing_user():
    endpoint = "/stats/tasks"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 404

# Run the test scenarios
test_get_task_statistics()
test_get_task_statistics_unauthorized()
test_get_task_statistics_non_existing_user()


import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Get event statistics for a user
@pytest.mark.StatsEndpoints
def test_get_event_statistics():
    endpoint = "/stats/events"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 200
    assert "today" in response.json()

# Scenario 2: Attempt to get event statistics with unauthorized access
@pytest.mark.StatsEndpoints
def test_get_event_statistics_unauthorized():
    endpoint = "/stats/events"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 403

# Scenario 3: Attempt to get event statistics for non-existing user
@pytest.mark.StatsEndpoints
def test_get_event_statistics_non_existing_user():
    endpoint = "/stats/events"

    url = base_url + endpoint
    response = requests.get(url)

    assert response.status_code == 404

# Run the test scenarios
test_get_event_statistics()
test_get_event_statistics_unauthorized()
test_get_event_statistics_non_existing_user()

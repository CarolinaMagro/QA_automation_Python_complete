import requests

BASE_URL = "https://api.example.com"
API_KEY = "your_api_key"

# Replace with actual test data
event_id = "sample_event_id"
non_existing_event_id = "non_existing_event_id"
sample_household_id = "sample_household_id"
# Test scenarios
def test_get_existing_event():
    url = f"{BASE_URL}/events/{event_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert "Payload of DynEvent" in response.json().get("response_description", "")
    assert "activityDateTime" in response.json()
    assert "crmId" in response.json()

def test_get_non_existing_event():
    url = f"{BASE_URL}/events/{non_existing_event_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 404
    assert "Specified event is not found." in response.text

def test_access_denied():
    url = f"{BASE_URL}/events/{event_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 403
    assert "Specified event is not found." in response.text



# Test scenarios
def test_update_existing_event():
    url = f"{BASE_URL}/events/{event_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"description": "string"}
    response = requests.put(url, headers=headers, json=payload)

    assert response.status_code == 200
    assert "The task was updated successfully." in response.json().get("response_description", "")
    assert "objectId" in response.json()

def test_update_non_existing_event():
    url = f"{BASE_URL}/events/{non_existing_event_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"description": "string"}
    response = requests.put(url, headers=headers, json=payload)

    assert response.status_code == 404

def test_access_denied():
    url = f"{BASE_URL}/events/{event_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"description": "string"}
    response = requests.put(url, headers=headers, json=payload)

    assert response.status_code == 403



# Test scenarios
def test_get_events_successfully():
    url = f"{BASE_URL}/events"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {
        "top": 10,
        "skip": 0,
        "toDate": "2023-08-25T18:00:00.000Z",
        "fromDate": "2023-08-01T00:00:00.000Z",
        "householdId": sample_household_id
    }
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 200
    assert "Payload of DynQueryResult containing DynEvent" in response.json().get("response_description", "")
    assert response.json().get("resultsCount", 0) > 0
    assert "results" in response.json()

def test_get_events_not_found():
    url = f"{BASE_URL}/events"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {
        "top": 10,
        "skip": 0,
        "toDate": "2023-08-25T18:00:00.000Z",
        "fromDate": "2023-08-01T00:00:00.000Z",
        "householdId": sample_household_id
    }
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 404

def test_access_denied():
    url = f"{BASE_URL}/events"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {
        "top": 10,
        "skip": 0,
        "toDate": "2023-08-25T18:00:00.000Z",
        "fromDate": "2023-08-01T00:00:00.000Z",
        "householdId": sample_household_id
    }
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 403

# Run the tests
test_get_events_successfully()
test_get_events_not_found()
test_access_denied()


# Run the tests
test_update_existing_event()
test_update_non_existing_event()
test_access_denied()

# Run the tests
test_get_existing_event()
test_get_non_existing_event()
test_access_denied()

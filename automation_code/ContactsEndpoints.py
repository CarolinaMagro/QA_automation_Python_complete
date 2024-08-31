import requests

BASE_URL = "https://api.example.com"
API_KEY = "your_api_key"

# Replace with actual test data
contact_id = "sample_contact_id"
non_existing_contact_id = "non_existing_contact_id"

# Replace with actual test data
query_param = "sample_query"
top_param = 10
skip_param = 0
account_stage_param = "sample_stage"

# Test scenarios
def test_get_existing_contact():
    url = f"{BASE_URL}/Contacts/{contact_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert "Contact retrieved successfully" in response.json().get("response_description", "")
    assert "firstName" in response.json() and response.json()["firstName"] == "string"
    assert "lastName" in response.json() and response.json()["lastName"] == "string"

def test_non_existing_contact():
    url = f"{BASE_URL}/Contacts/{non_existing_contact_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 404
    assert response.text == "Specified contact is not found."

def test_access_denied():
    url = f"{BASE_URL}/Contacts/{contact_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 403
    assert response.text == "Specified contact is not found."





# Test scenarios
def test_get_list_of_dynpeople():
    url = f"{BASE_URL}/Contacts"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {
        "query": query_param,
        "top": top_param,
        "skip": skip_param,
        "accountStage": account_stage_param
    }
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 200
    assert "Search results" in response.json().get("response_description", "")
    assert response.json().get("resultsCount") == 1
    assert response.json().get("next") == "prospects?top=1&skip=0"
    assert isinstance(response.json().get("results"), list)
    assert response.json()["results"][0]["name"] == "John Browne"
    assert response.json()["results"][0]["crmId"] == "0015e000010mXutAAE"

def test_get_empty_list_of_dynpeople():
    url = f"{BASE_URL}/Contacts"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {
        "query": "non_existing_query",
        "top": top_param,
        "skip": skip_param,
        "accountStage": account_stage_param
    }
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 404
    assert response.text == ""

def test_access_denied():
    url = f"{BASE_URL}/Contacts"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {
        "query": query_param,
        "top": top_param,
        "skip": skip_param,
        "accountStage": account_stage_param
    }
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 403
    assert response.text == ""

# Run the tests
test_get_list_of_dynpeople()
test_get_empty_list_of_dynpeople()
test_access_denied()
# Run the tests
test_get_existing_contact()
test_non_existing_contact()
test_access_denied()
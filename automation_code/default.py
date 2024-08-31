import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Complete a checklist item successfully
@pytest.mark.ChecklistItems
def test_complete_checklist_item():
    endpoint = "/checklistItems/{id}"
    item_id = "0015e000014LsiNAAS"

    url = base_url + endpoint.format(id=item_id)
    response = requests.put(url)

    assert response.status_code == 200
    assert response.json()["httpCode"] == 200

# Scenario 2: Attempt to complete a non-existing checklist item
@pytest.mark.ChecklistItems
def test_complete_nonexistent_item():
    endpoint = "/checklistItems/{id}"
    item_id = "nonexistent"

    url = base_url + endpoint.format(id=item_id)
    response = requests.put(url)

    assert response.status_code == 404

# Scenario 3: Attempt to complete a checklist item with unauthorized access
@pytest.mark.ChecklistItems
def test_complete_item_unauthorized():
    endpoint = "/checklistItems/{id}"
    item_id = "0015e000014LsiNAAS"

    url = base_url + endpoint.format(id=item_id)
    response = requests.put(url)

    assert response.status_code == 403

# Run the test scenarios
test_complete_checklist_item()
test_complete_nonexistent_item()
test_complete_item_unauthorized()

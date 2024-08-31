import requests
import json
import pytest

# Step definitions
@Given('the endpoint "{endpoint}"')
def set_endpoint(context, endpoint):
    context.endpoint = endpoint

@Given('the module "{module}"')
def set_module(context, module):
    context.module = module

@Given('the request body is')
def set_request_body(context):
    context.request_body = context.text

@When('I make a POST request')
def make_post_request(context):
    url = f"BASE_URL{context.endpoint}"  # Replace BASE_URL with the actual base URL
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=context.request_body, headers=headers)
    context.response = response

@Then('the response status code should be {response_code}')
def validate_response_code(context, response_code):
    assert context.response.status_code == int(response_code)

@Then('the response description should be "{response_description}"')
def validate_response_description(context, response_description):
    assert context.response_description == response_description

@Then('the response body should contain "{response_example}"')
def validate_response_body(context, response_example):
    response_data = context.response.json()
    assert json.dumps(response_data) == response_example

# Test scenarios
@prospects
def test_create_new_prospect_successful(context):
    context.endpoint = "/prospects"
    context.module = "Prospects"
    context.request_body = """
    {
      "householdType": "CRM",
      "name": "Browne Family",
      "tier": null,
      ...
      "crmContact": null
    }
    """
    context.response_code = 200
    context.response_description = "The prospect was created successfully."
    context.response_example = '{"objectId":"0015e000014LsiNAAS","message":"Creation successful.","requestId":"a63f88fe-a2a3-428b-ae24-09e1fb1cbe5b","httpCode":200}'

@prospects
def test_create_new_prospect_not_found(context):
    context.endpoint = "/prospects"
    context.module = "Prospects"
    context.request_body = """
    {
      "householdType": "CRM",
      "name": "Browne Family",
      "tier": null,
      ...
      "crmContact": null
    }
    """
    context.response_code = 404
    context.response_description = "-"

@prospects
def test_create_new_prospect_forbidden(context):
    context.endpoint = "/prospects"
    context.module = "Prospects"
    context.request_body = """
    {
      "householdType": "CRM",
      "name": "Browne Family",
      "tier": null,
      ...
      "crmContact": null
    }
    """
    context.response_code = 403
    context.response_description = "-"


import requests
import json
import behave

# Define the base URL for the API
BASE_URL = "https://api.example.com"  # Replace with the actual API URL

# Define custom step decorators
given = behave.given
when = behave.when
then = behave.then

# Custom step to set the endpoint and URL
@given('the endpoint "{endpoint}"')
def step_given_endpoint(context, endpoint):
    context.endpoint = endpoint
    context.url = BASE_URL + endpoint

# Custom step to make a GET request with parameters
@when('I make a GET request with parameters:')
def step_when_get_request_with_parameters(context):
    params = json.loads(context.text)
    context.response = requests.get(context.url, params=params)

# Custom step to verify the response status code
@then('the response status code should be {status_code}')
def step_then_response_status_code(context, status_code):
    assert str(context.response.status_code) == status_code, f"Expected {status_code}, but got {context.response.status_code}"

# Custom step to verify the response description
@then('the response description should be "{description}"')
def step_then_response_description(context, description):
    response_data = context.response.json()
    assert response_data.get('message') == description, f"Expected '{description}', but got '{response_data.get('message')}''"

# Custom step to verify the response body
@then('the response body should contain:')
def step_then_response_body_contains(context):
    expected_body = json.loads(context.text)
    response_data = context.response.json()
    assert response_data == expected_body, f"Expected '{expected_body}', but got '{response_data}'"

import requests
import json
import behave

# Define the base URL for the API
BASE_URL = "https://api.example.com"  # Replace with the actual API URL

# Define custom step decorators
given = behave.given
when = behave.when
then = behave.then

# Custom step to set the endpoint and URL
@given('the endpoint "{endpoint}"')
def step_given_endpoint(context, endpoint):
    context.endpoint = endpoint

# Custom step to make a GET request with parameters
@when('I make a GET request with the following parameters:')
def step_when_get_request_with_parameters(context):
    params = json.loads(context.text)
    url = BASE_URL + context.endpoint.format(**params)
    context.response = requests.get(url)

# Custom step to verify the response status code
@then('the response status code should be {status_code}')
def step_then_response_status_code(context, status_code):
    assert str(context.response.status_code) == status_code, f"Expected {status_code}, but got {context.response.status_code}"

# Custom step to verify the response description
@then('the response description should be "{description}"')
def step_then_response_description(context, description):
    response_data = context.response.json()
    assert response_data.get('message') == description, f"Expected '{description}', but got '{response_data.get('message')}''"

# Custom step to verify the response body
@then('the response body should contain:')
def step_then_response_body_contains(context):
    expected_body = json.loads(context.text)
    response_data = context.response.json()
    assert response_data == expected_body, f"Expected '{expected_body}', but got '{response_data}'"

# Execute the feature file
if __name__ == '__main__':
    behave.__main__.main("prospects.feature")

import requests

# Base URL for the API
base_url = "https://api.example.com"

# Scenario 1: Update an existing prospect successfully
@Given('the endpoint "{endpoint}"')
def step_given_endpoint(context, endpoint):
    context.endpoint = endpoint

@Given('the request body:')
def step_given_request_body(context):
    context.request_body = context.text

@When('I make a PUT request with the following parameters:')
def step_when_make_put_request(context):
    url = base_url + context.endpoint.format(id=context.id)
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=context.request_body, headers=headers)
    context.response = response

@Then('the response status code should be {status_code}')
def step_then_response_status_code(context, status_code):
    assert str(context.response.status_code) == status_code

@Then('the response description should be "{description}"')
def step_then_response_description(context, description):
    response_json = context.response.json()
    assert response_json.get('message', '') == description

# Scenario 2: Attempt to update a non-existing prospect
# (Similar steps as Scenario 1 with different parameters)

# Scenario 3: Attempt to update a prospect with forbidden access
# (Similar steps as Scenario 1 with different parameters)
#pip install behave


import requests

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Update existing prospect and associated contacts attributes successfully
def test_update_existing_prospect_attributes():
    endpoint = "/prospects/{id}/attributes"
    prospect_id = "sample_id"
    request_body = [{"attrName": "CONTACT_0.Name", "attrValue": "Thom Yorke"}]

    url = base_url + endpoint.format(id=prospect_id)
    response = requests.put(url, json=request_body)

    assert response.status_code == 200
    assert response.json()["message"] == "Prospect updated successfully"

# Scenario 2: Attempt to update non-existing prospect and associated contacts attributes
def test_update_non_existing_prospect_attributes():
    endpoint = "/prospects/{id}/attributes"
    prospect_id = "non_existing_id"
    request_body = [{"attrName": "CONTACT_0.Name", "attrValue": "Thom Yorke"}]

    url = base_url + endpoint.format(id=prospect_id)
    response = requests.put(url, json=request_body)

    assert response.status_code == 404

# Scenario 3: Attempt to update prospect and associated contacts attributes with forbidden access
def test_update_prospect_attributes_forbidden():
    endpoint = "/prospects/{id}/attributes"
    prospect_id = "sample_id"
    request_body = [{"attrName": "CONTACT_0.Name", "attrValue": "Thom Yorke"}]

    url = base_url + endpoint.format(id=prospect_id)
    response = requests.put(url, json=request_body)

    assert response.status_code == 403

# Run the test scenarios
test_update_existing_prospect_attributes()
test_update_non_existing_prospect_attributes()
test_update_prospect_attributes_forbidden()


import requests
import pytest

# Define the API base URL
base_url = "https://api.example.com"

# Scenario 1: Get all attributes of an existing prospect
@pytest.mark.Prospects
def test_get_existing_prospect_attributes():
    endpoint = "/prospects/{id}/attributes"
    prospect_id = "sample_id"

    url = base_url + endpoint.format(id=prospect_id)
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json() != {}

# Scenario 2: Attempt to get attributes of a non-existing prospect
@pytest.mark.Prospects
def test_get_non_existing_prospect_attributes():
    endpoint = "/prospects/{id}/attributes"
    prospect_id = "non_existing_id"

    url = base_url + endpoint.format(id=prospect_id)
    response = requests.get(url)

    assert response.status_code == 404

# Scenario 3: Attempt to get attributes of a prospect with forbidden access
@pytest.mark.Prospects
def test_get_prospect_attributes_forbidden():
    endpoint = "/prospects/{id}/attributes"
    prospect_id = "sample_id"

    url = base_url + endpoint.format(id=prospect_id)
    response = requests.get(url)

    assert response.status_code == 403

# Run the test scenarios
test_get_existing_prospect_attributes()
test_get_non_existing_prospect_attributes()
test_get_prospect_attributes_forbidden()

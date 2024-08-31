import requests
import json
import pytest

from Prospects import \
    given, \
    then, \
    when

BASE_URL = "https://api.example.com"
API_KEY = "your_api_key"

# Step definitions
@given('the base URL is "{base_url}"')
def step_given_base_url(context, base_url):
    context.base_url = base_url

@given('the API key is "{api_key}"')
def step_given_api_key(context, api_key):
    context.api_key = api_key

@when('I make a POST request')
def step_when_make_post_request(context):
    url = f"{context.base_url}{context.endpoint}"
    headers = {"Authorization": f"Bearer {context.api_key}"}
    response = requests.post(url, headers=headers, json=context.request_body)
    context.response = response

@then('the response status code should be {expected_status}')
def step_then_response_status_code(context, expected_status):
    assert context.response.status_code == int(expected_status)

@then('the response description should be "{expected_description}"')
def step_then_response_description(context, expected_description):
    assert context.response.json().get("response_description") == expected_description

@then('the response JSON should contain "{expected_key}"')
def step_then_response_json_contains_key(context, expected_key):
    response_json = context.response.json()
    assert expected_key in response_json
    assert response_json[expected_key] == context.expected_response[expected_key]

# Test data
@pytest.fixture
def context():
    return {}

# Scenarios
#@Households
def test_create_new_household_success(context):
    context.endpoint = "/Households"
    context.module = "Households"
    context.request_body = {
        "householdType": "CRM",
        # ... other fields ...
    }
    context.response_code = 200
    context.response_description = "The Household was created successfully."
    context.expected_response = {
        "householdType": "CRM",
        # ... other fields ...
    }
    context.expected_status = 200

#@Households
def test_create_new_household_not_found(context):
    context.endpoint = "/Households"
    context.module = "Households"
    context.request_body = {
        "householdType": "CRM",
        # ... other fields ...
    }
    context.response_code = 404
    context.response_description = "-"
    context.expected_status = 404

#@Households
def test_create_new_household_forbidden(context):
    context.endpoint = "/Households"
    context.module = "Households"
    context.request_body = {
        "householdType": "CRM",
        # ... other fields ...
    }
    context.response_code = 403
    context.response_description = "-"
    context.expected_status = 403



import requests
import pytest

BASE_URL = "https://api.example.com"
API_KEY = "your_api_key"

# Step definitions
@given('the base URL is "{base_url}"')
def step_given_base_url(context, base_url):
    context.base_url = base_url

@given('the API key is "{api_key}"')
def step_given_api_key(context, api_key):
    context.api_key = api_key

@when('I make a GET request')
def step_when_make_get_request(context):
    url = f"{context.base_url}{context.endpoint}"
    headers = {"Authorization": f"Bearer {context.api_key}"}
    response = requests.get(url, headers=headers)
    context.response = response

@then('the response status code should be {expected_status}')
def step_then_response_status_code(context, expected_status):
    assert context.response.status_code == int(expected_status)

@then('the response description should be "{expected_description}"')
def step_then_response_description(context, expected_description):
    assert context.response.json().get("response_description") == expected_description

@then('the response JSON should contain "{expected_key}" with value "{expected_value}"')
def step_then_response_json_contains_key(context, expected_key, expected_value):
    response_json = context.response.json()
    assert expected_key in response_json
    assert response_json[expected_key] == expected_value

# Scenarios
#@Households
def test_get_households_success(context):
    context.endpoint = "/Households"
    context.module = "Households"
    context.response_code = 200
    context.response_description = "Search results"
    context.expected_key = "resultsCount"
    context.expected_value = 1
    context.expected_status = 200

#@Households
def test_get_households_not_found(context):
    context.endpoint = "/Households"
    context.module = "Households"
    context.response_code = 404
    context.response_description = "-"
    context.expected_status = 404

#@Households
def test_get_households_forbidden(context):
    context.endpoint = "/Households"
    context.module = "Households"
    context.response_code = 403
    context.response_description = "-"
    context.expected_status = 403


import requests
import pytest

BASE_URL = "https://api.example.com"
API_KEY = "your_api_key"

# Step definitions
# Similar to previous step definitions, you can reuse them here

@when('I make a GET request with id "{id}"')
def step_when_make_get_request_with_id(context, id):
    url = f"{context.base_url}{context.endpoint}".replace("{id}", id)
    headers = {"Authorization": f"Bearer {context.api_key}"}
    response = requests.get(url, headers=headers)
    context.response = response

# Scenarios
#@Households
def test_get_existing_household_success(context):
    context.endpoint = "/Households/{id}"
    context.module = "Households"
    context.response_code = 200
    context.response_description = "Household retrieved successfully"
    context.expected_name = "Browne Family"
    context.id = "sample_id"

#@Households
def test_get_existing_household_not_found(context):
    context.endpoint = "/Households/{id}"
    context.module = "Households"
    context.response_code = 404
    context.response_description = "-"
    context.id = "sample_id"

# Step definitions
# Similar to previous step definitions, you can reuse them here

@when('I make a PUT request with id "{id}"')
def step_when_make_put_request_with_id(context, id):
    url = f"{context.base_url}{context.endpoint}".replace("{id}", id)
    headers = {"Authorization": f"Bearer {context.api_key}", "Content-Type": "application/json"}
    response = requests.put(url, json=context.request_body, headers=headers)
    context.response = response



#@Households
def test_retrieve_box_frup_forbidden(context):
    context.endpoint = "/Households/{id}/box"
    context.module = "Households"
    context.response_code = 403
    context.response_description = "-"
    context.id = "sample_id"

    # Perform the GET request and validate the response
    response = make_get_request(context)
    validate_response(response, context)

# Helper functions
def make_get_request(context):
    url = BASE_URL + context.endpoint.replace("{id}", context.id)
    headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(url, headers=headers)
    return response

def validate_response(response, context):
    assert response.status_code == context.response_code
    response_json = response.json()
    assert response_json["message"] == context.response_description

# Scenarios
#@Households
def test_create_box_frup_success(context):
    context.endpoint = "/Households/{id}/box"
    context.module = "Households"
    context.response_code = 200
    context.response_description = "The box folder was successfully added to the CRM Household."
    context.id = "sample_id"
    context.request_body = {
        "box__Folder_ID__c": "sample_folder_id",
        "box__Record_ID__c": "sample_record_id",
        "box__Permission__c": "read",
        "ownerId": "sample_owner_id",
        "name": "Sample Box Frup",
        "attributes": {
            "type": "Box_Frup__c",
            "referenceId": "ref1"
        },
        "id": "sample_id",
        "createdById": "sample_creator_id",
        "lastModifiedById": "sample_modifier_id",
        "lastModifiedDate": "2023-08-25T15:22:02.269Z"
    }

#@Households
def test_create_box_frup_not_found(context):
    context.endpoint = "/Households/{id}/box"
    context.module = "Households"
    context.response_code = 404
    context.response_description = "-"
    context.id = "sample_id"
    context.request_body = {
        "box__Folder_ID__c": "sample_folder_id",
        "box__Record_ID__c": "sample_record_id",
        "box__Permission__c": "read",
        "ownerId": "sample_owner_id",
        "name": "Sample Box Frup",
        "attributes": {
            "type": "Box_Frup__c",
            "referenceId": "ref1"
        },
        "id": "sample_id",
        "createdById": "sample_creator_id",
        "lastModifiedById": "sample_modifier_id",
        "lastModifiedDate": "2023-08-25T15:22:02.269Z"
    }


    # Perform the POST request and validate the response
    response = make_post_request(context)
    validate_response(response, context)

# Helper functions
def make_post_request(context):
    url = BASE_URL + context.endpoint.replace("{id}", context.id)
    headers = {"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"}
    response = requests.post(url, json=context.request_body, headers=headers)
    return response

def validate_response(response, context):
    assert response.status_code == context.response_code
    response_json = response.json()
    assert response_json["message"] == context.response_description
    if context.response_code == 200:
        assert "objectId" in response_json




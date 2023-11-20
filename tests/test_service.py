# Import necessary modules for testing.
import pytest
import src.service as service
import unittest.mock as mock
import requests


@mock.patch("src.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    """
    Test function to check the behavior of 'get_user_from_db' when mocked.
    """
    # Mock the return value of the function.
    mock_get_user_from_db.return_value = "Mocked Alice"
    # Call the function and check if the return value matches the mocked value.
    user_name = service.get_user_from_db(1)
    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):
    """
    Test function to check the behavior of 'get_users' when mocked with a successful response.
    """
    # Create a mock response with a status code of 200 and a JSON return value.
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    # Set the mock to return the created response.
    mock_get.return_value = mock_response
    # Call the function and check if the returned data matches the expected value.
    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    """
    Test function to check the behavior of 'get_users' when mocked with an error response.
    """
    # Create a mock response with a status code of 400.
    mock_response = mock.Mock()
    mock_response.status_code = 400
    # Set the mock to return the created error response.
    mock_get.return_value = mock_response
    # Use pytest.raises to check if a requests.HTTPError is raised.
    with pytest.raises(requests.HTTPError):
        service.get_users()

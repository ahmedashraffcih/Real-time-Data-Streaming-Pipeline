# test_dag.py

import sys
sys.path.append("D:/Personal Projects/Realtime Data Streaming/")
from unittest.mock import patch
from data_generation.format_data import format_data


def test_format_data():
    # Define a mock response with fixed data
    mock_response = {
        'name': {'first': 'John', 'last': 'Doe'},
        'gender': 'male',
        'location': {
            'street': {'number': 123, 'name': 'Main St'},
            'city': 'City',
            'state': 'State',
            'country': 'Country',
            'postcode': '12345'
        },
        'email': 'john.doe@example.com',
        'login': {'username': 'johndoe'},
        'dob': {'date': '2000-01-01'},
        'registered': {'date': '2024-01-01'},
        'phone': '123-456-7890',
        'picture': {'medium': 'http://example.com/picture.jpg'}
    }

    # Call the function under test
    formatted_data = format_data(mock_response)

    # Assert that the function returns the expected formatted data
    assert formatted_data['first_name'] == 'John'
    assert formatted_data['last_name'] == 'Doe'
    assert formatted_data['gender'] == 'male'
    assert formatted_data['address'] == '123 Main St, City, State, Country'
    assert formatted_data['post_code'] == '12345'
    assert formatted_data['email'] == 'john.doe@example.com'
    assert formatted_data['username'] == 'johndoe'
    assert formatted_data['dob'] == '2000-01-01'
    assert formatted_data['registered_date'] == '2024-01-01'
    assert formatted_data['phone'] == '123-456-7890'
    assert formatted_data['picture'] == 'http://example.com/picture.jpg'

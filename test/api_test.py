import requests
import pytest


@pytest.fixture
def api_url():
    return "http://localhost:8000/api/v1"


def test_get_available_moves(api_url):
    chess_figure = "pawns"
    current_field = "H2"
    expected_response = {
        "availableMoves": ["h3", "h4"],
        "error": None,
        "figure": "pawns",
        "currentField": "H2",
    }

    response = requests.get(f"{api_url}/{chess_figure}/{current_field}")
    assert response.status_code == 200
    assert response.json() == expected_response


def test_get_available_moves_valid_field(api_url):
    chess_figure = "rook"
    current_field = "H15"
    expected_response = {
        "availableMoves": [],
        "error": "Invalid row value",
        "figure": "rook",
        "currentField": "H15",
    }

    response = requests.get(f"{api_url}/{chess_figure}/{current_field}")
    assert response.status_code == 409
    assert response.json() == expected_response


def test_not_existing_figure(api_url):
    chess_figure = "rooook"
    current_field = "H2"

    response = requests.get(f"{api_url}/{chess_figure}/{current_field}")
    assert response.status_code == 404


def test_valid_move(api_url):
    chess_figure = "rook"
    current_field = "H2"
    dest_field = "H3"
    expected_response = {
        "move": "valid",
        "figure": "rook",
        "error": None,
        "currentField": "H2",
        "destField": "H3",
    }
    response = requests.get(f"{api_url}/{chess_figure}/{current_field}/{dest_field}")
    assert response.status_code == 200
    assert response.json() == expected_response


def test_invalid_move(api_url):
    chess_figure = "rook"
    current_field = "H2"
    dest_field = "A3"
    expected_response = {
        "move": "invalid",
        "figure": "rook",
        "error": "Current move is not permitted.",
        "currentField": "H2",
        "destField": "A3",
    }
    response = requests.get(f"{api_url}/{chess_figure}/{current_field}/{dest_field}")
    assert response.status_code == 409
    assert response.json() == expected_response

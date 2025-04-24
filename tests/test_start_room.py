import builtins
import pytest
from rooms.start_room import StartRoom
from rooms.hallway import Hallway

@pytest.fixture
def mock_print(monkeypatch):
    printed = []
    monkeypatch.setattr(builtins, "print", lambda msg:printed.append(msg))
    return printed

def test_get_description_contains_expected_text():
    room = StartRoom()
    description = room.get_description()
    assert "Nacházíš se v temné cele" in description
    assert "Příkazy" in description

def test_handle_command_vyjdi_ven_resurns_hallway(mock_print):
    room = StartRoom()
    result = room.handle_command("vyjdi ven")
    assert isinstance(result, Hallway)
    assert "otevíráš dveře a vsupuješ do temné chodby..." in mock_print[0]

def test_handle_cpmmand_porozhlednout_prints_description_and_returns_none(mock_print):
    room = StartRoom()
    result = room.handle_command("porozhlednout")
    assert result is None
    assert "zrezivělý zámek" in mock_print[0]

def test_handle_command_unknow_returnt_none_and_prints_error(mock_print):
    room = StartRoom()
    result = room.handle_command("neexistujici prikaz")
    assert result is None
    assert "Nerozumím tomuto příkazu" in mock_print[0]

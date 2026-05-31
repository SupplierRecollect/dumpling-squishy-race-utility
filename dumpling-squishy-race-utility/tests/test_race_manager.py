import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.race_manager import RaceManager

def test_create_race():
    mgr = RaceManager("test_game_123")
    result = mgr.create_race("race_001", ["player1", "player2"])
    assert result["status"] == "waiting"
    assert len(result["participants"]) == 2

def test_start_race():
    mgr = RaceManager("test_game_123")
    mgr.create_race("race_002", ["p1", "p2"])
    assert mgr.start_race("race_002") == True
    assert mgr.get_race_status("race_002") == "racing"

def test_finish_race():
    mgr = RaceManager("test_game_123")
    mgr.create_race("race_003", ["a", "b"])
    mgr.start_race("race_003")
    result = mgr.finish_race("race_003", "a")
    assert result["winner"] == "a"
    assert result["status"] == "finished"

def test_duplicate_race():
    mgr = RaceManager("test_game_123")
    mgr.create_race("race_004", ["x"])
    try:
        mgr.create_race("race_004", ["y"])
        assert False
    except ValueError:
        assert True

def test_unknown_race():
    mgr = RaceManager("test_game_123")
    assert mgr.get_race_status("nonexistent") == "unknown"
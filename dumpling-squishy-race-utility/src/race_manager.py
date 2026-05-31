import requests

class RaceManager:
    def __init__(self, game_id: str):
        self.game_id = game_id
        self.active_races = {}
        self.base_url = "https://apis.roblox.com/cloud/v2"

    def create_race(self, race_id: str, participants: list) -> dict:
        if race_id in self.active_races:
            raise ValueError(f"Race {race_id} already exists")
        payload = {
            "race_id": race_id,
            "participants": participants,
            "status": "waiting"
        }
        self.active_races[race_id] = payload
        return payload

    def start_race(self, race_id: str) -> bool:
        race = self.active_races.get(race_id)
        if not race:
            return False
        race["status"] = "racing"
        return True

    def get_race_status(self, race_id: str) -> str:
        race = self.active_races.get(race_id)
        return race["status"] if race else "unknown"

    def finish_race(self, race_id: str, winner: str) -> dict:
        race = self.active_races.get(race_id)
        if not race:
            return {}
        race["status"] = "finished"
        race["winner"] = winner
        return race
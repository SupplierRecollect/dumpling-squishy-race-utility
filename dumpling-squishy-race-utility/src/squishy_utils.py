import random

class SquishyUtils:
    DUMPLING_TYPES = ["classic", "pork", "veggie", "shrimp", "spicy"]

    @staticmethod
    def random_dumpling() -> str:
        return random.choice(SquishyUtils.DUMPLING_TYPES)

    @staticmethod
    def calculate_squish_factor(dumpling_type: str, squish_power: float) -> float:
        base_squish = {"classic": 1.0, "pork": 1.2, "veggie": 0.8, "shrimp": 1.1, "spicy": 1.5}
        factor = base_squish.get(dumpling_type, 1.0)
        return round(squish_power * factor, 2)

    @staticmethod
    def generate_race_lap_time(dumpling_type: str, squish_factor: float) -> float:
        base_time = 10.0
        variation = random.uniform(-2.0, 2.0)
        return round(base_time - (squish_factor * 0.5) + variation, 2)
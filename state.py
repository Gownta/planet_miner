from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Ore:
    name: str
    index: int
    price: float


@dataclass
class Planet:
    name: str
    purchase_cost: float

    # Location
    index: int
    distance: float
    telescope: int

    # Mining ratios. (X, Y) means X% of production is ore Y.
    # Sorted by ore index, ascending
    produce: List[Tuple[float, Ore]]

    # Main upgrades
    mining_level: int = 1
    shipping_level: int = 1
    cargo_level: int = 1

    # Colonization
    colonization_mining_level: int = 1
    colonization_shipping_level: int = 1
    colonization_cargo_level: int = 1

    def __post_init__(self):
        self.produce = sorted(self.produce, key=lambda x: -x[1].index)

    def output(self) -> List[Tuple[float, Ore]]:
        """
        Calculate the rate at which ores are shipped off the planet.

        Production is limited by shipping capacity. Higher-level ores
        (higher index) are prioritized when capacity is insufficient.
        """
        total_mining_rate = Planet.mining_speed(self.mining_level)
        shipping_capacity = Planet.ship_hz(self.shipping_level, self.distance) * Planet.ship_capacity(self.cargo_level)

        # Calculate production for each ore
        production = [(pct * total_mining_rate, ore) for pct, ore in self.produce]
        remaining = shipping_capacity
        for i in range(len(production)):
            amt = min(remaining, production[i][0])
            production[i][0] = amt
            remaining -= amt
        return production

    @staticmethod
    def mining_speed(level: int) -> float:
        return 0.25 + 0.1 * (level - 1) + 0.017 * (level - 1) ** 2

    @staticmethod
    def ship_hz(level: int, distance: float) -> float:
        speed = 1 + 0.2 * (level - 1) + (1 / 75) * (level - 1) ** 2
        return speed / distance

    @staticmethod
    def ship_capacity(level: int) -> int:
        result = 5 + 2 * (level - 1) + 0.1 * (level - 1) ** 2
        return round(result)

    @staticmethod
    def upgrade_cost(purchase_cost: int, level: int) -> float:
        """Calculate the cost to upgrade from level to level+1."""
        return (purchase_cost / 20) * (1.3 ** (level - 1))

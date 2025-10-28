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
    purchase_cost: int

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

    def output(self) -> List[Tuple[float, Ore]]:
        """
        Calculate the rate at which ores are shipped off the planet.

        Production is limited by shipping capacity. Higher-level ores
        (higher index) are prioritized when capacity is insufficient.
        """
        total_mining_rate = self.mining_speed()
        shipping_capacity = self.ship_hz() * self.ship_capacity()

        # Calculate production for each ore
        production = [(pct * total_mining_rate, ore) for pct, ore in self.produce]

        # Sort by ore index (descending) to prioritize higher-level ores
        production_sorted = reversed(production)

        # Allocate shipping capacity
        shipped = {}
        remaining_capacity = shipping_capacity

        for rate, ore in production_sorted:
            shipped_rate = min(rate, remaining_capacity)
            shipped[ore] = shipped_rate
            remaining_capacity -= shipped_rate

        # Return sorted by ore index (ascending)
        result = [(shipped[ore], ore) for _, ore in sorted(self.produce, key=lambda x: x[1].index)]

        return result

    def mining_speed(self) -> float:
        level = self.mining_level
        return 0.25 + 0.1 * (level - 1) + 0.017 * (level - 1) ** 2

    def ship_hz(self) -> float:
        level = self.shipping_level
        speed = 1 + 0.2 * (level - 1) + (1 / 75) * (level - 1) ** 2
        return speed / self.distance

    def ship_capacity(self) -> int:
        level = self.cargo_level
        result = 5 + 2 * (level - 1) + 0.1 * (level - 1) ** 2
        return round(result)

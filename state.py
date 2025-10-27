from dataclasses import dataclass, field


@dataclass
class Planet:
    name: str
    purchase_cost: int

    # Location
    index: int
    distance: float
    telescope: int

    # Mining ratios
    produce: list

    # Main upgrades
    mining_level: int = 1
    shipping_level: int = 1
    cargo_level: int = 1

    # Colonization
    colonization_mining_level: int = 1
    colonization_shipping_level: int = 1
    colonization_cargo_level: int = 1

    def output(self):
        pass

    def mining_speed(self) -> float:
        level = self.mining_level
        return 0.25 + 0.1 * (level - 1) + 0.017 * (level - 1) ** 2

    def ship_speed(self) -> float:
        level = self.shipping_level
        return 1 + 0.2 * (level - 1) + (1 / 75) * (level - 1) ** 2

    def ship_capacity(self) -> int:
        level = self.cargo_level
        result = 5 + 2 * (level - 1) + 0.1 * (level - 1) ** 2
        return round(result)


@dataclass
class Ore:
    name: str
    price: float

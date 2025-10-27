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


@dataclass
class Ore:
    name: str
    price: float

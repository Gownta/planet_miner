from state import Planet


def best_shipping_upgrade(shipping_level: int, cargo_level: int) -> str:
    """
    Determine whether to upgrade shipping or cargo for best cost efficiency.

    Returns 'shipping' or 'cargo' based on which upgrade provides the best
    increase in (ship_hz * ship_capacity) per unit cost.
    """

    def rate(shipping_level: int, cargo_level: int) -> float:
        return Planet.ship_hz(shipping_level, 1) * Planet.ship_capacity(cargo_level)

    curr = rate(shipping_level, cargo_level)

    ship_cost = Planet.upgrade_cost(1, shipping_level)
    ship_new = rate(shipping_level + 1, cargo_level)
    ship_lift = ship_new - curr
    ship_efficiency = ship_lift / ship_cost

    cargo_cost = Planet.upgrade_cost(1, cargo_level)
    cargo_new = rate(shipping_level, cargo_level + 1)
    cargo_lift =cargo_new - curr
    cargo_efficiency = cargo_lift / cargo_cost

    if ship_efficiency > cargo_efficiency:
        return (1, 0)
    return (0, 1)

    cargo_cost = Planet.upgrade_cost(1, cargo_level)
    cargo_bonus = rate(shipping_level, cargo_level + 1)

    if ship_bonus / ship_cost > cargo_bonus / cargo_cost:
        return (1, 0)
    return (0, 1)

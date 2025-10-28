from state import Planet


def best_shipping_upgrade(shipping_level: int, cargo_level: int) -> str:
    """
    Determine whether to upgrade shipping or cargo for best cost efficiency.
    Returns (1, 0) if shipping is better, or (0, 1) for cargo
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


def simulate_upgrades():
    """
    Starting at (1, 1), iteratively upgrade shipping or cargo based on
    best_shipping_upgrade for 100 iterations, printing levels each time.
    """
    shipping_level = 1
    cargo_level = 1

    print(f"({shipping_level}, {cargo_level})")

    for _ in range(100):
        ship_upgrade, cargo_upgrade = best_shipping_upgrade(shipping_level, cargo_level)
        shipping_level += ship_upgrade
        cargo_level += cargo_upgrade
        print(f"({shipping_level}, {cargo_level})")



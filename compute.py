from state import Planet
from data import PLANETS


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

    print(f"{shipping_level - cargo_level:+d} ({shipping_level}, {cargo_level})")

    for _ in range(50):
        # Do two upgrades
        ship_upgrade, cargo_upgrade = best_shipping_upgrade(shipping_level, cargo_level)
        shipping_level += ship_upgrade
        cargo_level += cargo_upgrade

        ship_upgrade, cargo_upgrade = best_shipping_upgrade(shipping_level, cargo_level)
        shipping_level += ship_upgrade
        cargo_level += cargo_upgrade

        print(f"{shipping_level - cargo_level:+d} ({shipping_level}, {cargo_level})")


def planet_upgrade_efficiency(planet: Planet, mining_level: int) -> float:
    """
    Calculate the efficiency of upgrading a planet's mining level.

    Returns the ratio of production increase to upgrade cost.
    Production is calculated as produce * mining_speed, ignoring shipping.
    """
    cost = Planet.upgrade_cost(planet.purchase_cost, mining_level)

    speed1 = Planet.mining_speed(mining_level)
    speed2 = Planet.mining_speed(mining_level + 1)
    speed_delta = speed2 - speed1

    # Calculate weighted average value of production
    # For each (pct, ore), multiply pct by the ore's price
    weighted_value = sum(pct * ore.price for pct, ore in planet.produce)

    # Multiply by speed_delta to get the value delta
    value_delta = weighted_value * speed_delta

    # Divide value delta by cost to get efficiency ratio
    return value_delta / cost



def balance_planets(p1: Planet, p2: Planet):
    """
    Balance two planets by iteratively upgrading the more efficient one.
    """
    # Start at mining_level 10 for each planet
    p1_mining_level = 10
    p2_mining_level = 10

    for _ in range(30):
        # Determine which planet is more efficient to upgrade
        p1_efficiency = planet_upgrade_efficiency(p1, p1_mining_level)
        p2_efficiency = planet_upgrade_efficiency(p2, p2_mining_level)

        # Upgrade the more efficient planet's mining_level
        if p1_efficiency > p2_efficiency:
            p1_mining_level += 1
        else:
            p2_mining_level += 1

        # Only print once each planet has been upgraded at least once
        if p1_mining_level > 10 and p2_mining_level > 10:
            # Print the two mining levels with delta
            delta = p1_mining_level - p2_mining_level
            print(f"{p1.name} {p2.name} {p1_mining_level} {p2_mining_level} {delta:+d}")


def balance_planet_pair(i: int):
    """
    Get planets indexed by i and i+1, then pass them to balance_planets.
    """
    planets_list = list(PLANETS)
    p1 = planets_list[i].value
    p2 = planets_list[i + 1].value
    balance_planets(p1, p2)


if __name__ == "__main__":
    balance_planet_pair(1)


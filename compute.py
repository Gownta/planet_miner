import sys
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



def balance_planets(p1: Planet, p2: Planet) -> tuple[int, int]:
    """
    Balance two planets by iteratively upgrading the more efficient one.
    Returns the minimum and maximum deltas between iterations 20 and 50.
    """
    # Start at mining_level 10 for each planet
    p1_mining_level = 10
    p2_mining_level = 10
    deltas = []

    for i in range(50):
        # Determine which planet is more efficient to upgrade
        p1_efficiency = planet_upgrade_efficiency(p1, p1_mining_level)
        p2_efficiency = planet_upgrade_efficiency(p2, p2_mining_level)

        # Upgrade the more efficient planet's mining_level
        if p1_efficiency > p2_efficiency:
            p1_mining_level += 1
        else:
            p2_mining_level += 1

        # Collect deltas between iterations 20 and 50
        if i >= 20:
            delta = p1_mining_level - p2_mining_level
            deltas.append(delta)

    return min(deltas), max(deltas)


def balance_planet_pair(i: int):
    """
    Get planets indexed by i and i+1, then pass them to balance_planets.
    Print the planet names and the min-max range of their level differences.
    """
    planets_list = list(PLANETS)
    p1 = planets_list[i].value
    p2 = planets_list[i + 1].value
    min_delta, max_delta = balance_planets(p1, p2)
    print(f"{p1.name} {p2.name} {min_delta:+d} {max_delta:+d}")


def balance_all_planets(n: int):
    """
    Call balance_planet_pair for each index from 0 to n.
    """
    for i in range(n + 1):
        balance_planet_pair(i)


def balorian(level: int, n: int):
    """
    For BALOR mining levels 1 through level, and for the first n planets,
    find the mining level where each planet becomes more efficient than BALOR.
    Output as a matrix where rows are planets and columns are BALOR levels.
    """
    planets_list = list(PLANETS)
    balor = planets_list[0].value

    # Print header row with BALOR levels
    print("Planet", end="")
    for balor_level in range(1, level + 1):
        print(f"\t{balor_level}", end="")
    print()

    # For each planet
    for i in range(n):
        planet = planets_list[i].value
        print(f"{planet.name}", end="")

        # For each BALOR level
        for balor_level in range(1, level + 1):
            balor_efficiency = planet_upgrade_efficiency(balor, balor_level)

            # Find the mining level where this planet becomes more efficient than BALOR
            planet_level = 1
            while planet_upgrade_efficiency(planet, planet_level) >= balor_efficiency:
                planet_level += 1

            print(f"\t{planet_level - 1}", end="")

        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compute.py <level>")
        sys.exit(1)

    level = int(sys.argv[1])
    balorian(level, 25)


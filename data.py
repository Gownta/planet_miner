from enum import Enum

from state import Ore, Planet

class PLANETS(Enum):
    BALOR = Planet(name="Balor", purchase_cost=100)
    DRASTA = Planet(name="Drasta", purchase_cost=200)
    ANADIUS = Planet(name="Anadius", purchase_cost=500)
    DHOLEN = Planet(name="Dholen", purchase_cost=1_250)
    VERR = Planet(name="Verr", purchase_cost=5_000)
    NEWTON = Planet(name="Newton", purchase_cost=9_000)
    WIDOW = Planet(name="Widow", purchase_cost=15_000)
    ACHERON = Planet(name="Acheron", purchase_cost=25_000)
    YANGTZE = Planet(name="Yangtze", purchase_cost=40_000)
    SOLVEIG = Planet(name="Solveig", purchase_cost=75_000)
    IMIR = Planet(name="Imir", purchase_cost=150_000)
    RELIC = Planet(name="Relic", purchase_cost=250_000)
    NITH = Planet(name="Nith", purchase_cost=400_000)
    BATALLA = Planet(name="Batalla", purchase_cost=800_000)
    MICAH = Planet(name="Micah", purchase_cost=1_500_000)
    PRANAS = Planet(name="Pranas", purchase_cost=3_000_000)
    CASTELLUS = Planet(name="Castellus", purchase_cost=6_000_000)
    GORGON = Planet(name="Gorgon", purchase_cost=12_000_000)
    PARNITHA = Planet(name="Parnitha", purchase_cost=25_000_000)
    ORISONI = Planet(name="Orisoni", purchase_cost=50_000_000)
    THESEUS = Planet(name="Theseus", purchase_cost=100_000_000)
    ZELENE = Planet(name="Zelene", purchase_cost=200_000_000)
    HAN = Planet(name="Han", purchase_cost=400_000_000)
    STRENNUS = Planet(name="Strennus", purchase_cost=800_000_000)
    OSUN = Planet(name="Osun", purchase_cost=1_600_000_000)
    PLOITARI = Planet(name="Ploitari", purchase_cost=3_200_000_000)
    ELYSTA = Planet(name="Elysta", purchase_cost=6_400_000_000)
    TIKKUUN = Planet(name="Tikkuun", purchase_cost=12_500_000_000)
    SATENT = Planet(name="Satent", purchase_cost=25_000_000_000)
    URLA = Planet(name="Urla", purchase_cost=50_000_000_000)
    RAST = Planet(name="Rast", purchase_cost=100_000_000_000)
    VULAR = Planet(name="Vular", purchase_cost=250_000_000_000)
    NIBIRU = Planet(name="Nibiru", purchase_cost=600_000_000_000)
    XENA = Planet(name="Xena", purchase_cost=1_500_000_000_000)
    RUPERT = Planet(name="Rupert", purchase_cost=4_000_000_000_000)
    PAX = Planet(name="Pax", purchase_cost=10_000_000_000_000)
    IVYRA = Planet(name="Ivyra", purchase_cost=25_000_000_000_000)
    UTRITS = Planet(name="Utrits", purchase_cost=62_000_000_000_000)
    DOOSIE = Planet(name="Doosie", purchase_cost=160_000_000_000_000)
    ZULU = Planet(name="Zulu", purchase_cost=400_000_000_000_000)
    UNICAE = Planet(name="Unicae", purchase_cost=1_000_000_000_000_000)
    DUNE = Planet(name="Dune", purchase_cost=2_500_000_000_000_000)
    NARAKA = Planet(name="Naraka", purchase_cost=6_200_000_000_000_000)
    DAEDALUS = Planet(name="Daedalus", purchase_cost=15_000_000_000_000_000)
    CLOVIS = Planet(name="Clovis", purchase_cost=40_000_000_000_000_000)
    ZERO = Planet(name="Zero", purchase_cost=100_000_000_000_000_000)
    SOTOMI = Planet(name="Sotomi", purchase_cost=100_000_000_000_000_000)

ORES = [
    Ore(name="Copper", price=1.80),
    Ore(name="Iron", price=3.60),
    Ore(name="Lead", price=5.60),
    Ore(name="Silica", price=17.60),
    Ore(name="Aluminium", price=23.80),
    Ore(name="Silver", price=64.80),
    Ore(name="Gold", price=105.00),
    Ore(name="Diamond", price=192.00),
    Ore(name="Platinium", price=340.00),
    Ore(name="Titanium", price=730.00),
    Ore(name="Iridium", price=1_600.00),
    Ore(name="Paladium", price=3_500.00),
    Ore(name="Osmium", price=7_800.00),
    Ore(name="Rhodium", price=17_500.00),
    Ore(name="Inerton", price=40_000.00),
    Ore(name="Quadium", price=92_000.00),
    Ore(name="Scrith", price=215_000.00),
    Ore(name="Uru", price=510_000.00),
    Ore(name="Vibranium", price=1_250_000.00),
    Ore(name="Aether", price=3_200_000.00),
]

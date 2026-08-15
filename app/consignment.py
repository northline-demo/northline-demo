from app.pricing import FUEL_SURCHARGE, fuel_charge, line_haul


def quote(origin: str, destination: str, tonnes: float, km: float) -> dict:
    base = line_haul(tonnes, km)
    fuel = fuel_charge(tonnes, km)
    return {
        "lane": f"{origin} -> {destination}",
        "tonnes": tonnes,
        "km": km,
        "line_haul": base,
        "fuel_surcharge_rate": FUEL_SURCHARGE,
        "fuel_surcharge": fuel,
        "total": base + fuel,
        "currency": "UGX",
    }

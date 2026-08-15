"""Freight pricing rules for Northline.

CODEOWNERS protects this file: every change needs an internal reviewer.
One wrong number here and every quote the company issues is wrong.
"""

# Fuel surcharge, applied to the line-haul rate.
# Reviewed whenever the pump price moves. Board-approved.
FUEL_SURCHARGE = 0.12

# Base line-haul rate, UGX per tonne per kilometre.
RATE_PER_TONNE_KM = 950


def line_haul(tonnes: float, km: float) -> int:
    """Base freight charge before surcharges."""
    return round(tonnes * km * RATE_PER_TONNE_KM)


def fuel_charge(tonnes: float, km: float) -> int:
    """Fuel surcharge payable on the line haul."""
    return round(line_haul(tonnes, km) * FUEL_SURCHARGE)

from app.consignment import quote
from app.pricing import FUEL_SURCHARGE, fuel_charge, line_haul

# The surcharge Northline's board signed off. If the code and this
# number disagree, the build goes red and nothing reaches production.
APPROVED_SURCHARGE = 0.12

# Reference lane: Kampala -> Gulu, 12 tonnes, 340 km.
TONNES, KM = 12, 340


def test_surcharge_matches_approved_rate():
    assert FUEL_SURCHARGE == APPROVED_SURCHARGE


def test_line_haul_reference_lane():
    assert line_haul(TONNES, KM) == 3_876_000


def test_fuel_charge_reference_lane():
    assert fuel_charge(TONNES, KM) == 465_120


def test_quote_adds_up():
    q = quote("Kampala", "Gulu", TONNES, KM)
    assert q["total"] == q["line_haul"] + q["fuel_surcharge"]
    assert q["currency"] == "UGX"

def margin_check(load):
    margin = load.customer_rate - load.carrier_rate
    if margin < 150:
        return ("LOW_MARGIN", "HIGH")
    return None


def negative_margin(load):
    if load.customer_rate < load.carrier_rate:
        return ("NEGATIVE_MARGIN", "CRITICAL")
    return None


def rate_per_mile_check(load):
    rpm = load.customer_rate / max(load.miles, 1)
    if rpm < 1.0:
        return ("LOW_RPM_POSSIBLE_TYPO", "HIGH")
    return None


def new_mc_high_value(load):
    high_value = load.commodity.lower() in ["electronics", "pharmaceuticals"]
    if load.carrier_mc_age_days < 30 and high_value:
        return ("NEW_MC_HIGH_VALUE", "CRITICAL")
    return None


def overweight_check(load):
    if load.equipment.lower() == "dry van" and load.weight > 45000:
        return ("DRY_VAN_OVERWEIGHT", "HIGH")
    return None


RULES = [
    margin_check,
    negative_margin,
    rate_per_mile_check,
    new_mc_high_value,
    overweight_check,
]
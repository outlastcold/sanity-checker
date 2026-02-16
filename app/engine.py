from .rules import RULES

def evaluate_load(load):
    flags = []

    for rule in RULES:
        result = rule(load)
        if result:
            flags.append({
                "type": result[0],
                "severity": result[1]
            })

    risk_score = calculate_risk_score(flags)

    return {
        "risk_score": risk_score,
        "flags": flags,
        "recommendation": recommendation(risk_score)
    }


def calculate_risk_score(flags):
    score = 0
    for f in flags:
        if f["severity"] == "CRITICAL":
            score += 40
        elif f["severity"] == "HIGH":
            score += 20
        elif f["severity"] == "MEDIUM":
            score += 10
    return min(score, 100)


def recommendation(score):
    if score >= 70:
        return "REVIEW BEFORE TENDER"
    elif score >= 40:
        return "DOUBLE CHECK LOAD DETAILS"
    return "LOAD LOOKS OK"
Sanity Checker API

Rule-based freight load risk flagging API built with FastAPI.

Problem

Small freight brokerages often rely on manual checks to catch risky loads.
This leads to preventable losses from:

Low margins

Data entry errors

Overweight shipments

Fraud-prone carrier selections

Sanity Checker evaluates a load and returns risk flags with a recommendation before the load is tendered.

Features

Margin risk detection

Negative margin detection

Low rate-per-mile typo detection

New MC + high-value commodity fraud risk

Dry van overweight detection

Risk scoring with recommendation

Auto-generated Swagger docs

Tech Stack

Python

FastAPI

Uvicorn

Pydantic

Run locally
1. Create virtual environment
python -m venv venv
.\venv\Scripts\activate
2. Install dependencies
pip install fastapi uvicorn
3. Run the API
uvicorn app.main:api --reload

Open Swagger:
http://127.0.0.1:8000/docs

Example Request

POST /check_load

{
  "origin": "Atlanta, GA",
  "destination": "Dallas, TX",
  "miles": 781,
  "customer_rate": 1000,
  "carrier_rate": 950,
  "equipment": "Dry Van",
  "weight": 47000,
  "pickup_date": "2026-02-16",
  "delivery_date": "2026-02-17",
  "commodity": "Electronics",
  "new_carrier": true,
  "carrier_mc_age_days": 12
}
Example Response
{
  "risk_score": 80,
  "flags": [
    { "type": "LOW_MARGIN", "severity": "HIGH" },
    { "type": "NEW_MC_HIGH_VALUE", "severity": "CRITICAL" },
    { "type": "DRY_VAN_OVERWEIGHT", "severity": "HIGH" }
  ],
  "recommendation": "REVIEW BEFORE TENDER"
}
Roadmap

Transit time feasibility rule

Margin percentage thresholds

Batch load evaluation endpoint

Configurable rules via JSON
Margin percentage thresholds

Batch load evaluation endpoint

Configurable rules via JSON

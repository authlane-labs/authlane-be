from datetime import datetime

EVENTS = [
    {"id": "evt-1", "title": "phone verification", "status": "requested", "severity": "high", "updatedAt": datetime.utcnow().date().isoformat()},
    {"id": "evt-2", "title": "refresh token hardening", "status": "approved", "severity": "medium", "updatedAt": datetime.utcnow().date().isoformat()},
]

METRICS = [
    {"key": "signin_success_rate", "label": "signin success rate", "value": 184, "unit": "ms", "target": 220},
    {"key": "refresh_retry_rate", "label": "refresh retry rate", "value": 92, "unit": "%", "target": 90},
    {"key": "phone_token_reuse_blocks", "label": "phone token reuse blocks", "value": 37, "unit": "events", "target": 30},
]

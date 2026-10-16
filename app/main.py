from fastapi import FastAPI
from app.models import Lead, ProcessedLead

app = FastAPI(title="Lead Qualification Automation API", version="1.0.0", description="A sample Python/FastAPI lead validation and CRM-ready data processing service.")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/leads/process", response_model=ProcessedLead)
def process_lead(lead: Lead) -> ProcessedLead:
    """Validate and score an incoming lead; generate a CRM-ready payload (no external requests)."""
    score = 20
    score += 30 if lead.interested_in in {"automation", "ai-agent", "crm"} else 0
    score += 30 if lead.employees >= 20 else (15 if lead.employees >= 5 else 0)
    score += 20 if lead.phone else 0
    priority = "high" if score >= 80 else "medium" if score >= 50 else "low"
    tags = [f"interest:{lead.interested_in}", f"priority:{priority}"]
    crm_payload = {
        "full_name": lead.name,
        "email": str(lead.email),
        "company": lead.company,
        "phone": lead.phone,
        "tags": tags,
        "custom_fields": {"employee_count": lead.employees, "lead_score": score, "notes": lead.notes},
    }
    return ProcessedLead(name=lead.name, email=lead.email, company=lead.company, phone=lead.phone, score=score, priority=priority, tags=tags, crm_payload=crm_payload)

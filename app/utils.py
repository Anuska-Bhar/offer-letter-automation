from datetime import datetime, timedelta

def compute_dates(joining_date_str):
    if not joining_date_str or not str(joining_date_str).strip():
        raise ValueError("joining_date is required and cannot be empty. Use format DD/MM/YYYY")

    try:
        joining = datetime.strptime(joining_date_str, "%d/%m/%Y")
    except ValueError as exc:
        raise ValueError("joining_date must be in format DD/MM/YYYY (e.g. 31/12/2026)") from exc
    
    onboarding_start = joining
    onboarding_end = joining + timedelta(days=9)
    probation_start = onboarding_end + timedelta(days=1)
    
    return {
        "date": datetime.today().strftime("%d/%m/%Y"),
        "onboarding_start": onboarding_start.strftime("%d/%m/%Y"),
        "onboarding_end": onboarding_end.strftime("%d/%m/%Y"),
        "probation_start": probation_start.strftime("%d/%m/%Y")
    }
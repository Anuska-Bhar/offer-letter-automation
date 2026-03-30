from datetime import datetime, timedelta

def compute_dates(joining_date_str):
    joining = datetime.strptime(joining_date_str, "%d/%m/%Y")
    
    onboarding_start = joining
    onboarding_end = joining + timedelta(days=9)
    probation_start = onboarding_end + timedelta(days=1)
    
    return {
        "date": datetime.today().strftime("%d/%m/%Y"),
        "onboarding_start": onboarding_start.strftime("%d/%m/%Y"),
        "onboarding_end": onboarding_end.strftime("%d/%m/%Y"),
        "probation_start": probation_start.strftime("%d/%m/%Y")
    }
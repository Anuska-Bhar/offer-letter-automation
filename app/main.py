from fastapi import FastAPI
from pydantic import BaseModel
from app.generator import generate_offer
from app.utils import compute_dates

app = FastAPI()

class Employee(BaseModel):
    template_key: str
    name: str
    position: str
    annual_salary_pa: str
    variable_pay_pa: str
    joining_date: str
    renumeration_sal: str
    renumeration_vp: str
    responsibilities: str

@app.post("/generate-offer-letter")
def generate(employee: Employee):
    data = employee.dict()
    
    computed = compute_dates(data["joining_date"])
    data.update(computed)
    
    output_file = generate_offer(data)
    
    return {"file": output_file}
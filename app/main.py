from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.generator import generate_offer
from app.utils import compute_dates
from app.logger import log

app = FastAPI()

class Employee(BaseModel):
    id: str
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
    try:
        data = employee.dict()

        computed = compute_dates(data["joining_date"])
        data.update(computed)

        file_path = generate_offer(data)

        return FileResponse(
            path=file_path,
            filename=file_path.split("/")[-1],
            media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        log(f"Generating offer letter for {data['name']}")
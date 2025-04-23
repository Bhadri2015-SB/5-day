from fastapi import FastAPI
from tasks import send_email_background

app = FastAPI()

@app.post("/send-email/")
async def trigger_email(email: str):
    task = send_email_background.delay(email)
    return {"message": f"Email to {email} scheduled!", "task_id": task.id}

from fastapi import FastAPI

app = FastAPI(
    title="DrivePass API",
    description="Fleet Management & Vehicle Subscription Platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "application": "DrivePass",
        "status": "Running",
        "version": "0.1.0"
    }
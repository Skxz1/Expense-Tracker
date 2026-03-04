# Import FastAPI framework
from fastapi import FastAPI

# Import a response class that lets us return HTML
from fastapi.responses import HTMLResponse

# Create the FastAPI application instance
# This object represents your entire web server
app = FastAPI(title="Expense Tracker")


# This decorator tells FastAPI:
# "Run this function when someone visits the '/' route"
@app.get("/", response_class=HTMLResponse)
def home() -> str:

    # This function returns HTML that will be shown in the browser
    return "<h1>Expense Tracker</h1>"


# A simple health check endpoint
# Many production systems use this to check if a service is alive
@app.get("/health")
def health() -> dict:

    # FastAPI automatically converts dictionaries to JSON
    return {"status": "ok"}

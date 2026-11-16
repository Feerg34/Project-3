import os
import requests
from dotenv import load_dotenv

load_dotenv()

CANVAS_URL = os.getenv("CANVAS_API_URL")
CANVAS_TOKEN = os.getenv("CANVAS_API_TOKEN")

if not CANVAS_URL or not CANVAS_TOKEN:
    raise ValueError("Missing Canvas configuration in .env")

url = f"{CANVAS_URL.rstrip('/')}/api/v1/calendar_events"

headers = {
    "Authorization": f"Bearer {CANVAS_TOKEN}"
}

params = {
    "type": "event",
    "context_codes[]": "course_15999",
    "per_page": 100,
    "start_date": "2026-01-01T00:00:00Z",
    "end_date": "2027-01-01T00:00:00Z"
}

try:
    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=20
    )

    print("HTTP Status:", response.status_code)

    response.raise_for_status()

    courses = response.json()

    print(f"\nFound {len(courses)} courses:\n")

    for course in courses:
        print("------------------------------")
        print("ID:", course.get("id"))
        print("Name:", course.get("name"))
        print("Course code:", course.get("course_code"))
        print("Status:", course.get("workflow_state"))

except requests.exceptions.HTTPError:
    print("Canvas returned an HTTP error.")
    print("Response:", response.text[:1000])

except requests.exceptions.RequestException as error:
    print("Connection error:", error)

from flask import Flask, render_template, request, jsonify
import os
import requests
from datetime import datetime, timedelta
import re

app = Flask(__name__)


# Course cache
course_cache = {}

#Weather cache
weather_cache = {}

# Route for the frontend
@app.route('/')
def index():
    return render_template("index.html")


# Function to standardize courses to a format with letters followed by 3 nums
def standardize_course(course):
    #course = request.form["course"]
    if not course:
        return None, 400
    #course = course.upper()
    pattern = re.compile(r'^([a-zA-Z]+)\s*(\d{3})$')
    match = pattern.match(course)
    if match:
        return match.groups(), 200
    else:
        return None, 400
    
#Course formatting helper

def format_course(course):
    pattern = re.compile(r'^([a-zA-Z]+)(\d{3})$')
    match = pattern.match(course)
    if match:
        course_dept, course_num = match.groups()
        return f"{course_dept} {course_num}"
    else:
        return course


# Calculate the next meeting
def calculate_next_meeting(meeting_days, start_time):
    if not meeting_days or not start_time:
        return None
    days_mapping = {"M": 0, "T": 1, "W": 2, "R": 3, "F": 4, "S": 5, "U": 6}
    meeting_days_numbers = [days_mapping[day] for day in meeting_days]
    now = datetime.now()
    for i in range(7):
        potential_meeting_day = (now + timedelta(days=i)).weekday()
        if potential_meeting_day in meeting_days_numbers:
            next_meeting_date = now.date() + timedelta(days=i)
            next_meeting = datetime.combine(next_meeting_date, start_time)
            if next_meeting > now:
                return next_meeting
    return None

#Function for weather forecast

def get_weather_forecast(course, date, next_meeting_time):
    if not date or not next_meeting_time:
        return None
    date_str = date.strftime("%Y-%m-%d")
    cache_key = f"{course}_{date_str}"
    if cache_key in weather_cache:
        return weather_cache[cache_key]
    else:
        url = f"https://api.weather.gov/gridpoints/ILX/96,72/forecast/hourly"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "N/A", "Forecast": "Forecast not available"}
        forecasts = response.json()["properties"]["periods"]
        for forecast in forecasts:
            forecast_start_time = datetime.strptime(forecast["startTime"], "%Y-%m-%dT%H:%M:%S%z")
            if forecast_start_time.date() == date and forecast_start_time.hour == next_meeting_time.hour:
                weather_cache[cache_key] = forecast
                return forecast
        for forecast in forecasts:
            forecast_start_time = datetime.strptime(forecast["startTime"], "%Y-%m-%dT%H:%M:%S%z")
            if forecast_start_time.date() == date:
                weather_cache[cache_key] = forecast
                return forecast
        return {"error": "N/A", "Forecast": "Forecast not available"}


# Route for "/weather"
@app.route('/weather', methods=["POST"])

def weather():
    return POST_weather()


def POST_weather():
  course = request.form["course"]

  # ...
  return "Not Implemented", 501


@app.route('/weatherCache')
def get_cached_weather():
    return jsonify(weather_cache), 200
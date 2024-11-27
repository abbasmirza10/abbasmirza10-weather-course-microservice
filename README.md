# Weather Course Microservice

## Overview
This project involves building a microservice that reports the weather for the next meeting of a given course. The service will interact with a provided course schedule microservice and the National Weather Service API to provide weather forecasts for course meeting times.

## Features
- **POST /weather**: Returns the weather forecast for the next meeting of a given course.
- **GET /weatherCache**: Returns the current state of the weather forecast cache.
- **Caching**: The service caches weather forecasts to avoid repeatedly querying the National Weather Service API for the same course.
- **Weather Data**: Uses the National Weather Service API to retrieve the weather forecast for a given time.

## Getting Started

### Prerequisites
- Python 3.x
- Install dependencies using `pip`:
  ```bash
  pip install -r requirements.txt
Running the Services
Run the Course Microservice: Navigate to the courses_microservice directory and start the course microservice:

bash
Copy code
cd courses_microservice
python3 schedules.py
The microservice should start and be accessible at http://localhost:34000.

Run Your Weather Microservice: Navigate to the project directory and run the weather microservice:

bash
Copy code
python3 classweather.py
The service will start running on http://localhost:5000.

Interacting with the Service
POST /weather: Send a POST request with a JSON body containing the course identifier (e.g., "CS 340") to get the weather for the next class meeting. Example:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"course": "CS 340"}' http://localhost:5000/weather
GET /weatherCache: Send a GET request to view the current weather cache. Example:

bash
Copy code
curl http://localhost:5000/weatherCache
Caching
The service caches weather forecasts for each course. If a course's weather has already been requested, it will return the cached forecast without querying the National Weather Service API again. This helps avoid hitting request limits.

Error Handling
If a course is not found in the schedule, a 400 status code with an error message is returned.
If weather data is unavailable for the course meeting time, the forecast will be marked as "forecast unavailable."
Testing
Running Automated Tests
Automated tests are provided and can be run using pytest:

bash
Copy code
python3 -m pytest
The tests validate that your microservice works correctly with different courses, including checking for valid forecasts and handling cache behavior.

Folder Structure
bash
Copy code
weather-course-microservice/
│
├── classweather.py               # Main service for handling weather requests
├── courses_microservice/         # Directory containing the course schedule microservice
├── requirements.txt              # List of dependencies
├── tests/                        # Folder for test cases
└── README.md                     # This file
License
This project is licensed under the MIT License - see the LICENSE file for details.

sql
Copy code

You can copy and paste this into your `README.md` for the weather-course-microservice project. It includes the necessary details without due dates and extra information.

# Api Recommendation for MovieLens 1 million records

This is an API REST developed in python that comes from a previous analysis via kmeans and collaborative filter recommendation. For accessing and using this endpoint, make sure to follow these steps.

## Installation

First of all, make sure to clone this project:

```bash
# Clone repository
git clone https://github.com/DanielJPC19/api-recommendation-ml-1m

# Enter the generated to folder
cd api-recommendation-ml-1m
```

Then, create a virtual environment and install the requirements:

```bash
# Create virtual environment with the name of .venv
python -m venv .venv

# Install requirements from requirements.txt
pip install -r requirements.txt
```

## Execution

From here, you have two endpoints, one that returns the whole recommendations, and the second that search a specific user:

```
# First endpoint
http://<IP or localhost>:8000/recommendations

# Second endpoint
http://<IP or localhost>:8000/recommendations/<userID>
```

Taking care of this, execute the API by using `uvicorn`, this is done by:

```bash
uvicorn main:app --reload
```

## Test the endpoints

From here, you can access the json from the browser, or by using `curl` as follow:

```bash
# Returns the recommendation for user with ID 1
curl http://localhost:8000/recommendations/1

# Returns the whole recommendations of every user
curl http://localhost:8000/recommendations
```

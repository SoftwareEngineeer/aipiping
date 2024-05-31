# FastAPI Travel Recommendations

This project is a FastAPI application that provides travel recommendations for a given country and season using the OpenAI GPT-3.5 API.

## Features

- Provides travel recommendations based on the country and season provided.
- Utilizes OpenAI's GPT-3.5 to generate recommendations.
- Implements CORS to allow requests from different origins.
- Securely handles API keys and sensitive data.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- OpenAI API key

## Setup

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/fastapi-travel-recommendations.git
cd fastapi-travel-recommendations
```


# Create and activate a virtual environment:

```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

# Install the required packages:
```bash
pip install -r requirements.txt
```

# Set up environment variables:
```bash
OPENAI_API_KEY=your_openai_api_key
```

# Run the application:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 3000
```


# Using Docker
## Build the docker image
```bash
docker build -t fastapi-travel-recommendations .
```
## Run the docker container
```bash
docker run -d --name fastapi-travel-recommendations -p 3000:3000 --env-file .env fastapi-travel-recommendations
```
The application will be available at http://127.0.0.1:3000.

## Endpoints
### GET /recommendations/
#### Parameters
- country (str): The country for which recommendations are needed.
- season (str): The season for recommendations. Must be one of summer, winter, spring, or autumn.

#### Example Request
```bash
curl "http://127.0.0.1:3000/recommendations/?country=Canada&season=winter"
```
#### Example Response
```json
{
  "country": "Canada",
  "season": "winter",
  "recommendations": [
    "Go skiing in Whistler.",
    "Experience the Northern Lights in Yukon.",
    "Visit the Quebec Winter Carnival."
  ]
}
```




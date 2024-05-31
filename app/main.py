from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the OpenAI client
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise RuntimeError("OpenAI API key is not set")

client = OpenAI(api_key=api_key)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel Recommendations API"}

@app.get("/recommendations/")
def get_recommendations(
    country: str = Query(..., description="The country for recommendations"),
    season: str = Query(..., description="The season for recommendations", pattern="^(summer|winter|spring|autumn)$")
):
    # Craft the prompt
    prompt = f"Provide three travel recommendations for things to do in {country} during the {season}."

    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        recommendations = response.choices[0].message.content.strip().split('\n')
        return {
            "country": country,
            "season": season,
            "recommendations": [rec.strip() for rec in recommendations if rec]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)

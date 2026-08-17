from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from recipe_scrapers import scrape_me
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/recipe")
def scrape_recipe(url: str):
    try:
        scraper = scrape_me(url)
        return {
            "title": scraper.title(),
            "ingredients": [{"name": ing, "qty": 1} for ing in scraper.ingredients()],
            "instructions": scraper.instructions(),
            "image": scraper.image(),
            "time": f"{scraper.total_time()} mins" if scraper.total_time() else "Unknown time"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

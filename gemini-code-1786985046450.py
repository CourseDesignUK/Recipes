from recipe_scrapers import scrape_me

# Provide the URL of the BBC Good Food recipe
scraper = scrape_me("https://www.bbcgoodfood.com/recipes/classic-cottage-pie")

# Extract structured data
title = scraper.title()
ingredients = scraper.ingredients()
instructions = scraper.instructions()
image_url = scraper.image()
prep_time = scraper.prep_time()
cost_metrics = scraper.nutrients() # Depending on the site schema

print(scraper.to_json()) # Returns complete recipe dictionary
import os
import requests
import pandas as pd
from geopy.distance import geodesic
from llama_index.experimental import PandasQueryEngine
from dotenv import load_dotenv

load_dotenv()

class CoffeeScraper:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")
        self.gallery_coords = (45.4299, -75.6939)
        self.df = pd.DataFrame(columns=[
            "name", "address", "price_level",
            "rating", "distance_km", "scraped_at"
        ])

    def scrape_nearby_coffee(self):
        params = {
            "engine": "google_maps",
            "q": "coffee shops near National Gallery of Canada",
            "type": "search",
            "hl": "en",
            "api_key": self.api_key
        }

        response = requests.get("https://serpapi.com/search", params=params)

        if response.status_code != 200:
            print(f"SerpAPI error: {response.text}")
            return

        results = response.json().get("local_results", [])

        for place in results:
            coords = (
                place.get("gps_coordinates", {}).get("latitude"),
                place.get("gps_coordinates", {}).get("longitude")
            )

            if None in coords:
                continue

            distance = round(geodesic(self.gallery_coords, coords).km, 2)

            self.df = pd.concat([self.df, pd.DataFrame([{
                "name": place.get("title"),
                "address": place.get("address"),
                "price_level": len(place.get("price", "")),
                "rating": place.get("rating"),
                "distance_km": distance,
                "scraped_at": pd.Timestamp.now()
            }])], ignore_index=True)

        print(f"Successfully scraped {len(self.df)} coffee shops.")

    def get_query_engine(self):
        return PandasQueryEngine(
            df=self.df,
            verbose=True,
            instruction_str=(
                "You are a coffee shop analyst. Use this data to answer questions "
                "about coffee shops near National Gallery of Canada. "
                "Key fields: name, price_level ($1-3), rating (1-5), distance_km."
            )
        )


coffee_scraper = CoffeeScraper()

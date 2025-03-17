import scrapy
import requests
import json

class AirbnbSpider(scrapy.Spider):
    name = "airbnb_spider"
    allowed_domains = ["airbnb.com"]
    start_urls = ["https://www.airbnb.com/s/London--United-Kingdom/homes"] 

    def parse(self, response):
        listings = response.css(".listing-card-wrapper")

        for listing in listings:
            data = {
                "title": listing.css("._gjfol0::text").get(),
                "location": listing.css("._1tanv1h::text").get(),
                "price_per_night": listing.css("._tyxjp1::text").re_first(r"\d+"),
                "ratings": listing.css("._1bbeetd span::text").get(),
                "reviews": listing.css("._1bbeetd::text").re_first(r"\d+"),
                "amenities": ["WiFi", "Kitchen"],  
                "image_urls": listing.css("img::attr(src)").getall(),
            }

            self.send_to_backend(data)

    def send_to_backend(self, data):
        url = "http://localhost:8000/api/listings/"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        print(response.json())

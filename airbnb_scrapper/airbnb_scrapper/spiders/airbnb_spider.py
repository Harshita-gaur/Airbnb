import scrapy
import requests
import json

class AirbnbSpider(scrapy.Spider):
    name = "airbnb_spider"
    allowed_domains = ["airbnb.com"]
    start_urls = ["https://www.airbnb.com/s/London--United-Kingdom/homes"] 

    def parse(self, response):
        listings = response.css("div._8s3ctt")
        for listing in listings:
            data = {
                "title": listing.css("._1whrsux9::text").get(),
                "location": listing.css("._167qordg::text").get(),
                "price_per_night": listing.css("._tyxjp1::text").re_first(r"\d+"),
                "ratings": listing.css("._10fy1f8::text").get(),
                "reviews": listing.css("._a7a5sx::text").re_first(r"\d+"),
                "image": listing.css("img._6tbg2q::attr(src)").getall(),
            }
            response = requests.post(
                "http://localhost:8000/api/listings/",
                json=data,
                headers={"Content-Type": "application/json"},
            )
            print(response.json())


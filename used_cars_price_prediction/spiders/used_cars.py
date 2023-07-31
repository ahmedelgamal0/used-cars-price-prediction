import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UsedCarsSpider(CrawlSpider):
    name = "used_cars"
    allowed_domains = ["www.dubizzle.com.eg"]
    start_urls = ["https://www.dubizzle.com.eg/en/vehicles/cars-for-sale"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='a52608cc']/a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@title='Next']/parent::node()"))
        )

    def parse_item(self, response):
        price = response.xpath("(//div[@aria-label='Overview']/div/div/div/span)[1]/text()").get()
        location = response.xpath("(//div[@aria-label='Overview']/div/div/div/span)[2]/text()").get()

        details_div = response.xpath("//div[@aria-label='Details']")

        before = './/span[text()="'
        after = '"]/following-sibling::span/text()'

        brand = details_div.xpath(f"{before}Brand{after}").get()
        model = details_div.xpath(f"{before}Model{after}").get()
        condition =  details_div.xpath(f"{before}Condition{after}").get()
        fuel_type = details_div.xpath(f"{before}Fuel Type{after}").get()
        year = details_div.xpath(f"{before}Year{after}").get()
        transmission_type = details_div.xpath(f"{before}Transmission Type{after}").get()
        color = details_div.xpath(f"{before}Color{after}").get()
        body_type = details_div.xpath(f"{before}Body Type{after}").get()
        km = details_div.xpath(f"{before}Kilometers{after}").get()
        engine_capacity = details_div.xpath(f"{before}Engine Capacity (CC){after}").get()


        yield {
            'brand' : brand,
            'model' : model,            
            'condition' : condition,
            'year' : year,
            'color' :color,
            'body_type' : body_type,
            'fuel_type' : fuel_type,
            'transmission_type' : transmission_type,
            'engine_capacity' : engine_capacity,
            'location' : location,
            'km' : km,
            'price' : price            
        }

       
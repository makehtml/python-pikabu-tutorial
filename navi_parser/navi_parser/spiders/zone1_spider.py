import scrapy


class Zone1Spider(scrapy.Spider):
    name = "zone1"

    def start_requests(self):
        url = 'https://www.admiralty.co.uk/maritime-safety-information/radio-navigational-warnings/low-bandwidth/navarea-1'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for tr in response.css('.radio-navigational-warning-table tbody tr'):
            if tr.css('.optional-column::text').get():
                # TODO: привести к Date .parse()
                date = tr.css('.optional-column + td::text').get()
                yield {
                    'id': tr.css('.optional-column::text').get(),
                    'date': date,
                    'title': tr.css('.optional-column + td + td::text').get(),
                    # 'area': response.css('div.ExternalClassE94DAD22C5514EC681C0E7A85F785CFB::text').get()[0],
                    # 'description': response.css('div.ExternalClassE94DAD22C5514EC681C0E7A85F785CFB::text').get()[3][4]
                }
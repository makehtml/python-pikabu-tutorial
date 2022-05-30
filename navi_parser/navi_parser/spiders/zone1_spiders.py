import scrapy


class Zone1Spider(scrapy.Spider):
    name = "zone1"

    def start_requests(self):
        urls = [
            # 'https://armada.defensa.gob.es/ihm/Aplicaciones/Navareas/Index_Navareas_xml_en.html',
         'https://www.admiralty.co.uk/maritime-safety-information/radio-navigational-warnings/low-bandwidth/navarea-1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield{
            'id': response.css('td.optional-column::text').get(),
            'date': response.css('h3.accordion-content-cell::text').get(),
            'area': response.css('div.ExternalClassE94DAD22C5514EC681C0E7A85F785CFB::text').get()[0],
            'title': response.css('div.ExternalClassE94DAD22C5514EC681C0E7A85F785CFB::text').get()[1],
            'description': response.css('div.ExternalClassE94DAD22C5514EC681C0E7A85F785CFB::text').get()[3][4]
        }

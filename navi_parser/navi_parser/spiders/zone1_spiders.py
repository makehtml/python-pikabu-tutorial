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
        id = response.xpath('/html/body/form/div[4]/div/div/div/main/div/span/article/div/div[2]/div[2]/div[1]/div/div/div/div[1]/table/tbody/tr[1]/td[2]/text()')
        date = response.xpath('//*[@id="ctl00_ctl39_g_7a56dbd8_1bd3_49a5_8f17_204f53697688"]/table/tbody/tr[1]/td[3]/text()')
        area = response.xpath('//*[@id="fa3ed36a-fd5c-4d47-b282-6cb1ed8bb870"]/td[3]/div/div[1]/text()')
        title = response.xpath('//*[@id="fa3ed36a-fd5c-4d47-b282-6cb1ed8bb870"]/td[3]/div/div[2]/text()')
        description = response.xpath('//*[@id="fa3ed36a-fd5c-4d47-b282-6cb1ed8bb870"]/td[3]/div/div[4]/text(), //*[@id="fa3ed36a-fd5c-4d47-b282-6cb1ed8bb870"]/td[3]/div/div[5]/text()')


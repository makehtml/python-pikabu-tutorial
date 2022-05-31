"""
Here should be described zone3_spider.py
"""

import scrapy


class Zone3Spider(scrapy.Spider):
    name = "zone3"

    def start_requests(self):
        urls = [
            # 'https://armada.defensa.gob.es/ihm/Aplicaciones/Navareas/Index_Navareas_xml_en.html',
            'https://armada.defensa.gob.es/ihm/XML/Index_navareas_eng.xml'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for warning in response.css('navarea'):
            yield {
                'id': warning.attrib['id_nav'],
                'date': warning.attrib['fecha_emi'],
                'area': warning.attrib['loca'].capitalize(),
                'title': warning.attrib['asunto'].capitalize(),
                'description': warning.css('::text').get().replace('<br />', '\n')
            }

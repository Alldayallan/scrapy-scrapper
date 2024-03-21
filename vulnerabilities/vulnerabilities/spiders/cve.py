import scrapy
import os
import csv

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, "source-EXPLOIT-DB.html")

class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    start_urls = [f"file://{url}"]

    def parse(self, response):
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 100:
                table = child
                break
        
        count = 0
        csv_file = open ('vulnerabilites.csv', 'w')
        writer = csv.writer(csv_file)
        writer.writerow(['exploit id', 'cve id'])
        for row in table.xpath('//tr'):
            if count > 100:
                break
            try:
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                writer.writerow([exploit_id, cve_id])
                count += 1
            except IndexError:
                pass
            csv_file.close()

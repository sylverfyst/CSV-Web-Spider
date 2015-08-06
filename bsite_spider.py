from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.utils.markup import remove_tags
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from tutorial.items import BSiteItem
import csv

class BsiteSPider(CrawlSpider):
	name = "Bsite"
	l= []
	my_file = open("aerospace.csv", "rb")
	reader = csv.reader(my_file)
	
	for row in reader:
		l.append(row)
		print l[0]
	start_urls = l[0]
	allowed_domains = l[0]
	download_delay = 1
	rules = [Rule(SgmlLinkExtractor(allow=('.+')), follow=True, callback='parse_item')]
    
	def parse_item(self, response):
		text = Selector(response).xpath("//body//text()").re('(\w+)')
		
		for text in text:
			newtext = text.encode('utf8')
			hxs = HtmlXPathSelector(response)
			item = BSiteItem()
			if newtext == 'aerospace' or newtext == 'Aerospace' or newtext == 'AEROSPACE':
				print 'True'
				test = response.url
				print test
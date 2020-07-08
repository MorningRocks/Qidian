import scrapy
from qidian_spider.items import QidianSpiderItem
class Qidian100spider(scrapy.Spider):
    name = 'qidian_100_spider'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/rank/fengyun']
    n = 1
    def parse(self, response):
        book_list = response.xpath('//div[@class="book-img-text"]/ul/li')
        print("小说个数",len(book_list))

        for i_item in book_list:
            qidianSpiderItem = QidianSpiderItem()
            qidianSpiderItem['a_book_number'] = i_item.xpath('./div[@class="book-img-box"]/span/text()').extract()
            qidianSpiderItem['f_book_link'] = i_item.xpath('./div[@class="book-img-box"]/a/@href').extract()
            qidianSpiderItem['b_book_name'] = i_item.xpath('./div[@class="book-mid-info"]/h4/a/text()').extract()
            qidianSpiderItem['c_author'] = i_item.xpath('./div[@class="book-mid-info"]/p[@class="author"]/a[1]/text()').extract()
            qidianSpiderItem['d_book_type'] = i_item.xpath('./div[@class="book-mid-info"]/p[@class="author"]/a[2]/text()').extract()
            qidianSpiderItem['e_condition'] = i_item.xpath('./div[@class="book-mid-info"]/p[@class="author"]/span/text()').extract()
            qidianSpiderItem['i_intro'] = i_item.xpath('normalize-space(./div[@class="book-mid-info"]/p[@class="intro"]/text())').extract()
            qidianSpiderItem['g_update_info'] = i_item.xpath('./div[@class="book-mid-info"]/p[@class="update"]/a/text()').extract()
            qidianSpiderItem['h_up_time'] = i_item.xpath('./div[@class="book-mid-info"]/p[@class="update"]/span/text()').extract()

            #print(qidianSpiderItem)
            yield qidianSpiderItem
        # #解析下一页
        # next_link = response.xpath('//div[class="lbf-pagination"]/ul[@class="lbf-pagination-item-list"]/li[7]/a/@href').extract()
        # if next_link:
        #     next_link = next_link[0]
        #     yield scrapy.Request('https://www.qidian.com/rank/fengyun'+next_link,callback=self.parse)
        # for url in self.urls:
        #     url = 'https:' + url
        #     # page number
        #     for i in range(1, 5):
        #         url = url.replace(str(i), str(i + 1))
        #         yield Request(url, self.parse)
        #yield scrapy.Request(self.geturl(), self.parse())
        if self.n < 5:
            self.n += 1  # n表示页码
        next_url = 'https://www.qidian.com/rank/fengyun?page=%d' % self.n
        yield scrapy.Request(next_url, callback=self.parse)

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    a_book_number = scrapy.Field()
    f_book_link = scrapy.Field()
    b_book_name = scrapy.Field()
    c_author = scrapy.Field()
    d_book_type = scrapy.Field()
    e_condition = scrapy.Field()
    i_intro = scrapy.Field()
    g_update_info = scrapy.Field()
    h_up_time = scrapy.Field()


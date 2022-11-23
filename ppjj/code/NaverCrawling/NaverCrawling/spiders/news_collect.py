import scrapy
import random
from NaverCrawling.items import NavercrawlingItem
from NaverCrawling.items import NaverEdaily

class QuotesSpider(scrapy.Spider):
    name = "news"
    user_agents_list = [
            'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
                ]

    def start_requests(self):
        while True:
            page=1
            urls = [
                        # 연합 인포
                f'https://news.einfomax.co.kr/news/articleList.html?page={page}&total=175311&box_idxno=&sc_area=A&view_type=sm&sc_word=%EA%B8%88%EB%A6%AC',
                # 이데일리
                f'https://news.einfomax.co.kr/news/articleList.html?page={page}&total=175311&box_idxno=&sc_area=A&view_type=sm&sc_word=%EA%B8%88%EB%A6%AC'
            ]
            # user_agents_list = [
            # 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
            #     ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse_yonhab,headers={'User-Agent': random.choice(self.user_agents_list)})
                yield scrapy.Request(url=url, callback=self.parse_edaily,headers={'User-Agent': random.choice(self.user_agents_list)})


    def parse_yonhab(self, response):
        url=response.css('#newsList')
        print(url)
        

    def parse_edaily(self,response):
        pass
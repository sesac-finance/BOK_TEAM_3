'''import scrapy
import random
from NaverCrawling.items import NavercrawlingItem
from NaverCrawling.items import NaverEdaily
import datetime
import calendar

class QuotesSpider(scrapy.Spider):
    name = "aaa"

    def start_requests(self):
        date_total=datetime.datetime(2013,1,3)
        future_date=datetime.datetime(2013,2,1)
        while True:
            if date_total.year==future_date.year and date_total.month==future_date.month:
                break
            howmany_days=calendar.monthrange(date_total.year, date_total.month)[1]
            for day_count in range(1,howmany_days+1):
                date_year=date_total.year
                date_month=date_total.month
                date_total=datetime.datetime(date_year,date_month,day_count)
                date_day=date_total.day
                date_put_y=date_total.strftime('%y')
                date_put_m=date_total.strftime('%m')
                date_put_d=date_total.strftime('%d')
                urls = [
                    # 연합 인포
            f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds={date_year}.{date_put_m}.{date_put_d}&de={date_year}.{date_put_m}.{date_put_d}&docid=&related=0&mynews=1&office_type=2&office_section_code=8&news_office_checked=2227&nso=so%3Ar%2Cp%3Afrom{date_year}{date_put_m}{date_put_d}to{date_year}{date_put_m}{date_put_d}&is_sug_officeid=0',
            # 이데일리
            f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds={date_year}.{date_put_m}.{date_put_d}&de={date_year}.{date_put_m}.{date_put_d}&docid=&related=0&mynews=1&office_type=2&office_section_code=8&news_office_checked=1018&nso=so%3Ar%2Cp%3Afrom{date_year}{date_put_m}{date_put_d}to{date_year}{date_put_m}{date_put_d}&is_sug_officeid=0'
        ]   
        
                for url in urls[1:]:
                    yield scrapy.Request(url=url, callback=self.parse)
            if date_month==12:
                date_total=datetime.datetime(date_year+1,1,1)
            else:
                date_total=datetime.datetime(date_year,date_month+1,1)
    def parse(self, response):
        a=0
        naver_news=response.css('.list_news li')
        user_agents_list = [
        'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
            ]
        for num in range(len(naver_news)):
            naver_new=naver_news[num].css('.news_area > a::attr(href)').get()
        
            

            # yield scrapy.Request(url=naver_new, callback=self.parse_edaily,headers={'User-Agent': random.choice(user_agents_list)})
            print('한번')
        
        next_check=response.css('.sc_page>a::attr(aria-disabled)').get()
        # next_page='https://search.naver.com/search.naver'+response.css('.sc_page>a::attr(href)').getall()
        next_page=response.css('div.sc_page a::attr(href)').getall()[-1]

        print('잘되고 있다',next_page)
        if next_check =='true':
            print('계속',a)
            # yield scrapy.Request(url=next_page, callback=self.parse,headers={'User-Agent': random.choice(user_agents_list)})
            
            
        else:
            print("끝")
        # if len(next_page)==1:
        #     pass
        # else:
        #     for nu in range(1,len(next_page)-1):
        #         Next_naver='https://search.naver.com/search.naver'+next_page[nu].css('::attr(href)').get()
        #         yield scrapy.Request(url=Next_naver, callback=self.parse,headers={'User-Agent': random.choice(user_agents_list)})'''
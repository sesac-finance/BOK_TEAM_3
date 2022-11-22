import scrapy
import random
from NaverCrawling.items import NavercrawlingItem
# from NaverCrawling.items import NaverEdaily
import datetime
import calendar

class QuotesSpider(scrapy.Spider):
    name = "naver"

    def start_requests(self):
        date_total=datetime.datetime(2014,11,8)
        future_date=datetime.datetime(2019,12,31)
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
            f'https://search.naver.com/search.naver?where=news&query=%EA%B8%88%EB%A6%AC&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds={date_year}.{date_put_m}.{date_put_d}&de={date_year}.{date_put_m}.{date_put_d}&docid=&related=0&mynews=1&office_type=2&office_section_code=8&news_office_checked=1001&nso=so%3Ar%2Cp%3Afrom{date_year}{date_put_m}{date_put_d}to{date_year}{date_put_m}{date_put_d}&is_sug_officeid=0',
            # 이데일리
            
        ]   
        
                for url in urls:
                    yield scrapy.Request(url=url, callback=self.parse) #하루에 한 번씩 크롤링을 시키는 부분
            if date_month==12:
                date_total=datetime.datetime(date_year+1,1,1)
            else:
                date_total=datetime.datetime(date_year,date_month+1,1)
    def parse(self, response):
    
        naver_news=response.css('.list_news li')
        user_agents_list = [
        'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
            ]
        for num in range(len(naver_news)): #한 페이지 안에 뉴스들의 개수를 갖고오는 부분
            naver_new=naver_news[num].css('.news_area > a::attr(href)').get() #하이퍼링크 가져오는 부분
        
            

            # yield scrapy.Request(url=naver_new, callback=self.parse_yonhab,headers={'User-Agent': random.choice(user_agents_list)})
            yield scrapy.Request(url=naver_new, callback=self.parse_edaily,headers={'User-Agent': random.choice(user_agents_list)})

        next_page=response.css('.btn_next')
        if len(next_page)==1:
            pass
        else:
            next_check=response.css('.sc_page>a::attr(aria-disabled)').get()
        
            next_page=response.css('div.sc_page a::attr(href)').getall()[-1]

        
            if next_check =='true':
                
                yield scrapy.Request(url=next_page, callback=self.parse,headers={'User-Agent': random.choice(user_agents_list)})


    def parse_edaily(self,response):

        item2=NavercrawlingItem()

        item2['title']=response.css('.title-article01 .tit::text').get()
        item2['content']="".join(response.css('.story-news.article *::text').getall()).replace('\n','').strip()
        item2['date']=response.css('#newsUpdateTime01::attr(data-published-time)').get()

        if item2['content']=='' or '[표]' in item2['title']:
            yield None
        else:
            yield item2

import scrapy

from tutorial.items import TutorialItem


class RunSpider(scrapy.Spider):
    name = "run"
    allowed_domains = ["58guakao.com"]
    start_urls = [
        'http://resume.58guakao.com/qzjl/1',
    ]

    def parse(self, response):
        print("抓取完成 - %s" % response.url)
        # 分析页面数据，创建Item
        tr_list = response.css("table.tblist tr")
        for i in range(2, len(tr_list)):
            item = TutorialItem()
            tr = tr_list[i]
            td_list = tr.css("td")
            td_name = td_list[0]
            td_span = td_name.css("span")[0]
            name = td_span.css("::text").extract_first()
            item['name'] = name.strip()
            item['gender'] = td_list[1].css("::text").extract_first()
            item['age'] = td_list[2].css("::text").extract_first()
            item['life'] = td_list[3].css("::text").extract_first()
            item['education'] = td_list[4].css("::text").extract_first()
            item['address'] = td_list[7].css("::text").extract_first()
            yield item
        # 检测下一页
        next_page = response.css(".pager>a.next")
        if next_page is not None:
            a = next_page.css("::attr(href)").extract_first()
            next_url = response.urljoin(a)
            yield scrapy.Request(url=next_url, callback=self.parse)

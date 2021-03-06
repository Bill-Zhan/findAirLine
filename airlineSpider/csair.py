#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by AKM_FAN@163.com on 2018/1/24
"""
南方航空公司机票
http://b2c.csair.com/B2C40/modules/bookingnew/main/flightSelectDirect.html?t=S&c1={0}&c2={1}&d1={2}&at=1&ct=0&it=0
"""


from selenium import webdriver


def csair_flight(org_city_code, dst_city_code, flight_date):
    airline_url = 'http://b2c.csair.com/B2C40/modules/bookingnew/main/flightSelectDirect.html?t=S&c1={0}&c2={1}&d1={2}&at=1&ct=0&it=0'.format(org_city_code, dst_city_code, flight_date)
    print(airline_url)

    browser = webdriver.Chrome('/Users/roy/Downloads/tmp/chromedriver')
    browser.implicitly_wait(30)
    browser.get(airline_url)

    try:
        flight_div = browser.find_element_by_xpath('//div[@class="sp-trip-body"]')
    except Exception as err:
        browser.quit()
        print err
        print u'没有%s当日的航班信息' % flight_date
        return '', '', ''
    flight_list = flight_div.find_elements_by_tag_name('ul')

    cheapest_flight = None
    cheapest_price = ''
    for item in flight_list:
        price = item.find_elements_by_class_name('price')[-1].text.split(' ')[1]
        if not cheapest_flight and not cheapest_price:
            cheapest_flight = item
            cheapest_price = price

        if price and int(cheapest_price) > int(price):
            cheapest_flight = item
            cheapest_price = price

    if cheapest_flight:
        cheapest_flight_text = cheapest_flight.text
        browser.quit()
        return '', cheapest_flight_text, cheapest_price

    browser.quit()
    return '', '', ''


# csair_fligth('NKG', 'KMG', '2018-03-02')
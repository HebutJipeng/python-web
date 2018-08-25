# -*- coding: utf-8 -*-
import scrapy
import re
import time
import codecs
import json

from fbpage.items import FbpageItem

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class FbpageSpider(scrapy.Spider):
    # 定义Scrapy爬虫相关的内容
    name = "fbpage"
    allowed_domains = ["www.facebook.com"]
    start_urls = (
        'https://www.facebook.com',
    )

    def __init__(self):
        # Mac Chrome设置 #
        print('?????')
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images":2} # 禁止显示图片
        chromeOptions.add_experimental_option("prefs",prefs)
        chromeOptions.add_argument("--disable-notifications") # 禁止通知
        chromeOptions.add_argument("--headless") # 后台静默运行
        self.driver = webdriver.Chrome('/Users/jipeng/htdoc/frontend/python_web/v2/chromedriver', chrome_options=chromeOptions)
        # Mac Chrome设置 #

    def parse(self, response):
        driver = self.driver
        wait = WebDriverWait(driver, 300)
        urls = []
        scroll_times = 2    # 期望的翻页 次数
        url_num = 10    # 期望的用户数
        user_list_url = "https://www.facebook.com/search/820882001277849/likers?ref=snippets" # 粉丝列表地址
        js_scroll="window.scrollTo(0,document.documentElement.scrollHeight)"
        js_scroll_up="window.scrollBy(0,-1)"
        js_scroll_top="window.scrollTo(0,0)"

        # 几个JS脚本，由于需要不停向下翻页来获取更多的用户、兴趣信息，
        # 如果不删除已经获取过信息的网页元素，将导致网页卡顿严重
        js_removeUselessDom='''
            var list=document.getElementById("pagelet_loader_initial_browse_result").firstChild.firstChild;
            list.removeChild(list.childNodes[1]);
        '''
        js_removeFirstUserList='''
            var list=document.getElementById("pagelet_loader_initial_browse_result").firstChild.firstChild;
            list.removeChild(list.childNodes[0]);
        '''
        js_removeTwoUserList='''
            var list=document.getElementById("pagelet_loader_initial_browse_result").firstChild.firstChild;
            list.removeChild(list.childNodes[0]);
            list.removeChild(list.childNodes[0]);
        '''
        js_removeTwoInterest='''
            var list=document.getElementById("pagelet_timeline_medley_likes").childNodes[1].firstChild;
            list.removeChild(list.childNodes[0]);
            list.removeChild(list.childNodes[0]);
        '''
        js_removeOneInterest='''
            var list=document.getElementById("pagelet_timeline_medley_likes").childNodes[1].firstChild;
            list.removeChild(list.childNodes[0]);
        '''
        item = FbpageItem()
        #打开网页
        for i in range(1, 10000):
            try:
                driver.get(response.url)
                break
            except:
                print("****\n打开网页失败，重试中\n****")
        #登陆fb
        for i in range(1,10000):
            try:
                username_box = driver.find_element_by_xpath('//input[@type="email"]')
                username_box.send_keys("jipeng@gotokeep.com")
                password_box = driver.find_element_by_xpath('//input[@type="password"]')
                password_box.send_keys("jp123456")
                login_btn = driver.find_element_by_xpath('//label[@class="uiButton uiButtonConfirm"]')
                login_btn.click()
                break
            except:
                print("****\n获取登陆表单元素失败，重试中\n****")
        #获取用户列表
        with codecs.open('url.txt', 'r') as url_file:   # 记得先在工作目录>fbpage下新建url.txt
            lines = url_file.readlines()
        urls = lines
        url_file.close()

        if lines != "" and len(lines) >= url_num:   # 保证url.txt中有足够多的用户数量
            pass
        else:
            #搜索
            driver.get(user_list_url)
            if '/likers' in user_list_url:
                print("---->", user_list_url)
                pass
            else:
                #点击显示更多
                seemore_btn = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "See All")))
                seemore_btn.click()
            #删除无用dom
            driver.execute_script(js_removeUselessDom)
            time.sleep(0.1)
            print("****\n已删除用户列表中的无用dom\n****")
            #获取第一部分用户主页链接
            for sel in driver.find_elements_by_xpath('//div[@id="BrowseResultsContainer"]//div[@data-gt]/div/a'):
                url = sel.get_attribute("href")
                print('aaaaa===>', url)
                if "?ref=br_rs" in url:
                    url = url.split("?")[0]
                else:
                    url = url.split("&")[0]
                if url + '\n' not in urls:
                    urls.append(url)
                    codecs.open('url.txt', 'a').write(url + "\n")
            driver.execute_script(js_removeFirstUserList)
            time.sleep(0.1)
            print("****\n已删除初始用户列表\n****")
            driver.execute_script(js_scroll)
            time.sleep(0.1)
            print("****\n向下滚动以获取更多用户列表\n****")

            #删除第i部分用户列表并下滑
            for i in range(1,scroll_times):
                print("****\n第%d次滚动\n****" % i)
                while len(driver.find_elements_by_xpath('//div[@id="pagelet_loader_initial_browse_result"]/div/div/div')) < 3:
                    print("****\n等待用户列表加载\n****")
                    time.sleep(1)
                time.sleep(3)
                for sel in driver.find_elements_by_xpath('//div[@id="pagelet_loader_initial_browse_result"]/div/div/div//div[@data-gt]/div/a'):
                    url = sel.get_attribute("href")
                    if "?ref=br_rs" in url:
                        url = url.split("?")[0]
                    if "&ref=br_rs" in url:
                        url = url.split("&")[0]
                    if url + '\n' not in urls:
                        urls.append(url)
                        codecs.open('url.txt', 'a').write(url + "\n")
                driver.execute_script(js_removeTwoUserList)
                time.sleep(0.1)
                print("****\n已删除所有用户列表\n****")
                driver.execute_script(js_scroll_up)
                time.sleep(0.1)
                driver.execute_script(js_scroll)
                time.sleep(0.1)
                print("****\n滚动以加载更多用户列表\n****")
                i += 1
        user_index = 1
        # 对于只有数字id的用户，在主页地址后面加上&sk=likes,否则加上/likes_all
        for url in urls:
            url = url.split('\n')[0]
            if "?id" in url:
                url = url + "&sk=likes"
            else:
                # url = url + "/likes_section_apps_and_games" # 游戏相关
                url = url + "/likes_all"
            file = codecs.open('fbpage.json', 'r', encoding='utf-8').read()
            if url not in file:
                for i in range(1,10000):
                    try:
                        driver.get(url) # 打开用户的兴趣页面
                        break
                    except:
                        print("****\n打开网页失败，重试中\n****")
                        driver.save_screenshot('fail.png')
                interests = []
                pass_current_user = False
                # if driver.find_elements_by_xpath('//a[@name="Apps and Games"]'): # 游戏相关
                if driver.find_elements_by_xpath('//a[@name="All Likes"]'):
                    item["url"] = url   # 保存用户的主页链接数据，交给pipeline处理
                    print("****\n正在获取第%d个用户的兴趣\n****" % user_index)
                    driver.execute_script(js_scroll)
                    time.sleep(0.1)
                    print("****\n向下滚动以获取更多用户兴趣\n****")
                    initial_time = 0
                    # xpath('//div[@id="pagelet_timeline_medley_likes"]/div[2]/div/ul'为用户兴趣列表，每组ul中有4个兴趣
                    # xpath('//div[@id="pagelet_timeline_medley_likes"]/div[2]/div/img')为正在加载更多数据的动画，如果没有了表示兴趣已经显示完全了
                    while len(driver.find_elements_by_xpath('//div[@id="pagelet_timeline_medley_likes"]/div[2]/div/ul')) < 3 and driver.find_elements_by_xpath('//div[@id="pagelet_timeline_medley_likes"]/div[2]/div/img'):
                        print("****\n向下滚动后还未完全加载用户兴趣，请稍等\n****")
                        time.sleep(1)
                        initial_time += 1
                        if initial_time >= 5:
                            driver.execute_script(js_scroll)
                            time.sleep(0.1)
                            print("****\n等待时间过长，向下滚动以获取更多用户兴趣\n****")
                            initial_time = 0
                    for sel in driver.find_elements_by_xpath('//div[@class="fsl fwb fcb"]/a'):
                        interest = sel.text
                        if interest not in interests:
                            print("****\n已获取一个兴趣\n%s\n当前第%d个用户，第%d个兴趣\n****" % (interest, user_index, len(interests)))
                            interests.append(interest)
                    while driver.find_elements_by_xpath('//div[@id="pagelet_timeline_medley_likes"]/div[2]/div/img') and not pass_current_user:
                        wait_time = 0
                        while len(driver.find_elements_by_xpath('//div[@id="pagelet_timeline_medley_likes"]/div[2]/div/ul')) < 3:
                            print("****\n向下滚动后还未完全加载用户兴趣，请稍等\n****")
                            time.sleep(1)
                            wait_time += 1
                            if wait_time >= 5:
                                print("****\n等待超时，尝试向下滚动\n****")
                                driver.execute_script(js_scroll)
                                time.sleep(0.1)
                                print("****\n向下滚动以获取更多用户兴趣\n****")
                                wait_time = 0
                        driver.execute_script(js_removeTwoInterest)
                        time.sleep(0.1)
                        print("****\n已删除两组用户兴趣列表\n****")
                        driver.execute_script(js_scroll_up)
                        time.sleep(0.1)
                        print("****\n向上滚动以获取更多用户兴趣\n****")
                        wait_time_scrollup = 0
                        while len(driver.find_elements_by_xpath('//div[@id="pagelet_timeline_medley_likes"]/div[2]/div/ul')) < 3 and not pass_current_user:
                            if driver.find_elements_by_xpath('//div[@id="pagelet_timeline_medley_likes"]/div[2]/div/img'):
                                print("****\n向上滚动后还未完全加载用户兴趣，请稍等\n****")
                                wait_time_scrollup += 1
                                time.sleep(1)
                                if wait_time_scrollup >= 60:    # 超过60s无响应，则跳过当前用户
                                    pass_current_user = True
                                    print("****\n加载失败，跳过该用户\n****")
                                    break
                            else:
                                print("****\n已到达列表末尾，获取完兴趣后开始下一个用户\n****")
                                for sel in driver.find_elements_by_xpath('//div[@class="fsl fwb fcb"]/a'):
                                    interest = sel.text
                                    if interest not in interests:
                                        interests.append(interest)
                                        print("****\n已获取一个兴趣\n%s\n当前第%d个用户，第%d个兴趣\n****" % (interest, user_index, len(interests)))
                                break
                        for sel in driver.find_elements_by_xpath('//div[@class="fsl fwb fcb"]/a'):
                            interest = sel.text
                            if interest not in interests:
                                interests.append(interest)
                                print("****\n已获取一个兴趣\n%s\n当前第%d个用户，第%d个兴趣\n****" % (interest, user_index, len(interests)))
                    user_index += 1
                    item["interests"] = interests   # 保存用户的兴趣数据，交给pipeline处理
                    yield item
                else:
                    item["url"] = url
                    item["interests"] = interests
                    yield item
                    # print("****\n该用户不允许其他人查看自己的兴趣，或没有关于游戏的兴趣，略过\n****") # 游戏相关
                    print("****\n该用户不允许其他人查看自己的兴趣，或没有任何兴趣，略过\n****")
                pass_current_user = False
                # 新建一个标签页以抓取下一个用户数据，并关闭当前标签页
                driver.execute_script('''window.open()''')
                time.sleep(1)
                first_window = driver.window_handles[0]
                second_window = driver.window_handles[1]
                driver.switch_to_window(first_window)
                driver.close()
                driver.switch_to_window(second_window)
        driver.quit()
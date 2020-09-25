#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/22 18:36
#@Author: f
#@File  : 雨课堂forHIT.py

"""
代码基于 https://github.com/lingyan12/yuketang 和https://github.com/xrervip/HIT_auto_report/blob/master/HIT_auto_report.py 进行修改
依赖于python运行环境+chorme+selenium chrome驱动
selenium chrome驱动 镜像地址: http://npm.taobao.org/mirrors/selenium

说明：使用参数 CookieMode 可以在cookie，json 写入cookie并进行快捷登录
"""
"""
下一步目标：
1.增加多线程播放配置
2.提高稳定性和健壮性
"""
import platform
import json
from selenium.webdriver.chrome.options import Options
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support import expected_conditions  as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class auto雨课堂:

    home_url='https://hit.yuketang.cn/pro/portal/home/'
    course_url= ""

    def __init__(self,mode):

        isCookieMode=False
        if "CookieMode" in mode:
            isCookieMode=True

        self.setDriver()

        """使用CookieMode登录"""
        self.loadCookie(isCookieMode)

        self.readFromJSON()#从JSON读入URL

        self.load_url(self.course_url)

        self.login(isCookieMode)

        while True:
            time.sleep(0.1)
            if self.driver.current_url==self.course_url:
                print("成功登录雨课堂")
                break

        self.prepare_list('url_list.txt')
        self.PlayAllVideo('url_list.txt')


        self.driver.quit()

    def PlayAllVideo(self,location):
        """
        播放全部的视频
        :param location:  文件的位置
        :return:
        """

        url_list = self.read_url_list(location)

        for url in url_list:
            self.PlayVideo(url)

        print("完成url_list中全部任务")


    def PlayVideo(self,url):
        """
        播放全部的视频
        :param url: 网课的URL
        :return:
        """
        print(url)
        self.load_and_wait_url(url)  #切换到新的窗口

        title=self.wait_and_getText("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/span")
        print("正在播放:"+title)

        try:
            work_persent = self.wait_and_getText(
                '/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/section[1]/div[2]/div/div/span')
        except TimeoutException:
            work_persent="任务进度元素加载失败" #元素加载失败




        print("任务进度："+work_persent)
        time.sleep(0.5)

        """该小节播放完成/不需要播放"""
        if "100%" in work_persent :
            return


        """"需要播放视频的情况"""
        self.wait_and_getText("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/section[2]/div[1]/div/div/div/xt-wrap/xt-controls/xt-inner/xt-time/span[2]")
        """开始播放"""
        button = WebDriverWait(self.driver, 10, poll_frequency=2).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="video-box"]/div/xt-wrap/xt-controls/xt-inner/xt-playbutton')))

        """设置2倍速度"""
        if button:
            speed_button = WebDriverWait(self.driver, 10, poll_frequency=1).until(ec.presence_of_element_located((By.XPATH,
                                                                                                   '//*[@id="video-box"]/div/xt-wrap/xt-controls/xt-inner/xt-speedbutton/xt-speedvalue')))
            speed_2 = self.driver.find_element_by_xpath(
                '//*[@id="video-box"]/div/xt-wrap/xt-controls/xt-inner/xt-speedbutton/xt-speedlist/ul/li[1]')
            ac(self.driver).move_to_element(speed_button).perform()
            time.sleep(1)
            speed_2.click()
            button.click()

            cur_time = self.driver.find_element_by_xpath(
                '//*[@id="video-box"]/div/xt-wrap/xt-controls/xt-inner/xt-time/span[1]').text.split(':')
            full_time = self.driver.find_element_by_xpath(
                '//*[@id="video-box"]/div/xt-wrap/xt-controls/xt-inner/xt-time/span[2]').text.split(':')
            cur = (int(cur_time[1]) * 60 + int(cur_time[2]))
            ful = (int(full_time[1]) * 60 + int(full_time[2]))
            self.wait_video(cur,ful)
            time.sleep(5)

        return

    def wait_video(self,cur,ful):
        """
        等待视频播放完成
        :param cur: 当前时间
        :param ful: 总时间
        :return:
        """
        count=cur
        while cur<ful:
            time.sleep(1)
            cur=cur+1
            print("当前时间：" + str(cur) + "总时间" + str(ful))

        return
    def prepare_list(self,location):
        """
        为播放准备连接
        :param location: 保存网课连接的文件地址
        :return:
        """
        with open(location,'r+',encoding='utf-8') as fp:
            lines = fp.readlines()  # 读取所有行
            last_line=""
            if len(lines)!=0:
                last_line = lines[-1]  # 取最后一行
            if "构建完成" not in last_line:
                fp.close()
                self.get_list(location)
            else:
                fp.close()
                print("已从历史记录中获取链接")

            print("全部链接已就绪")

        return

    def get_list(self,location):
        """
        爬取全部网课连接
        :param location:保存网课连接的文件地址
        :return:
        """
        with open(location,'w+',encoding='utf-8') as fp:

            self.driver.get(self.course_url)
            self.wait_element_path("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div[2]/section[2]/div[2]/ul/li[1]/div[1]/div/span")
            botton=self.driver.find_elements(By.XPATH,"//span[@class='cursorpoint unit-name-hover']")
            print("正在爬取全部视频网页连接")
            for i in botton:
                i.click()
                handle = self.driver.current_window_handle  # 当前主窗口
                handles = self.driver.window_handles  # 全部窗口句柄
                # 对窗口进行遍历
                for newhandle in handles:
                    # 筛选新打开的窗口B
                    if newhandle != handle:
                        # 切换到新打开的窗口B
                        # browser.switch_to_window(newhandle) 旧版本
                        self.driver.switch_to.window(newhandle)
                        current_url = (self.driver.current_url + '\r')
                        print(self.driver.current_url)
                        if "/video/" in self.driver.current_url:
                            fp.writelines(current_url)
                            fp.flush()
                        self.driver.close()
                        self.driver.switch_to.window(handle)
                        time.sleep(0.5)
            fp.writelines('构建完成')
            fp.flush()
            fp.close()
        return

    def read_url_list(self,location):
        url_list = []
        with open(location, 'r',encoding='utf-8') as fp:
            url_content = fp.readlines()
            for url in url_content:
                if "构建完成" not in url:
                    url = url[:-1]
                    url_list.append(url)
            fp.close()
        return url_list

    def login(self,isCookieMode):
        """
          雨课堂登录
          :param isCookieMode:  如果使用cookie，则不需要登录
          :return:
          """

        if isCookieMode:
            return
        print("登录雨课堂")

        self.load_url(self.home_url)
        self.wait_element_path('/html/body/div[4]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/button')
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[3]/div/div[1]/div/div/div[2]/button').click()
        while True:
            self.load_url(self.course_url)
            time.sleep(5)
            if self.course_url == self.driver.current_url:
                return

    def loadCookie(self,isCookieMode):
        """
        从cookie载入登录信息
        :return:
        """
        if not isCookieMode:
            return

        print("从Cookie文件加载登录信息")
        try:
            f = open("./cookie.json", 'r', encoding='utf-8')
        except FileNotFoundError:
            print("未检测到Cookie.json，需要进行手动登录")
            return False


        """载入cookie"""
        cookies = json.load(f)

        self.load_url(self.home_url)
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        return True

    def setDriver(self):
        """
        根据系统环境配置chormedriver
        :return:
        """
        chrome_options = Options()
        sysstr = platform.system()

        if (sysstr == "Linux"):  # for Linux
            chrome_options.add_argument('--headless')  # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
            chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行
            chrome_options.add_argument("--mute-audio") #静音播放

        else:  # for other OS
            chrome_options.add_argument("--mute-audio") #静音播放

        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        print("成功配置chrome驱动")


    def load_and_wait_url(self, target_url, timeout=10.0):
        """
        等待直到url更新为目标url
        :param target_url: 预计更新后的目标url
        :param timeout: 超时时间
        :return:
        """
        self.load_url(target_url)
        while target_url != self.driver.current_url and timeout > 0:
            time.sleep(0.1)
            timeout -= 0.1
        if timeout <= 0:
            raise TimeoutException()

    def wait_element_path(self, element_xpath):
        """
        等待相应xpath的元素加载完成
        :param element_xpath: 元素xpath
        :return: 对对应的元素
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )
        return element

    def wait_and_send_keys(self, element_id, keys):
        """
        等待相应id的元素加载完成后输入字符
        :param element_id: 元素id
        :param keys: 需要输入的字符
        :return:
        """
        element = self.wait_element_id(element_id)
        element.send_keys(keys)

    def wait_and_click(self, element_xpath):
        """
        等待相应id的元素加载完成后点击元素
        :param element_xpath: 元素path
        :return:
        """
        element = self.wait_element_path(element_xpath)
        element.click()

    def wait_and_getText(self, element_xpath):
        """
        等待相应id的元素加载完成后点获取其中的文字信息
        :param element_xpath: 元素path
        :return:
        """
        element = self.wait_element_path(element_xpath)
        return element.text

    def readFromJSON(self):
        """
        从JSON中读取数据，并写入URL
        :return:
        """
        try:
            f = open("./config.json", 'r', encoding='utf-8')
        except FileNotFoundError :
            print("config.json文件不存在，请检查！")

        data = json.load(f)
        self.course_url = data[0]["URL"]

        print("读取json文件")

    def load_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)


if __name__ == '__main__':

    mode=""
    if len(sys.argv) == 2:
        mode=sys.argv[1]
    auto雨课堂(mode)
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as e_conditions
from selenium.webdriver.support.ui import WebDriverWait
from loguru import logger
from tkinter import messagebox,ttk
import tkinter as tk
import time
import requests
from bs4 import BeautifulSoup
import textwrap
import random


def game_data_craw_part_script():
    uiautomator2_option = UiAutomator2Options()
    uiautomator2_option.load_capabilities({
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    })

    android_driver = webdriver.Remote('http://127.0.0.1:4723', options=uiautomator2_option)
    wait = WebDriverWait(android_driver, 20)

    news_hrefs = []
    news_contents = []

    def quit_application_return():
        for i in list(range(0,7)):
            logger.info('这是第{}次退出...'.format(i))
            android_driver.back()

    def daily_news():
        def daily_news_step_one():
            try:
                news_source_url = 'https://news.baidu.com/'
                r = requests.get(news_source_url)
                soup = BeautifulSoup(r.content, 'lxml')
                news_source = soup.find('div', class_='hotnews')
                # print(news_source)
                news_source_1 = news_source.find('ul')
                # print(news_source_1)
                news_source_2 = news_source_1.find_all('li')
                # print(len(news_source_2))
                for new in news_source_2:
                    # print(new.text)
                    relevant_href_source = new.find('a')
                    relevant_href = relevant_href_source['href']
                    # print(relevant_href)
                    news_hrefs.append(relevant_href)
                    # print('++++--')
                return news_hrefs
            except Exception as e:
                logger.error(e)
                return None

        def daily_news_step_two():
            try:
                random_news_href = random.choice(news_hrefs)
                r = requests.get(random_news_href)
                soup = BeautifulSoup(r.content, 'lxml')
                news_content = soup.text
                result_news_content = textwrap.wrap(str(news_content))
                print(result_news_content)
                news_contents.append(result_news_content)
                return news_contents
            except Exception as e:
                logger.error(e)
                news_contents.append('暂无相关新闻.......')
                return news_contents

        def daily_news_running_sequence():
            daily_news_step_one()
            daily_news_step_two()

        daily_news_running_sequence()

    # daily_news()

    def check_whether_own_xiao_hei_he():
        logger.info('check_whether_own_xiao_hei_he running...')
        try:
            xiao_hei_he = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="小黑盒"]')))

            def stage_information():

                def quit_stage_information():
                    if messagebox.askyesno('提示', '是否确认退出当前页面?'):
                        stage_information_root.destroy()

                def inner_stage_information():
                    stage_text.insert(tk.INSERT, '检索应用中....\n\n')
                    time.sleep(1)

                    time.sleep(1)
                    stage_text.insert(tk.END, '可以先阅读新闻以等待.....\n\n')

                    time.sleep(1)
                    daily_news()
                    wait_for_insert_text = str(news_contents[0])
                    stage_text.insert(tk.END, f'{wait_for_insert_text}\n\n')
                    stage_information_root.update_idletasks()

                    if xiao_hei_he.get_attribute('text') == '小黑盒':
                        stage_text.insert(tk.END, '已完成检索,成功检索到应用,现可退出当前界面以继续.....\n\n')

                        stage_button_end = ttk.Button(stage_information_root, text='退出当前页面',
                                                      command=quit_stage_information)
                        stage_button_end.grid(row=3, column=13, columnspan=4)
                        stage_information_root.update_idletasks()

                stage_information_root = tk.Tk()
                stage_information_root.title('检索应用进程')

                stage_text = tk.Text(stage_information_root)
                stage_text.grid(row=1, column=0, columnspan=30)

                stage_button_start = ttk.Button(stage_information_root, text='开始检索',
                                                command=inner_stage_information)
                stage_button_start.grid(row=2, column=13, columnspan=4)

                stage_information_root.mainloop()

            stage_information()

        except Exception as e:
            logger.error(f'{e}')
            messagebox.showwarning('错误', '手机里未含小黑盒应用!!!')

    # check_whether_own_xiao_hei_he()

    def enter_xiao_hei_he():
        logger.info('enter_xiao_hei_he running...')
        try:
            xiao_hei_he_application = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="小黑盒"]')))
            xiao_hei_he_application.click()

        except Exception as e:
            logger.error(f'{e}')

    # enter_xiao_hei_he()

    def self_game_data_craw():
        logger.info('self_game_data_craw...')

        try:
            self_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, '//android.widget.RadioButton[@text="我"]')))
            self_button.click()

            running = True
            while running:

                data_details_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                           '//android.widget.TextView[@resource-id="com.max.xiaoheihe:id/tv_steam_info_card_username"]')))
                data_details_button.click()

                total_game_value = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                        '//android.view.View[@resource-id="app"]/android.view.View[4]/android.view.View[3]/android.view.View[1]/android.widget.TextView[1]'))).get_attribute(
                    'text')
                # print(total_game_value)

                total_game_time = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                       '//android.view.View[@resource-id="app"]/android.view.View[4]/android.view.View[4]/android.view.View/android.widget.TextView[1]'))).get_attribute(
                    'text')
                # print(total_game_time)

                total_game_number = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                         '//android.view.View[@resource-id="app"]/android.view.View[4]/android.view.View[5]/android.view.View/android.widget.TextView[1]'))).get_attribute(
                    'text')
                # print(total_game_number)

                describe_contain_messages = f'游戏库价值:{total_game_value}\n总游戏时长:{total_game_time}\n游戏库数量:{total_game_number}'
                if len(total_game_value) is not None and len(total_game_time) is not None and len(
                        total_game_number) is not None:
                    running = False
                    print(describe_contain_messages)
                    if messagebox.askyesno('搜索结果',f'{describe_contain_messages}\n是否进行储存?'):
                        with open('result.txt', 'a', encoding='utf-8') as f:
                            f.write(f'{describe_contain_messages}\n')
                        messagebox.showinfo('储存结果','储存成功,现可退出!')

        except Exception as e:
            logger.error(f'{e}')

    # self_game_data_craw()

    def other_game_data_craw(people_name):
        users_game_datas = []
        logger.info('other_game_data_craw...')
        try:
            search_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.max.xiaoheihe:id/iv_home_search"]')))
            search_button.click()

            search_input_location = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.max.xiaoheihe:id/et_search_edit"]')))
            # search_input_location.click()
            search_input_location.send_keys(people_name)

            time.sleep(2)
            ensure_search_position = [(1000, 2258)]
            android_driver.tap(ensure_search_position)

            application_user_zone = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="用户"]')))
            application_user_zone.click()

            # user_search_results_source = wait.until(e_conditions.presence_of_all_elements_located((AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.max.xiaoheihe:id/rv"]/android.widget.RelativeLayout')))
            user_search_results_source = wait.until(e_conditions.presence_of_all_elements_located(
                (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.max.xiaoheihe:id/tv_name"])')))
            # print(len(user_search_results_source))
            try:
                for each in user_search_results_source:
                    each.click()

                    each_data = wait.until(e_conditions.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.TextView[@text="数据"]')))
                    each_data.click()

                    #########用户数据爬取处理########
                    #########用户数据爬取处理########

                    try:
                        logger.info('用户数据爬取中.....')
                        # user_data_name = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="com.max.xiaoheihe:id/vg_card"]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView[1]'))).get_attribute('text')
                        # print(user_data_name)

                        user_data_game_lib_value = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                                        '//android.widget.RelativeLayout[@resource-id="com.max.xiaoheihe:id/pdv0"]/android.widget.TextView[1]'))).get_attribute(
                            'text')
                        print(user_data_game_lib_value)

                        uer_data_game_time = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                                  '//android.widget.RelativeLayout[@resource-id="com.max.xiaoheihe:id/pdv1"]/android.widget.TextView[1]'))).get_attribute(
                            'text')
                        print(uer_data_game_time)

                        user_data_game_lib_number = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                                         '//android.widget.RelativeLayout[@resource-id="com.max.xiaoheihe:id/pdv2"]/android.widget.TextView[1]'))).get_attribute(
                            'text')
                        print(user_data_game_lib_number)
                        data_content = f'游戏库价值:{user_data_game_lib_value};游戏时长:{uer_data_game_time};游戏库数量:{user_data_game_lib_number}'
                        logger.info(data_content)
                        users_game_datas.append(data_content)

                    except Exception as eaa:
                        logger.info('该用户未绑定steam平台 : {}'.format(eaa))
                        pass


                if messagebox.askyesno('搜索结果',f'已获取完毕,是否进行储存?'):
                    for i in users_game_datas:
                        with open('result.txt', 'a', encoding='utf-8') as f:
                            f.write(f'{i}\n')
                            messagebox.showinfo('储存结果', '储存成功,现可查看!')
                    time.sleep(2)
                    android_driver.back()
                    #########用户数据爬取处理########
                    #########用户数据爬取处理########

            except Exception as e:
                logger.error(f'用户检索结果处理失败:{e}')

        except Exception as e:
            logger.error(f'{e}')

    # other_game_data_craw(people_name='123123')

    def game_data_craw_run_sequence(input_user_name):
        logger.info('game_data_craw_run_sequence...')
        enter_xiao_hei_he()
        other_game_data_craw(people_name=input_user_name)


    # game_data_craw_run_sequence()

    def game_data_craw_run_sequence_ui_version():
        logger.info('game_data_craw_run_sequence_ui_version...')

        def craw_other_user_data():
            def inner_craw_other_user_data():
                total_game_data_root.destroy()
                user_name_search = str(user_name_search_.get()).strip()
                if len(user_name_search) == 0 or user_name_search is None:
                    messagebox.showwarning('错误', '输入无效!')
                else:
                    if messagebox.askyesno('提示', f'你搜索的用户为:{user_name_search}\n是否继续?'):
                        game_data_root.destroy()
                        game_data_craw_run_sequence(input_user_name=user_name_search)
                        quit_application_return()
            game_data_root = tk.Tk()
            game_data_root.title('爬取用户详细')

            tk.Label(game_data_root, text='搜索内容:').grid(row=1, column=0)
            user_name_search_ = tk.Entry(game_data_root)
            user_name_search_.grid(row=1, column=1, columnspan=3)

            ttk.Button(game_data_root, text='确认搜索', command=inner_craw_other_user_data).grid(row=2, column=2)
            game_data_root.mainloop()

        def check_myself():
            if messagebox.askyesno('提示', '确认获取消息?'):
                total_game_data_root.destroy()
                enter_xiao_hei_he()
                self_game_data_craw()
                quit_application_return()

        def quit_game_data_craw_page():
            if messagebox.askyesno('提示', '确认退出?'):
                total_game_data_root.destroy()

        total_game_data_root = tk.Tk()
        total_game_data_root.title('爬取数据菜单')

        ttk.Button(total_game_data_root, text='获取他人数据', command=craw_other_user_data).pack(side=tk.LEFT)

        ttk.Button(total_game_data_root, text='获取自己数据', command=check_myself).pack(side=tk.RIGHT)

        ttk.Button(total_game_data_root, text='退出', command=quit_game_data_craw_page).pack()

        total_game_data_root.mainloop()

    game_data_craw_run_sequence_ui_version()

# game_data_craw_part_script()

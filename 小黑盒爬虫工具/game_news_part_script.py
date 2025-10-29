from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from selenium.webdriver.common.by import By
from loguru import logger
import tkinter as tk
from tkinter import ttk,messagebox
import time

def game_news_part_script():

    options = UiAutomator2Options()
    options.load_capabilities({
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    })

    game_new_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(game_new_driver, 20)

    def quit_application():
        for i in list(range(0, 7)):
            logger.info('这是第{}次退出...'.format(i))
            game_new_driver.back()

    def enter_xiao_hei_he_application():
        logger.info("enter_xiao_hei_he_application running...")
        try:
            application_button = wait.until(
                e_conditions.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="小黑盒"]')))
            application_button.click()

        except Exception as e:
                    logger.error(e)


    def switch_to_news_page():
        logger.info("switch_to_news_page running...")
        try:

            news_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.RadioButton[@text="热点"]')))
            news_button.click()

        except Exception as e:
            logger.error(e)

    def hot_focus_craw():
        logger.info("hot_news_craw running...")
        try:
            switch_to_new_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="热榜"]')))
            switch_to_new_button.click()

            hot_focus_source = wait.until(e_conditions.presence_of_all_elements_located((AppiumBy.XPATH,
                                                                                         '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.max.xiaoheihe:id/rv"]')))
            print(len(hot_focus_source))

        except Exception as e:
            logger.error(e)

    def game_news_part_running_script_sequence():
        enter_xiao_hei_he_application()
        switch_to_news_page()
        hot_focus_craw()
        quit_application()

    game_news_part_running_script_sequence()


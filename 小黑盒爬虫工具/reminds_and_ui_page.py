import tkinter as tk
from tkinter import ttk,messagebox
from loguru import logger
import time
from 已完成.小黑盒爬虫工具.game_data_craw_part_script import game_data_craw_part_script
from 已完成.小黑盒爬虫工具.game_news_part_script import game_news_part_script

local_time = time.asctime(time.localtime(time.time()))

class RemindPage:
    def __init__(self):
        def  reminding():
            logger.info('reminding running....')
            remind_text.insert(tk.END,f'当前时间为 {local_time}...\n')
            time.sleep(1)
            remind_root.update_idletasks()

            remind_text.insert(tk.END,'需切至有小黑盒的页面...\n')
            time.sleep(1)
            remind_root.update_idletasks()

            remind_text.insert(tk.END,'小黑盒最好处于登录状态...\n')
            time.sleep(1)
            remind_root.update_idletasks()

            remind_text.insert(tk.END,'爬取的结果会以txt文件储存...\n')
            time.sleep(1)
            remind_root.update_idletasks()

            quit_remind_button.config(text='已完成阅读,点击退出')

        def quit_remind():
            if messagebox.askyesno('提示','确认退出提示界面?'):
                remind_root.destroy()

        remind_root = tk.Tk()
        remind_root.title('使用提示')
        remind_root.geometry('400x400')

        remind_text = tk.Text(remind_root)
        remind_text.pack()

        remind_start_button = ttk.Button(remind_root,text='开始使用',command=reminding)
        remind_start_button.pack()

        quit_remind_button = ttk.Button(remind_root,text='退出',command=quit_remind)
        quit_remind_button.pack()
        remind_root.mainloop()


class MainOriginPage:
    def __init__(self):
        def search_content_data_crab():
            logger.info('search_content_data_crab running....')

        def daily_hot_news_data_crab():
            logger.info('daily_hot_news_data_crab running....')
            game_news_part_script()

        def game_data_crab():
            logger.info('self_game_data_crab running....')
            game_data_craw_part_script()

        def quit_first_menu_page():
            if messagebox.askyesno('提示','确认退出当前界面?'):
                main_page_root.destroy()

        main_page_root = tk.Tk()
        main_page_root.title('菜单主界面')

        menu_search_button = ttk.Button(main_page_root,text='搜索结果爬取',command=search_content_data_crab)
        menu_search_button.pack()

        menu_hot_news_button = ttk.Button(main_page_root,text='热点内容爬取',command=daily_hot_news_data_crab)
        menu_hot_news_button.pack()

        menu_self_game_data_button = ttk.Button(main_page_root,text='数据爬取',command=game_data_crab)
        menu_self_game_data_button.pack()

        quit_menu_button = ttk.Button(main_page_root,text='退出菜单界面',command=quit_first_menu_page)
        quit_menu_button.pack()

        main_page_root.mainloop()

test_remind = RemindPage()
test_main = MainOriginPage()

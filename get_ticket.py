
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

def get_ticket(num, from_station, to_station, date):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://kyfw.12306.cn/otn/resources/login.html")
    driver.find_element_by_css_selector("#J-userName ").send_keys("")
    driver.find_element_by_css_selector("#J-password ").send_keys("")
    driver.find_element_by_css_selector("#J-login ").click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#id_card ").send_keys("0033")
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#verification_code ").click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#verification_code ").click()

    driver.implicitly_wait(50)
    driver.find_element_by_css_selector("#link_for_ticket").click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#fromStationText").send_keys(Keys.ENTER)
    driver.find_element_by_css_selector("#fromStationText").clear()
    driver.find_element_by_css_selector("#fromStationText").click()
    driver.find_element_by_css_selector("#fromStationText").send_keys(from_station)
    driver.find_element_by_css_selector("#fromStationText").send_keys(Keys.ENTER)

    driver.find_element_by_css_selector("#toStationText").clear()
    driver.find_element_by_css_selector("#toStationText").click()
    driver.find_element_by_css_selector("#toStationText").send_keys(to_station)
    driver.find_element_by_css_selector("#toStationText").send_keys(Keys.ENTER)

    #延迟
    sleep(1)
    driver.find_element_by_css_selector("#train_date").clear()
    driver.find_element_by_css_selector("#train_date").click()
    driver.find_element_by_css_selector("#train_date").send_keys(date)
    driver.find_element_by_css_selector("#train_date").send_keys(Keys.ENTER)

    driver.find_element_by_css_selector("#query_ticket").click()
    if num ==1:
        driver.find_element_by_css_selector(f' #queryLeftTable tr:nth-child({num}) .btn72').click()
    elif num!=1:
        driver.find_element_by_css_selector(f' #queryLeftTable tr:nth-child({int(num) *2 -1}) .btn72').click()
    driver.implicitly_wait(10)
    passenger = input("请选择乘客：(1,2,3...)")
    driver.find_element_by_css_selector(f' #normalPassenger_{int(passenger) - 1}').click()
    stu = input("是否学生票？（是/否）")
    if stu == '是':
        driver.find_element_by_css_selector("#dialog_xsertcj_ok").click()
    driver.find_element_by_css_selector("#submitOrder_id").click()
    driver.find_element_by_css_selector("#erdeng1 > ul:nth-child(4) li:nth-child(2) a").click()
    time.sleep(3)
    driver.find_element_by_css_selector("#qr_submit_id").click()
    time.sleep(3)
    driver.find_element_by_css_selector("#insurance_buy_and_agree").click()
    driver.find_element_by_css_selector("#payButton").click()
    driver.implicitly_wait(10)
    input("请在30秒内完成支付，支付完成后按任意键退出")
    driver.quit()
from selenium import webdriver
driver = webdriver.Chrome()

def countTabs():
    handles = len(driver.window_handles)
    return handles

def newTab(max=99):
    if countTabs() < max:
        driver.switch_to.new_window('tab')

newTab(3)

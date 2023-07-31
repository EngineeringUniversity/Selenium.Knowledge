from selenium import webdriver
driver = webdriver.Chrome()

def countTabs():
    handles = len(driver.window_handles)
    return handles

def newTab(max=99):
    if countTabs() < max:
        driver.switch_to.new_window('tab')

def closeTab():
    parent = driver.window_handles[0]
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    driver.close()
    driver.switch_to.window(parent)

newTab(3)

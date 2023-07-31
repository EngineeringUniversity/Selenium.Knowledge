def newTab():
    driver.switch_to.new_window('tab')

def countTabs():
    handles = len(driver.window_handles)
    print(handles)

newTab()
countTabs()    

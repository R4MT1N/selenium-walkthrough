from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.google.com')
element = driver.find_element_by_link_text('Privacy')

# Initialize an 'ActionChain'
ActionChains(driver)\
    .key_down(Keys.CONTROL)\
    .click(element)\
    .key_up(Keys.CONTROL)\
    .perform()

# Switch to the last open tab
driver.switch_to.window(driver.window_handles[-1])
# or -> driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
# or -> ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()

ActionChains(driver)\
    .move_to_element_with_offset(driver.find_element_by_link_text('Chrome & the Chrome Operating System'))\
    .perform()
# driver.quit()

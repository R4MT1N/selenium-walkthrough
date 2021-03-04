from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize Chrome web driver
driver = webdriver.Chrome()
# Load the wikipedia.org web page
driver.get('https://wikipedia.org')
# Assert that string "Wikipedia" is contained in the title of the loaded page
assert "Wikipedia" in driver.title
# Fetch the element with ID 'searchInput' from the page DOM
element = driver.find_element_by_id('searchInput')
# Clear the text already occupied the form input
element.clear()
# Sending specific keyboard keys to type (or commands, e.g., Ctrl + F2)
element.send_keys('selenium')
# Press 'Enter' on the input (i.e., submitting the form)
element.send_keys(Keys.RETURN)
# (After loading the new page) fetch the element with ID 'firstHeading'
title = driver.find_element_by_id('firstHeading')
# Assert that the element is displayed on the page and its text is equal to 'Selenium'
assert title.is_displayed() and title.text == "Selenium"
# Close the driver
driver.close()

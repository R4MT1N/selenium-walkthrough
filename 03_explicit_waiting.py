from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://lab.bitbaan.com/")
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/en/home/antivirus"]')))
element.click()
anti_viruses = WebDriverWait(driver, 5)\
    .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'antimalware_result_list_antiName__2vpnQ')))
print([av.text.strip() for av in anti_viruses])
driver.quit()

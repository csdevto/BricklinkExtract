from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options
import datetime, time
import pandas as pd
import numpy as np

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)
#Here it goes the bricklink address with the model #
driver.get("https://www.bricklink.com/v3/studio/design.page?idModel=163780")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/section/div/div/div/button"))).click()
PName = driver.find_element_by_class_name('studio-model__header-title').text

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div[1]/div/div/section[1]/div/section[3]/button[1]"))).click()
WebDriverWait(driver, 65).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='navigator_pages']"))).click()
x=1
y = len(driver.find_elements_by_class_name('moc-viewer__steps-overview-item-internal'))
print(y)
a=[]
while x <= y:
	
	driver.find_element_by_class_name('moc-viewer__steps-overview-input').click()
	driver.find_element_by_class_name('moc-viewer__steps-overview-input').clear()
	driver.find_element_by_class_name('moc-viewer__steps-overview-input').send_keys(x)
	driver.find_element_by_class_name('btn--cta').click()
	#time.sleep(.3)
	elements = driver.find_elements_by_class_name('moc-viewer__part-item-meta')
	for e in elements:
		c=[]
		for b in e.text.splitlines():
			if b[:1] == 'x':
				b = b[1:]
			c.append(b)
		if c[0] != 'Submodel':
			a.append(c)
	WebDriverWait(driver, 65).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='navigator_pages']"))).click()
	x += 1
print(a)


data = pd.DataFrame(a)
data.to_csv(PName + " - Parts.csv", index=False, header=False)
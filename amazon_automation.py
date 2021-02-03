from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.amazon.co.uk/')
driver.maximize_window()

cookies = driver.find_element_by_xpath('//*[@id="sp-cc-accept"]')
cookies.click()


search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.click()
search.send_keys('kawasaki ER-6N')

clickSearch = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
clickSearch.click()

stars = driver.find_element_by_xpath('//*[@id="p_72/419153031"]/span/a/section/i')
stars.click()
driver.implicitly_wait(20)

sort = driver.find_element_by_xpath('//*[@id="a-autoid-4-announce"]/span[2]')
sort.click()
driver.implicitly_wait(20)

lowToHigh = driver.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
lowToHigh.click()

print('The automation is completed ! Check the products !')



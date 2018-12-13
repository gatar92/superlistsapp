from selenium import webdriver
#from selenium.webdriver.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('pat')

browser = webdriver.Firefox(executable_path=r'/Users/Pawel/.local/bin/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib



# loading broswer
global driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# options = webdriver.ChromeOptions()
 
# options.add_argument('headless')
 
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
options = webdriver.ChromeOptions()
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
driver.maximize_window()

# login
URL = "https://my.uic.edu/uPortal/f/welcome/normal/render.uP"



driver.get(URL)
driver.implicitly_wait(40)
driver.find_element(By.XPATH, "//span[a/@href='https://my.uic.edu/Shibboleth.sso/Login?target=https://my.uic.edu/uPortal/Login']").click()
driver.find_element(By.ID, "https://shibboleth.uic.edu/shibboleth").click()
driver.find_element(By.NAME, "Select").click()
driver.find_element(By.ID,'UserID').send_keys('vbatch2')
driver.find_element(By.ID,'password').send_keys('Parni$UDCz3027714')

#going to registration page
driver.find_element(By.ID,'disable-on-click').click()
driver.find_element(By.XPATH,"//span[text()='Registration/View Classes -  XE Registration']").click()
time.sleep(1)
handles = driver.window_handles
size = len(handles)
for x in range(size):
  if handles[x] != driver.current_window_handle:
    driver.switch_to.window(handles[x])

#going to fall of the registration page
driver.find_element(By.XPATH,"//span[text()='Register for Classes']").click()
driver.find_element(By.ID,'https://shibboleth.uic.edu/shibboleth').click()
driver.find_element(By.NAME ,"Select").click()
driver.find_element(By.XPATH,"//span[@role = 'presentation']").click()
driver.find_element(By.XPATH,"//div[text()='Fall 2022 - Chicago']").click()
driver.find_element(By.XPATH,"//button[@type='button']").click()
# driver.find_element(By.XPATH, "//input[@displaytitle='Subject']").send_keys('Computer Science')
time.sleep(1)
courseList = ['Information Retrieval', 'Causal Inference and Learning']

#iterating for the subjects I need
while True:
  # time.sleep(30)
  for i in courseList:
    time.sleep(3)
    driver.find_element(By.NAME,"txt_courseTitle").clear()
    driver.find_element(By.NAME,"txt_courseTitle").send_keys(i)
    driver.find_element(By.XPATH,"//div[@title='Toggle lower panel (Ctrl + Alt + V)']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[text()='Search']").click()
    time.sleep(1)
    if i == 'Information Retrieval':


      element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//td[@data-id='3228361' and @data-property ='status']")))
      element = element.get_attribute('title')
      print('111111',element[1:5])
      if element[1:5] != 'FULL':
        print('11111111')
        driver.find_element(By.XPATH,"//td[@data-id='3228361' and @xe-field ='add']").click()
        driver.find_element(By.XPATH,"//button[text()='Submit']").click()
    # elif i == 'An Introduction to Quantum Computing':
    #   element = driver.find_element(By.XPATH,"//td[@data-id='3231078' and @data-property ='status']").get_attribute('title')
    #   print('22222',element[1:5])
    #   if element[1:5] != 'FULL':
    #     print('2222222222')
    #     driver.find_element(By.XPATH,"//td[@data-id='3231078' and @xe-field ='add']").click()
          # driver.find_element(By.XPATH,"//button[text()='Submit']").click()
    #     [;'
    # /.]
    # elif i == 'Data Mining and Text Mining':
      # element = driver.find_element(By.XPATH,"//td[@data-id='3114810' and @data-property ='status']").get_attribute('title')
      # print('3333',element[1:5])
      # if element[1:5] != 'FULL':
      #   print('333333333')
      #   driver.find_element(By.XPATH,"//td[@data-id='3114810' and @xe-field ='add']").click()
      #   time.sleep(3)
      #   driver.find_element(By.XPATH, "//div[@id = 's2id_action-38903-ddl']").click()
      #   driver.find_element(By.XPATH, "//div[text()='Web Drop Course']").click()
      #   driver.find_element(By.XPATH,"//button[text()='Submit']").click()
    else:
      element = driver.find_element(By.XPATH,"//td[@data-id='3125911' and @data-property ='status']").get_attribute('title')
      print('444444',element[1:5])
      if element[1:5] != 'FULL':
        print('4444444')
        driver.find_element(By.XPATH,"//td[@data-id='3125911' and @xe-field ='add']").click()
        driver.find_element(By.XPATH,"//button[text()='Submit']").click()


    
    # sending email if the registration is done
    # element = driver.find_element(By.ID,'registeredHours')
    # print(element)
    # print(element.text)
    # if int(driver.find_element(By.ID,'registeredHours').text) > 12:
    #   recipient = "venkatalaxmimounika@gmail.com" #receives mail address

    #   message = "registration is done for" + i  #message to be send


    #   def SendEmail(recipient , message):
    #       server = smtplib.SMTP("smtp.gmail.com" , 587)  # 587 = port number
    #       server.ehlo() # check the smtp connection 
    #       server.starttls()  # start the conection 
    #       server.login("quantumcomputing56@gmail.com" , "Computing56Quantum")  
    #       server.sendmail("quantumcomputing56@gmail.com" , recipient , message)
    #       server.close() 
          

    #   SendEmail(recipient , message)
    
    time.sleep(2)
    driver.find_element(By.ID, "search-again-button").click()
  

from selenium import webdriver
import time
import threading

g_num = 0

def job(num):
    global g_num 
    browser = webdriver.Firefox()
    browser.get('http://vm1.rsx.com.tw/web/user.php')

    account='aaa'
    password='aaaaaa'
    time.sleep(2)
    inputElement = browser.find_element_by_name("username")
    inputElement.send_keys(account)
    inputElement = browser.find_element_by_name("password")
    inputElement.send_keys(password)
    inputElement.submit()

    time.sleep(3)
    browser.find_element_by_link_text("簡訊發送").click()
    time.sleep(10)

    for i in range(0,10000):
     inputElement = browser.find_element_by_name("phone")
     inputElement.send_keys("0972073013")
     inputElement = browser.find_element_by_name("message")
     mutex.acquire()
     inputElement.send_keys("thread:"+str(num)+" ""test "+str(g_num))
     g_num=g_num+1
     mutex.release()
     print("thread:"+str(num)+" ""test "+str(g_num))
     inputElement.submit()
     time.sleep(3)
     browser.switch_to_alert().accept() 
     ##time.sleep(3)
     
     
     
    print("done")
    
mutex = threading.Lock()     
threads = []
for i in range(5):
  threads.append(threading.Thread(target = job, args = (i,)))
  threads[i].start()

for i in range(5):
  threads[i].join()

print("Done.")
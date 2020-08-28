from wabot.driver_cls import waDriver
import time
from bs4 import BeautifulSoup

def chk(content):
  soup = BeautifulSoup(content, 'html.parser')
  
  if 'Keep me signed in' in soup.text:
    return 'login_req'
  elif 'Trying to reach phone' in soup.text:
    return 'connect_internet_boss'
  elif 'Search or start new chat' in soup.text:
    return 'logged_in'
  elif 'Use Here' in soup.text:
    self.driver.find_element_by_xpath('//div[text()="Use Here"]').click()
    print('use_here_login')
    return 'use_here_login'
  else:
    print('somthing went wrong')
    return 'somthing went wrong'


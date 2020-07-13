from selenium import webdriver
import time

class InstaBot:
  def __init__(self, username, pw):
    self.username = username
    self.driver = webdriver.Firefox()
    self.driver.get("https://www.instagram.com/?hl=en")
    time.sleep(3)
    self.driver.find_element_by_xpath("//input[@name=\'username\']").send_keys(username)
    self.driver.find_element_by_xpath("//input[@name=\'password\']").send_keys(pw)
    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
    time.sleep(3)
    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    time.sleep(3)
    self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    time.sleep(3)

  def get_unfollowers(self):
    self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
    time.sleep(3)
    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    following = self._get_names()
    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    followers = self._get_names()
    unfollower = [user for user in following if user not in followers]
    with open('names.txt', 'w') as filehandle:
      for listitem in unfollower:
        filehandle.write('%s\n' % listitem)

  def _get_names(self):
    time.sleep(2)
    scrollBody  = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    last_ht, ht = 0, 1
    while last_ht != ht:
      last_ht = ht
      time.sleep(1)
      ht = self.driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight', scrollBody)
    links = scrollBody.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
    self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
    return names


myBot = InstaBot('your_username', 'your_password')
myBot.get_unfollowers()

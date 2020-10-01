from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By




browser = webdriver.Firefox()

url = "https://forms.office.com/Pages/ResponsePage.aspx?id=Nyg_QZRhGkSW1f1SXyNTPylDq2Z-UmRBpu-0C3HkDmtUN0NKSElSNUwxSVYxSkIyS0dZVllYN0lTVCQlQCN0PWcu"

browser.get(url)

print("\nAre you your you want to submit? (y/n)")
Sure_to_Submit = input(": ").upper()

if Sure_to_Submit == "N":
  browser.close()
  quit()
else:
  pass

def Login():

    Email = "ding-han.yan@student.bodwell.edu"
    Password = "Seandork0919"

    try:
      Login_Email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]'))
      )
      Login_Email.send_keys(Email)
    
    except:
      print("can't find the element")

    try:
      Btn_Next = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
      )
      Btn_Next.click()

    except:
      print("BTN next wetn wrong")

    sleep(1)

    try:
      Login_Password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "i0118"))
      )
      Login_Password.send_keys(Password)
    except:
      print("Password SEND key went wrong")
    
   
    sleep(2)

    try:
      Btn_Sign_in = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
      )
      Btn_Sign_in.click()
    except:
      print("BTN login in went wrong")

    sleep(1)

    try:
      Btn_Yes = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
      )
      Btn_Yes.click()
    except:
      print("BTN Yes went wrong")

def Write_Form():

  try:
    None_of_Above = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[14]/div/label/input"))
    )
    None_of_Above.click()
  except:
    print("OPtion 1 didn't work")

  try:
    Option_No = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/input"))
    )
    Option_No.click()
  except:
    print("Option two didn't work")

  if Sure_to_Submit == "Y":
    try:
      Btn_Submit = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div/div[2]/div[3]/div[1]/button/div"))
      )
      
      Btn_Submit.click()
      
    except:
      print("BTN submit didn't work")
  else:
    print("Ok I won't submit")


def Close():
  browser.close()
  quit()

Login()
Write_Form()
Close()

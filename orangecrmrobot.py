import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_Login_Negatif(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("S") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("skl") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()

        response_message = driver.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Invalid credentials')
 
    
    def test_Login_Negatif by No password(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Testq37") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()

        response_message = driver.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Required')

    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()

    response_message = driver.find_element(By.ID,"menu_admin_viewAdminModule").text
        self.assertEqual(response_message, 'Admin')
        


    def test_Login_Positif by new account(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Testqa37") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("Jacob2018!") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()

        response_message = driver.find_element(By.ID,"menu_admin_viewAdminModule").text
        self.assertEqual(response_message, 'Admin')

    def test_Job(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"menu_admin_viewAdminModule").click()
        driver.find_element(By.ID,"menu_admin_Job").click()
        driver.find_element(By.ID,"menu_admin_viewJobTitleList").click()
        time.sleep(3)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID,"jobTitle_jobTitle").send_keys("jobjobjobjob")

    def test_Add_Employee by No First name (self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtFirstName").send_keys("")
        driver.find_element(By.ID,"txtMiddleName").send_keys("QA37")
        driver.find_element(By.ID,"txtLastName"). send_keys("tester")
        driver.find_element(By.ID,"txtEmployeeName").send_keys("tester")
        time.sleep(3)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
    response_message = driver.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Required')    

    def test_Add_Employee by No Middle name (self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtFirstName").send_keys("Testqa37")
        driver.find_element(By.ID,"txtMiddleName").send_keys("")
        driver.find_element(By.ID,"txtLastName"). send_keys("tester")
        driver.find_element(By.ID,"txtEmployeeName").send_keys("tester")
        time.sleep(3)
        driver.find_element(By.ID,"btnSave").click()
        
    response_message = driver.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Required')
    
    def test_Add_Employee by No Last name (self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtFirstName").send_keys("Testqa37")
        driver.find_element(By.ID,"txtMiddleName").send_keys("QA")
        driver.find_element(By.ID,"txtLastName"). send_keys("")
        driver.find_element(By.ID,"txtEmployeeName").send_keys("tester")
        time.sleep(3)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
    response_message = driver.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Required')

    def test_Add_Employee by No Employee Name (self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtFirstName").send_keys("Testqa37")
        driver.find_element(By.ID,"txtMiddleName").send_keys("QA")
        driver.find_element(By.ID,"txtLastName"). send_keys("tester")
        driver.find_element(By.ID,"txtEmployeeName").send_keys("")
        time.sleep(3)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
    response_message = driver.find_element(By.ID,"Create Login Details").text
        self.assertEqual(response_message, 'Required')

    

    
        

unittest.main()
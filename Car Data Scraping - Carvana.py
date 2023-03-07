import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



url = "https://www.carvana.com/cars?email-capture="
# 
driverpath = r"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
driver = webdriver.Edge(driverpath)
driver.get(url)

#get the number of pages
pages = int(((driver.find_element(By.ID,"pagination").get_attribute("textContent")).replace("Next","")).split(" ")[-1])


#data to webscrape
year =[]
make = []
model = []
trim = []
miles = []
price = []
carUrls = []
pic =[]
page = []


#for loop to get through all the results
for i in range(1,pages+1):
    url = "https://www.carvana.com/cars?email-capture=&page=" + str(i)
    driver.get(url)

    cars = driver.find_elements(By.CLASS_NAME,"result-tile")

    loc = [1,2,3,4,5,7,8,9,10,11,12,13,14,16,17,19,20,21,22,23]
    
    j = 0 #iterator
    print(len(cars))
    for car in cars:
        try:
            yearMake = car.find_element(By.CLASS_NAME, "year-make").get_attribute("textContent").split(" ")
            trimModel = car.find_element(By.CLASS_NAME, "trim-mileage").get_attribute("textContent").split(" ")
            fullModel = car.find_element(By.CLASS_NAME, "trim-mileage").get_attribute("textContent").split("•")
            try:
                carPrice = (car.find_element(By.XPATH, "//*[@id='results-section']/div[" + str(j) +"]/a/div/div[2]/div[2]/div/div").get_attribute("textContent")).replace("$","") 
            except:
                j+=1
                carPrice = (car.find_element(By.XPATH, "//*[@id='results-section']/div[" + str(j) +"]/a/div/div[2]/div[2]/div/div").get_attribute("textContent")).replace("$","") 
            
            carUrl = (car.find_element(By.TAG_NAME, "a").get_attribute('href'))
            carPic = (car.find_element(By.TAG_NAME, "img").get_attribute('src'))
            year.append(yearMake[0])
            make.append(yearMake[1])
            model.append(yearMake[2])
            trim.append(fullModel[0])
            miles.append(trimModel[-2])
            price.append(carPrice)
            carUrls.append(carUrl)
            page.append(i)
            


            pic.append(carPic)
            j+=1
        except:
            print("missing")



data = pd.DataFrame(zip(year,make,model,trim,miles,price,carUrls,pic,page), columns = ["year","make","model", "trim", "miles", "price", "url","pic","page"])

data.to_excel("Carvana Data Set - Los Angeles, CA.xlsx")





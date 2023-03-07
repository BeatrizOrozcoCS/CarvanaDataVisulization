import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import json
import time
file = "Carvana Data Set - Los Angeles, CA.xlsx"
url = "https://www.carvana.com/vehicle/"

#data to webscrape - more detailed passthorugh


#get urls
data = pd.read_excel(file).drop_duplicates(subset = ["url"])
urlList = data["url"].to_list()
print(len(urlList))
#basic info to collect
year = []
make = []
model = []
trim = []
mileage = []
price = []
bodyType = [] 
doors = []
driveTrain = []
engine = []
fuelType = []
mpgCity =[]
mpgHWY = []
seating = []
transmission = []
interiorColor = []
exteriorColor = []
genFacts =[]
highlights =[]
locationAddress = []
locationCity = []
locationState = []
locationZip = []
fairMarketValue = []
kbbValue =[]
basicWarrantyMiles = []
basicWarrantyMonths = []
driveTrainWarrantyMiles = []
driveTrainWarrantyMonths = []
saleStatus = []
vin = []


# selnium
driverpath = r"C:\Users\Orozc\OneDrive\My Documents\Projects\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(driverpath)

# iterate through the list
for i in range(0,10):
    try:
        print(str(i))
        driver.get(str(urlList[i]))
        #check for this
       
        car = json.loads(driver.find_element(By.XPATH, "//*[@id='__NEXT_DATA__']").get_attribute("textContent"))

        try:
            carBodyType=car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["bodyType"]
        except:
            carBodyType="NA"
            
        try:
            carDoors = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["doors"]
        except:
            carDoors = "NA"
            
        try:
            carDriveTrain = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["drivetrainDescription"]
        except:
            carDriveTrain = "NA"
            
        try:
            carEngine = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["engineDescription"]
        except:
            carEnginer = "NA"
            
        try:
            carExteriorColor = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["exteriorColor"]
        except:
            carExteriorColor = "NA"
            
        try:
            carFairMarketValue = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["fairMarketValue"]
        except:
            carFairMarketValue = "NA"
        try:
            carFuelType = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["fuelDescription"]
        except:
            carFuelType = "NA"
        #generalized facts
        carGenFacts = ""
        try:
            for j in range(0,len(car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["generalizedFacets"])):
                if j == len(car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["generalizedFacets"])-1:
                    carGenFacts = carGenFacts + car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["generalizedFacets"][j]["facetName"]
                else:
                    carGenFacts = carGenFacts+ car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["generalizedFacets"][j]["facetName"] + ","
        except:
            carGenFacts = "NA"
        #highlights
        carHighlights =""
        try:
            for j in range(0,len(car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["highlights"])):
                if j == len(car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["highlights"])-1:
                    carHighlights += car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["highlights"][j]["tagKey"]
                else:
                    carHighlights += car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["highlights"][j]["tagKey"] + ","
        except:
            carHighlights = "NA"
            

        try:
            carInteriorColor = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["interiorColor"]
        except:
            carInteriorColor = "NA"
            
        try:
            carKBBValue =car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["kbbValue"]
        except:
            carKBBValue ="NA"
        try:
            carLocationAddress = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["location"]["addressLine1"]
        except:
            carLocationAddress = "NA"
        try:
            carLocationCity = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["location"]["city"]
        except:
            carLocationCity = "NA"
        try:
            carLocationState = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["location"]["stateAbbreviation"]
        except:
            carLocationState ="NA"
        try:
            carLocationZip = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["location"]["zip5"]
        except:
            carLocationZip ="NA"
        try:   
            carMake = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["make"]
        except:
            carMake = "NA"
        
        try:
            carBasicWarrantyMiles = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["manufacturerBasicWarrantyMiles"]
        except:
            carBasicWarrantyMiles ="NA"
        
        try:
            carBasicWarrantyMonths = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["manufacturerBasicWarrantyMonths"]
        except:
            carBasicWarrantyMonths ="NA"
            
        try:
            carDriveTrainWarrantyMiles = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["manufacturerDriveTrainWarrantyMiles"]
        except:
            carDriveTrainWarrantyMiles ="NA"
            
        try:
            carDriveTrainWarrantyMonths = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["manufacturerDriveTrainWarrantyMonths"]
        except:
            carDriveTrainWarrantyMonths ="NA"

        try:
            carMileage = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["mileage"]
        except:
            carMileage = "NA"
            
        try:
            carModel = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["model"]
        except:
            carModel = "NA"
            
        try:
            carMPGCity =car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["mpgCity"]
            carMPGHWY = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["mpgHighway"]
        except:
            try:
                carMPGCity =car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["evMpgeCity"]
                carMPGHWY = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["evMpgeHighway"]
            except:
                carMPGCity = "NA"
                carMPGHWY = "NA"

        try:
            carPrice = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["price"]
        except:
            carPrice = "NA"
        try:
            carSaleStatus = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["saleStatus"]
        except:
            carSaleStatus ="NA"
        try:
            carSeating = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["seating"]
        except:
            carSeating ="NA"
        try:   
            carTransmission = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["transmission"]
        except:
            carTransmission = "NA"
        try:
            carTrim = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["trim"]
        except:
            carTrim = "NA"
        try:
            carVin =car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["vin"]
        except:
            carVin = "NA"
        try:
            carYear = car["props"]["pageProps"]["initialState"]["vehicle"]["details"]["year"]
        except:
            carYear = "NA"

        year.append(carYear)
        make.append(carMake)
        model.append(carModel)
        trim.append(carTrim)
        mileage.append(carMileage)
        price.append(carPrice)
        bodyType.append(carBodyType)
        doors.append(carDoors)
        driveTrain.append(carDriveTrain)
        engine.append(carEngine)
        fuelType.append(carFuelType)
        mpgCity.append(carMPGCity)
        mpgHWY.append(carMPGHWY)
        seating.append(carSeating)
        transmission.append(carTransmission)
        interiorColor.append(carInteriorColor)
        exteriorColor.append(carExteriorColor)
        genFacts.append(carGenFacts)
        highlights.append(carHighlights)
        locationAddress.append(carLocationAddress)
        locationCity.append(carLocationCity)
        locationState.append(carLocationState)
        locationZip.append(carLocationZip)
        fairMarketValue.append(carFairMarketValue)
        kbbValue.append(carKBBValue)
        basicWarrantyMiles.append(carBasicWarrantyMiles)
        basicWarrantyMonths.append(carBasicWarrantyMonths)
        driveTrainWarrantyMiles.append(carDriveTrainWarrantyMiles)
        driveTrainWarrantyMonths.append(carDriveTrainWarrantyMonths)
        saleStatus.append(carSaleStatus)
        vin.append(carVin)


       
        time.sleep(4)
       
    except:
        year.append("FAIL")
        make.append("FAIL")
        model.append("FAIL")
        trim.append("FAIL")
        mileage.append("FAIL")
        price.append("FAIL")
        bodyType.append("FAIL")
        doors.append("FAIL")
        driveTrain.append("FAIL")
        engine.append("FAIL")
        fuelType.append("FAIL")
        mpgCity.append("FAIL")
        mpgHWY.append("FAIL")
        seating.append("FAIL")
        transmission.append("FAIL")
        interiorColor.append("FAIL")
        exteriorColor.append("FAIL")
        genFacts.append("FAIL")
        highlights.append("FAIL")
        locationAddress.append("FAIL")
        locationCity.append("FAIL")
        locationState.append("FAIL")
        locationZip.append("FAIL")
        fairMarketValue.append("FAIL")
        kbbValue.append("FAIL")
        basicWarrantyMiles.append("FAIL")
        basicWarrantyMonths.append("FAIL")
        driveTrainWarrantyMiles.append("FAIL")
        driveTrainWarrantyMonths.append("FAIL")
        saleStatus.append("FAIL")
        vin.append("FAIL")
        
data = pd.DataFrame(zip(year,make,
model,trim,mileage,
price,
bodyType,
doors,
driveTrain,
engine,
fuelType,
mpgCity,
mpgHWY,
seating,
transmission,
interiorColor,
exteriorColor,
genFacts,
highlights,
locationAddress,
locationCity,
locationState,
locationZip,
fairMarketValue,
kbbValue,
basicWarrantyMiles,
basicWarrantyMonths,
driveTrainWarrantyMiles,
driveTrainWarrantyMonths,
saleStatus,
vin,urlList), columns = ["year",
"make",
"model",
"trim",
"mileage",
"price",
"bodyType",
"doors",
"driveTrain",
"engine",
"fuelType",
"mpgCity",
"mpgHWY",
"seating",
"transmission",
"interiorColor",
"exteriorColor",
"genFacts",
"highlights",
"locationAddress",
"locationCity",
"locationState",
"locationZip",
"fairMarketValue",
"kbbValue",
"basicWarrantyMiles",
"basicWarrantyMonths",
"driveTrainWarrantyMiles",
"driveTrainWarrantyMonths",
"saleStatus",
"vin","url"])
data.to_excel("Test.xlsx")

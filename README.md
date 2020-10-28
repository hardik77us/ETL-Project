# ETL-Project - US Vehicle Access
![](https://github.com/hardik77us/ETL-Project/blob/main/Resources/car_dealership.png)

## Team Members: Hardik Vadel, Janette Chairez, Charles Robinson, Shimsy Varkey

### Roles: 
* Hardik Vadel – Data collector
*	Shimsy Varkey – Data Transformer
*	Charles Robinson – Relational Manager
*	Janette Chairez – Flask API Creator

### Datasets we used:
* Census CSV file: 

The census csv was used to retrieve data corresponding to CENSUSTRACT - for the unique census tract (our primary key), State, County, POP2010 - population count from 2010, OHU2010 - Number of Housing units for 2010, MedianFamilyIncome - Median family income, TractHUNV - Housing units without vehicles , PovertyRate - Poverty rate, LAT - Latitude, LON - Longitude. 


* Tract_Lat_lon CSV file:

This file was used to retrieve the latitude and longitude corresponsing to the unique census tract

* googlemaps API:

The googlemaps API was used to find the nearest car dealers to a latitude longitude. 

### Extraction

We read both the CSV files and combined them. Also called the googlemaps API. Since the CSV files had over 150 columns we had to find out what columns we required for our analysis. Since there was massive amount of data, we decided to go for information pertaining to only one state. We chose Delaware.

### Transformation

Inorder to make the data that we retrieved useful, we needed to look through all the columns and then transform it. So, from 150 columns we narrowed it to 10 columns such as CENSUSTRACT - for the unique census tract (our primary key), State, County, POP2010 - population count from 2010, OHU2010 - Number of Housing units for 2010, MedianFamilyIncome - Median family income, TractHUNV - Housing units without vehicles , PovertyRate - Poverty rate, LAT - Latitude, LON - Longitude. Renamed the columns to names we could easily understand. From the googlemaps API, we retrieved the nearest car dealership to the latitude and longitude and added it to the above combined table. 

### Load

We used SQL as our database and created the tables and primary key(census tract) for the data. We used SQL because we were dealing with structured datda with a consistent schema. Also because we were using cosistent data. At present we didnt use any complex queries, however we could use SQL for it if required later. We were also not expecting any scalability issues. The tables we created are **CensusData** , **Tract_lat_lon** and **Data**. The censusData had census tract (our primary key), State, County, POP2010 - population count from 2010, OHU2010 - Number of Housing units for 2010, MedianFamilyIncome - Median family income, PovertyRate - Poverty rate. The Tract_lat_lon has the census tract, latitude and longitude. The data table has census tract, state and county. 

The following is an image of the schema we used:

![](https://github.com/hardik77us/ETL-Project/blob/main/Resources/schema.png)

We used flask to build a route to execute a query to our database and return results. We had an **index(Welcome) page**, **population**, the **vehicle rate**, **name of dealership**. The Welcome page shows you the list of the links to the other pages. The population shows the total population and the total housing units. The Vehicle rate shows the total housing units and the units without vehicles. The dealership page shows the list of the dealerships and the corresponding latitude and longitude. 

### Use for above analysis:

We are looking to find out if there is a relationship between the economic situation per household to vehicle ownership based on the number of dealerships in the area. Also, we were hoping to use the data by a prospective car dealer to study the area to see if it will be profitable for them to start a dealership in the area considering the number of dealers in the latitude longitude and also the income, poverty rate and number of housing units.  





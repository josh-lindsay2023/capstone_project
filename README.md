# capstone_project

Say you wish to have a data source keeping track of immigration statistics on a monthly basis. However you may also wish to examine any underlying trends and for this reason you wish to be able to extraopolate data on the cities they are immigrating to or if climate and temperature has any effect. This data could be a monthly updated dashboard allowing any changes etc to be discovered and analysed. It will be aggregated from a number of sources and combined in one data model. The process of it's creation and what it includes is described below. 

## sources
Four datasets are combined together in this data model to give an overall comprehensive view of the immigration statistics. 
- I94 Immigration statistics : From the US National Trade and Tourism department collating details of immigrant arrivals in the U.S. In this use case we believe that the data will form part of a dashboard which is updated on a monthly basis so we will subset the data to April 2016.
- Demographic data : From the US Census Bureau's 2015 American Community Survey, containing information about the demographics of all US cities and census-designated places with a population greater or equal to 65,000. Therefore we believe the data is timely enough to be relevant to the immigration data.
- Temperature Data : Data sourced from Kaggle, repackaged from Berkeley Earth which looks at global temoperature on a daily basis at a country state and city level.
- State Code data : Sourced from https://scottontechnology.com/list-of-50-us-states-in-excel/#:~:text=Downloadable%20Excel%20%28.csv%29%20lists%20of%20the%2050,US%20State%20names%2C%20abbreviations%2C%20and%20AP%20style%20abbreviations. containing all of the stae names and their relevant state codes.

## Data Cleaning

The pre-processing steps carried out to make the data suitable to build the model from are detailed step by step in the project notebook. Some main ones are
- Add statename to immigrant data using state code and state code data.
- Reduce temperature dataset to US state data and average on monthly basis.
- Zero checks etc.
Landing tables should be constructed to ensure all of the data is loaded correctly, from which our model could be made.

## Model 
The model which was chosen to be appropriate for this data was the star schema, with the immigrant data as the central fact table. Visa, temperature and demogrpahic can then add supplementrary data as seperate dimension tables. This is better illustrated via the table below. 
|Table_Name|Columns|Table_type|Info|
|---|---|---|---|
|Immigrants_df|**cicid**, i94yr, i94mon, i94cit, i94res, i94port, arrdate, i94mode, i94addr, depdate, i94bir, i94visa, count, dtatdfile, occup, entdepa, entdepu, matflag, biryear, dtaddto, gender, insum, airline, admnum, fltno, State_name_lower, temp_id| Fact Table| Information on immigration details |
|Visa_df| **i94visa**, visatype| Dimension table| Information on visas and their corresponding type|
|Temperatures_df| **temp_id**, Average_temperature, Average_temperature_uncertainty, State, Country, Year, Month| Dimension Table| Information around the average temperature in April 2013 for U.S states| 
|Demographics_df| **City, State**,	Median Age,	Male Population, Female Population, Total Population, Number of Veterans, Foreign-born, Average Household Size,	State Code,	Race, Count, Race_American Indian and Alaska Native, Race_Asian, Race_Black or African-American, Race_Hispanic or Latino, 	Race_White,	count_hispanic or latino, count_white, count_asian,	count_black or african-american,	count_american indian and alaska native| Dimension table| Information on demogrpahics of US cities|

The model is created using PostgreSQL due to the limited size of the data for this POC. As in future we would want to use larger quantities of data which would update on a monthly basis and EMR cluster with spark could be used. An AWS glue job would also be appropriate. For the scheduling aspect, airflow would be the suggested tool. 

## Other Scenarios 

Although the model presented here is appropriate for the use case and POC presented here there are multiple other tools which could be used if there were chnages to the environment. Some of these include
 - **The size of the data is increased by 100x** : In this case spark would have tobe used. Additionally an Amazon EMR cluster should be used to run the ETL to del with the increased size. This offers basically unlimited computing power as it scales in and out depending on the need of the model. The data can also be uploaded directly to S3.
 - **The Pipelines have to be run at 7am on a daily basis**: This can be easily set up using Airflow. A DAG can be set up with each step of the ETL included within it. A scheduler is then set up to ensure it is ran at the times needed without human intervention.
 - **The Database needs too be accessed by 100+ people** : Cloud capabilities on AWS allows large amounts of people to access the same data remotely and allows the root user to have control over their permissions. Due to the large size of the data and number of people who require access, redshift may be the most ideal solution in this scenario.

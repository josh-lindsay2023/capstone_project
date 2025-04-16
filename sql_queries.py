create_demographics = '''
CREATE TABLE IF NOT EXISTS demo(
City VARCHAR,
State VARCHAR,
Median_Age FLOAT,
Male_Population FLOAT, 
Female_Population FLOAT,
Total_Population FLOAT,
Number_of_Veterans FLOAT,
Foreign_born FLOAT, 
Average_Household_Size FLOAT,
State_Code VARCHAR,
Race_American_Indian_and_Alaska_Native INT,
Race_Asian INT,
Race_Black_or_African_American INT,
Race_Hispanic_or_Latino INT,
Race_White INT,
count_hispanic_or_latino INT,
count_white INT,
count_asian INT,
count_black_or_african_american INT,
count_american_indian_and_alaska_native INT
);
'''

drop_demographics = "DROP TABLE IF EXISTS demo;"

demographic_insert = """
INSERT INTO demo(city, state, Median_age, Male_population, Female_population, Total_population, 
Number_of_Veterans, Foreign_born, Average_Household_Size, State_Code, Race_American_Indian_and_Alaska_Native, Race_Asian, Race_Black_or_African_American, Race_Hispanic_or_Latino, Race_White, count_hispanic_or_latino, count_white, count_asian, count_black_or_african_american, count_american_indian_and_alaska_native ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s);
"""

create_temp = '''
CREATE TABLE IF NOT EXISTS temp(
temp_id INT PRIMARY KEY,
Average_temperature FLOAT,
Average_temperature_uncertainty FLOAT,
State VARCHAR, 
Country VARCHAR,
Year INT,
Month INT
);
'''

drop_temp = "DROP TABLE IF EXISTS temp;"

temp_insert = """
INSERT INTO temp( temp_id, Average_temperature, Average_temperature_uncertainty, State, Country, Year, Month) VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

create_visa = '''
CREATE TABLE IF NOT EXISTS visa(
visa_id INT,
i94visa FLOAT,
visatype VARCHAR);
'''

drop_visa = "DROP TABLE IF EXISTS visa;"

visa_insert='''
INSERT INTO visa(visa_id,i94visa, visatype) VALUES (%s, %s, %s);
'''

create_i94 = '''
CREATE TABLE IF NOT EXISTS immigrant(
cicid FLOAT PRIMARY KEY, 
i94yr FLOAT,
i94mon FLOAT,
i94cit FLOAT,
i94res FLOAT,
i94port VARCHAR,
arrdate FLOAT,
i94mode FLOAT,
i94addr VARCHAR,
depdate FLOAT,
i94bir FLOAT,
i94visa FLOAT,
count FLOAT, 
dtatdfile FLOAT,
visa_post VARCHAR,
occup VARCHAR,
entdepa VARCHAR,
entdepd VARCHAR,
entdepu VARCHAR, 
matflag VARCHAR, 
biryear FLOAT,
dtaddto VARCHAR,
gender VARCHAR, 
insum VARCHAR, 
airline VARCHAR, 
admnum FLOAT,
fltno INT,
State_name_lower VARCHAR,
temp_id INT);
'''
drop_i94 = "DROP TABLE IF EXISTS immigrant"

i94_insert = '''
INSERT INTO immigrant(cicid, i94yr, i94mon, i94cit, i94res, i94port, arrdate, i94mode, i94addr, depdate, i94bir, i94visa, count, dtatdfile, visa_post, occup, entdepa, entdepd, entdepu, matflag, biryear, dtaddto, gender, insum, airline, admnum, fltno, State_name_lower, temp_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s);
'''


drop_table_queries = [drop_demographics, drop_temp, drop_visa ,drop_i94]
create_table_queries = [create_demographics, create_temp, create_visa, create_i94 ]

## Flight Data Tableau Story

Analyzed 2008 flight data and created several data visualizations.  
[Flight Data Tableau Public workbook](https://public.tableau.com/views/FlightDataModified/FlightDataAnalysis)

### Data

Information on United State flight delays and performance comes from RITA.

Name | Description
------------ | -------------
Month|1-12
DayOfWeek|1 (Monday) - 7 (Sunday)
UniqueCarrier|unique carrier code
ArrDelay|arrival delay, in minutes
Origin|origin IATA airport code
Dest|destination IATA airport code
Distance|in miles
Cancelled|was the flight cancelled?
CancellationCode|reason for cancellation (A = carrier, B = weather, C = NAS, D = security)
CarrierDelay|in minutes
WeatherDelay|in minutes
NASDelay|in minutes
SecurityDelay|in minutes
LateAircraftDelay|in minutes

Airport code and 'City, State' mapping for origin and destination airports.

Name | Description
------------ | -------------
AirportCode|3 letter airport code
CityState|'City, State' airport is located

### Questions to answer

##### Cancellations
1.	Which months and days of week are the most affected?
2.	Which reasons does it cause the most cancellations?
3.	Which airline has the most flight cancellations?
4.	Which airport has the most flight cancellations?

##### Delays
1.	Which airports are affected by weather?
2.	Which airline has the worst on-time performance?
3.	Does more flight distance cause delays?
4.	Which airport has the worst on-time performance?

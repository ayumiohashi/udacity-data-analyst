## FBI Gun Data

### Data

The data (Original source [Github](https://github.com/BuzzFeedNews/nics-firearm-background-checks/blob/master/README.md)) comes from the FBI's National Instant Criminal Background Check System. The NICS is used by to determine whether a prospective buyer is eligible to buy firearms or explosives. Gun shops call into this system to ensure that each customer does not have a criminal record or isn’t otherwise ineligible to make a purchase. The data has been supplemented with state level data from [census.gov](https://www.census.gov/).


* The NICS data `gun-data.csv` - contains the number of firearm checks by month, state, and type.

* The U.S. census data `us-census-data.csv` - contains several variables at the state level. Most variables just have one data point per state (2016), but a few have data for more than one year.

### Questions to answer

* Which states have had the highest growth in gun registrations?
* What census data is most associated with high gun per capita?

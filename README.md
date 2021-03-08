# real-estate

## Overview
This project looks for statistically significantly high local housing values after new sports franchises were established

## Analysis
Houses are valued by the FMAC seasonally-adjusted housing index (SA Index). Specifically, the difference between the city's SA Index and the USA's SA Index (SA Index Difference), to account for large changes in the US economy that affect housing values country-wide. Plots show the city SA Index, USA SA Index and SA Index Difference as a timeseries. A t-test is done on the SA Index Difference timeseries to find values where the SA Index Difference is statistically significant. The t-test 0.95 value is displayed as a horizontal line on the plot so the viewer can visualize which dates show statistically significant high values of the SA Index Difference. These dates can be evaluated to see if the fall shortly after teams were established in the given city.

## Workflow
CSV files are imported to fix city names to city FMAC API area codes, and get data for franchise relocations (year, city name, etc.)

SA Indices are pulled as a timeseries datafreame to construct plots

Plots are used to visualize:
* SA Index for the city as a time series
* SA Index for the USA as a time series
* The difference of the USA and city SA Indices as a time series
* The 0.95 statistical significance value of the SA Index Difference time series
* Dates that teams were established in the city (added manually in the powerpoint for team logo graphics and efficiency)

## Conclusions
* only 2 cities showed statistically significantly high SA Index Difference values within 10 years after franchise establishment
* Given that statistically significant values more frquently showed up in cities not shortly after franchise establishment, and given that thee are many other indistries making city economic effects, it seems that SA Index Differences were more frequently afftected by other city variables

![](images/capture.png)







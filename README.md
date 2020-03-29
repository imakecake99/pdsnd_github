Python code created 3rd March 2020, ReadMe created 5th March 2020.

Explore US Bikeshare Data project

Python is used to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington through an interactive experience in terminal where raw input is used to return statistical information.

Data Files:
* chicago.csv
* new_york_city.csv
* washington.csv

Python Files:
* bikeshare.py
* bikeshare_template.py

Code Snippets:  
* df.groupby(['Start Station','End Station']).size().idxmax()
  Sourced from stack overflow: https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python

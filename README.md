*This README.md file was generated on 03-04-23 by Madeleine Roberts*
# CAPP 30122 databased_project
Examining the Scope and Sentiment of Local Newspaper Coverage on the 2023 Primary Election's Mayoral Candidates in Chicago

## Authors
- [Abe Burton](https://github.com/abejburton)
- [Kathryn Link-Oberstar](https://github.com/klinkoberstar)
- [Lee-Or Bentovim](https://github.com/bentoviml)
- [Madeleine Roberts](https://github.com/MadeleineKRoberts) 

## Introduction
The project aims to analyze the press coverage of the Chicago's mayoral primary race and investigate how candidates are covered differently in local newspapers. We scraped/access the APIs of six different Chicago focused media sites to collect data. We then conducted data analysis to identify which topics are brought up most often and sentiment analysis to examine the tone of the articles. This analysis was preformed for the candidate overall, the paper overall and for the candidate in each paper.


## Installation

1. Clone the project repository
```bash
```

2. Install virtual environment and dependencies
```bash
poetry install
python3 -m pip install nltk
python3 pip install pyarrow
```

## Usage
Project must be run in the Poetry virtual environment. 
Upon completion of above installation requirements and within project terminal, initalize virual environment by running:
```bash
poetry shell
```
<br />


**Execute the project by running:**
```bash
python -m databased
```
<br />

You are then prompted to enter a singular digit execute a portion or the entire project, as seen below. 

```bash
To execute a desired aspect of the project please enter one of the following commands:
    1 - Open Data Visualization
    2 - Scrape All Newspapers
    3 - Clean Scraped Data
    4 - Conduct Data Analysyis
    5 - Run Entire Project Start to Finish (Scrape -> Clean -> Analyze -> Visualize)
    6 - End Program
    
Please input the number of your desired command:
```
<sub>example: "1[Return]" will run the data visualization</sub>

<br />

**Command 1 - Opens Data Visualization**
Renders a Dash to visualize the final results of the dataBASED project.

Note: This command will take about ?? minutes to render Dash.

<br />

**Command 2 - Executes All Scrapers/Proquest API**
Runs all scrapers and Proquest API to collect newpaper articles about Chicago's mayoral candidates. The retrieved data is then stored in JSON format and outputted to the databased/data folder.

Note: This command will take about 20 minutes to complete.

<br />

**Command 3 - Executes All Data Cleaning**
Runs data cleaning on all scraped data; strips stop words, normalizes case, and selects only sentences that refer to the candidate that is the subject of the article. The cleaned data is then stored in JSON format and outputted to the databased/data folder.

Note: this command will take about 1 minute to complete.

<br />


**Command 4 - Execute All Data Analysis**
Runs data analysis on cleaned candidate data

Note: this command will take about 35 minutes to complete. However, if you comment out lines 54 and 55 in basic_sentiment.py the command will execute in about 2 minutes. The completion of the JSON for overall newspaper sentiment will be prevented as a result of this.

<br />


**Command 5 - Execute Entire Project**
```bash
python -m databased
```
<sub>Note: this command will take about 35 minutes to complete. However, if you comment out lines 54 and 55 in basic_sentiment.py the command will execute in about 1 minute. The completion of the JSON for overall newspaper sentiment will be prevented as a result of this.</sub>
<br />


# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)



# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

This project analyzes past years data, specificially calculates two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.


# Approach

```flow
st=>start: Load Arguments
op0=>operation: Retrieve Input File 
cond1=>condition: Is file a .csv?
op1=>operation: Generate H1B Instance
op2=>operation: Read CSV
op3=>operation: Cleanse Data
op4=>operation: Count
e=>end: Save Result

st->op0->cond
cond(yes)->op1->op2->op3->op4->e
cond(no)->op0
```
​```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
​```


# Run Instructions

You can run the tool with the following command from within the `h1b_statistics` folder:

    h1b_statistics~$ ./run.sh 

On a success execution, the output files of `run.sh` will be in `output` folder:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications



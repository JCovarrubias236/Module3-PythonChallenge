# Module 3 - Python Challenge
This repository will be used for the Module 3 Python challenge.

## Description

I completed this project to test my Python scripting skills and analyze the financial records of my fictional company for the first challenge (PyBank). In the next challenge (PyPoll), I modernized the vote-counting process for a rural town.

For the PyBank challenge, I organized my analysis to print into a text file called output.txt. Within the txt file, I generated the total months of data, total net profit/loss, the average change month over month, and then the greatest increase and decrease in profits.

In the PyPoll challenge, which was similarly formatted to the PyBank challenge, I printed the output of the script into a text file called output.txt. Within the text file, I counted the total amount of votes in the election and printed a complete list of candidates who received votes along with the percentage of total votes and count of votes. Lastly, I presented the winner of the election based on the popular vote.

## Visuals
The attached screenshots are of the results of the project. They display the financial analysis from the PyBank challenge and the election results from the PyPoll challenge.

![image](https://github.com/JCovarrubias236/python-challenge/assets/151583321/63835d90-a56f-4603-b956-cb4fec4696fc)
![image](https://github.com/JCovarrubias236/python-challenge/assets/151583321/2cc9a217-7209-4cd3-a9c2-eb558706feb0)

## Usage

Feel free to download the files I provided to look over the Python script files.

Input the below modules for script files to run properly

```python
import os

import csv
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change/recommend.

Please make sure to update tests as appropriate.

## Authors and Acknowledgement

I solely worked on this project, however, I did utilize websites like Stack Overflow and Geeks for Geeks to complete some tasks that either I needed a refresher or we did not learn in our prior boot camp classes. 

I used the below link to refresh my knowledge of loop counters and how the syntax works for inputting the counter with a for loop. This was used in the PyBank financial analysis.

https://stackoverflow.com/questions/522563/how-to-access-the-index-value-in-a-for-loop

The next link I used was also for the PyBank financial analysis. This was another refresher for the .index function I used to help me find the dates for the greatest increase/decrease in changes.

https://www.geeksforgeeks.org/python-list-index/

The last outside source, found below, that I used was to help me find the set() function that looks over a list with one column and grabs the unique values. I used this set() function in the PyPoll challenge to find the complete list of candidates that were voted for.

https://stackoverflow.com/questions/29860727/how-to-get-non-repeated-elements-in-a-list

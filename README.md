# Logs-Analysis

Source code for logs analyzer by quering postgresql data base.

This is the third project of the full stack developer nanodegree which is a part of 
the One Million arab coders initiative

# Code structure

The code consists mainly of 4 functions the first three executes certain database queries 
and the fourth is used to print the output in a readable format.

The queries are used to answer these three questions :
1-  What are the most popular three articles of all time?
2- Who are the most popular article authors of all time?
3- On which days did more than 1% of requests lead to errors?

These database's link including the data used to answer these questions is provided in the usage section


# Usage

To run the code :

1- You need to install  Vagrant and VirtualBox softwares 

2- Then you need to clone this repo https://github.com/udacity/fullstack-nanodegree-vm. 

3- After that run Vagrant using the command vagrant up then vagrant ssh

4- After the installation you will have to download the db from this link 
  https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip and run the command 
  "psql -d news -f newsdata.sql" after unzipping this file in the vagrant directory
  
5- For complete installation process check the installation steps in the logs analysis project in the full stack developer
 nano degree along with the instructions at the end of lesson 2 in the Database and backend section

6- Run this file by the command `./log_analysis.py` or `python log_analysis.py`

7- Note that this script is written in python 2

# The Output

The output of this script is found in output.txt


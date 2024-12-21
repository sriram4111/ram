# AtilQ Sales Analysis Dashboard📊

An interactive dashboard analyzing sales data across various dimensions to provide actionable business insights.

AtliQ Hardware is a company which supplies computer hardware and peripherals to many of clients such as surge stores, Nomad stores etc. across India. AtliQ Hardware head office is situated in Delhi, India and they have many regional office through out the India.

Here's a quick glimpse of some noteworthy facts about AtilQ:

 ➡️ **Project Planning using AIMS Grid -**
    It is a project management tool which consists of four components-
    Purpose - (What to do exactly)
    Stackholder - (Who will be involved)
    End result - (What do you want to achieve)
    Success Criteria - (Cost optimization and time save)
    
**AIMS Grid -**

**1. Purpose** :- To unlock sales insights that are not visible before for the sales them for decision support and automate them to reduced manual time spent in data gathering.

**2. Stakeholders :-**
Sales Director
Marketing Team
Customer Service Team
Data and Analytics Team
IT
**3. End result** :- An automated dashboard providing quick and latest sights in order to support Data driven decision making.

**4. Success Criteria :-**
Dahboard uncovering sales order insights with latest data available
Sales team able to take better decisions and prove 10% cost saving of total spend.
Sales analysis stop data gathering manually in order to save 20% business time andreinvest it value added activity.

**Flowchart of project execution -**


![AtilQ_pic](https://github.com/user-attachments/assets/c5432643-bcad-4135-b4ea-d5b7512f37c5)


**##Data Analysis using MySQL :**

Completed the Data discovery and then used mySQL for data analysis.

SQL database dump is in db_dump.sql file above. Download db_dump.sql file to your local computer

Importing Data to MySQL workbench

![sql_1](https://github.com/user-attachments/assets/1ef8940f-19ff-4100-896d-4848e21b397e)
![sql_2](https://github.com/user-attachments/assets/52c33cd8-280b-4666-896e-08687a18e6ea)


The import of data is done from an already existing MySQL file. This file has to be loaded into MySQL workbench for further data analysis.

Analysis of data by looking into different tables and reflecting garbage values

We can see that garbage value that the table market cantains certain values which are incorrect.

SELECT * FROM sales.market;

And then we can check that transacation table we can see that ceratin negative value in amount which is not possible. and we can see that certain transactions are in USD. Hence, filtration of that is also needed by converting into INR.

SELECT * FROM sales.transactions;

Analysis of different SQL statement on data base

1.To find of all customers records

SELECT * FROM sales.customers;

2.To find total number of customers

SELECT count(*) From sales.customers;

3.To find transactions for Chennai market (market code for chennai is Mark001

SELECT * FROM sales.transactions where market_code='Mark001';

4.To find distrinct product codes that were sold in chennai

SELECT distinct product_code FROM sales.transactions where market_code='Mark001';

5.To find transactions for Chennai market (market code for chennai is Mark002

SELECT * FROM sales.transactions where market_code='Mark002';

6.To find distrinct product codes that were sold in mumbai

SELECT distinct product_code FROM sales.transactions where market_code='Mark002';

7.To find transactions where currency is US dollars

SELECT * from sales.transactions where currency="USD";

8.To find transactions in 2020 join by date table

SELECT sales.transactions.*, sales.date.* FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020;

8.To find transactions in 2019 join by date table

SELECT sales.transactions.*, sales.date.* FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2019;

9.To find total revenue in year 2020,

SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r";

10.To find total revenue in year 2019,

SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2019 and sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r";

11.To find total revenue in year 2020, January Month,

SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.date.month_name="January" and (sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r");

12.To find total revenue in year 2020, February Month,

SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.date.month_name="February" and (sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r");

13.To find total revenue in year 2019, January Month,

SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.date.month_name="January" and (sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r");

14.To find total revenue in year 2019, February Month,

SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.date.month_name="February" and (sales.transactions.currency="INR\r" or sales.transactions.currency="USD\r");

15.To find total revenue in year 2020 in Chennai

SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.transactions.market_code="Mark001";

16.To find total revenue in year 2020 in Mumbai

SELECT SUM(sales.transactions.sales_amount) FROM sales.transactions INNER JOIN sales.date ON sales.transactions.order_date=sales.date.date where sales.date.year=2020 and sales.transactions.market_code="Mark002";

Similarly, if we want different of any other particular city the market code of that city is used on the mysql workbench.



Data Source:

The dataset used for this analysis includes sales records from various outlets, detailing product characteristics and sales performance.


# Marketing Analysis using PowerBI, SQL, Python

## Project Overview

This project demonstrates a comprehensive workflow for analyzing marketing data, from raw data acquisition and cleaning to interactive visualization and insight generation. Leveraging a powerful combination of Python, SQL, and Power BI, the aim is to transform disparate marketing datasets into actionable intelligence, enabling data-driven decision-making.

## Project Goal:

The primary goal of this project is to create a robust and insightful marketing analytics solution that can help businesses understand customer behavior, campaign performance, and overall market trends. By cleaning, transforming, and visualizing data, the project provides a clear, interactive dashboard for key stakeholders.

## Technologies Used:

* **Python:** Utilized for advanced data cleaning and manipulation. Python's rich ecosystem of libraries (like Pandas - NLTK - Gender_guesser ) is instrumental in preparing raw data for analysis.
* **SQL (Structured Query Language):** Employed for relational data cleaning, transformation, and potentially data integration, ensuring data integrity and structure before visualization.
* **Power BI:** The core tool for data visualization and dashboard creation. Power BI is used to connect to the cleaned data, build data models, and design interactive dashboards that offer dynamic insights into marketing performance.

## Project Workflow:

1.  **Data Cleaning and Preprocessing (Python & SQL):**
    * Initial raw marketing datasets are ingested.
    * **Python scripts** are developed to identify and handle inconsistencies in gender column and to do a sentiment analysis using the customer rating and ReviewText column.
    * **SQL queries** are crafted to perform transformations, removing duplicates, handling the missing values, preparing the data into a structured and analyzable format suitable for reporting.

2.  **Data Modeling and Analysis:**
    * The cleaned and transformed data is loaded into Power BI.
    * Relationships between various data tables are established to create a robust data model, enabling cross-table analysis.
    * Measures and calculated columns are defined to derive key marketing metrics and KPIs (Key Performance Indicators).

3.  **Interactive Dashboard Development (Power BI):**
    * Compelling and intuitive visualizations are designed to represent marketing performance, customer demographics, campaign effectiveness, and other critical insights.
    * Interactive elements like filters, slicers, and drill-through capabilities are incorporated to allow users to explore data dynamically and answer specific business questions.

 # project steps

## 1- data cleaning using SQl
### 1- the customer and geography table :
#### the query
```sql
-- 1- cleaning the customer table and merge it with the geography table ---
SELECT 
         C.CustomerID,
		 C.CustomerName , 
		 C.Email , 
		 C.Gender , 
		 C.Age , 
		 G.Country , 
		 G.City 
FROM     
         customers as C 
Left join 
         geography AS G
on 
         C.GeographyID = G.GeographyID ;
```
### tables before the query : 
#### the customer table :
| CustomerID | CustomerName | Email | Gender | Age | GeographyID |
|---|---|---|---|---|---|
| 1 | Emma Anderson | emma.anderson@example.com | Male | 50 | 2 |
| 2 | Sarah Brown | sarah.brown@example.com | Female | 37 | 4 |
| 3 | Robert Hernandez | robert.hernandez@example.com | Female | 26 | 6 |
| 4 | David Garcia | david.garcia@example.com | Male | 25 | 8 |
| 5 | Emma Miller | emma.miller@example.com | Female | 41 | 4 |

#### the geography table : 
| GeographyID | Country | City |
|---|---|---|
| 1 | UK | London |
| 2 | Germany | Berlin |
| 3 | France | Paris |
| 4 | Spain | Madrid |
| 5 | Italy | Rome |

### output of the query :
| CustomerID | CustomerName | Email | Gender | Age | Country | City |
|---|---|---|---|---|---|---|
| 1 | Emma Anderson | emma.anderson@example.com | Male | 50 | Germany | Berlin |
| 2 | Sarah Brown | sarah.brown@example.com | Female | 37 | Spain | Madrid |
| 3 | Robert Hernandez | robert.hernandez@example.com | Female | 26 | Netherlands | Amsterdam |
| 4 | David Garcia | david.garcia@example.com | Male | 25 | Sweden | Stockholm |
| 5 | Emma Miller | emma.miller@example.com | Female | 41 | Spain | Madrid |

### 2- the product table
#### the query :
```sql
-- 2- cleaning the product table ---
SELECT top 5 * FROM products

SELECT 
       ProductID , 
	   ProductName , 
	   Price ,
CASE  
	   When Price < 50 THEN 'LOW'
	   When Price BETWEEN 50 and 200 THEN 'MEDIUM'
	   ELSE 'HIGH'
end  AS PriceCategory
FROM 
       products
```
### table before the query :
| ProductID | ProductName | Category | Price |
|---|---|---|---|
| 1 | Running Shoes | Sports | 223.75 |
| 2 | Fitness Tracker | Sports | 196.68 |
| 3 | Yoga Mat | Sports | 485.32 |
| 4 | Dumbbells | Sports | 26.21 |
| 5 | Soccer Ball | Sports | 41.26 |

### output of the query :
| ProductID | ProductName | Price | PriceCategory |
|---|---|---|---|
| 1 | Running Shoes | 223.75 | HIGH |
| 2 | Fitness Tracker | 196.68 | MEDIUM |
| 3 | Yoga Mat | 485.32 | HIGH |
| 4 | Dumbbells | 26.21 | LOW |
| 5 | Soccer Ball | 41.26 | LOW |
 
### 3- customer_reviews table
#### the query : 
```sql
SELECT 
           ReviewID , 
		   CustomerID,
		   ProductID , 
		   ReviewDate ,
		   Rating , 
		   Replace (ReviewText,'  ',' ') AS ReviewText
FROM       
           customer_reviews
```

### table before the query :

| ReviewID | CustomerID | ProductID | ReviewDate | Rating | ReviewText |
|---|---|---|---|---|---|
| 1 | 77 | 18 | 2023-12-23 | 3 | Average experience, nothing special. |
| 2 | 80 | 19 | 2024-12-25 | 5 | The quality is top-notch. |
| 3 | 50 | 13 | 2025-01-26 | 4 | Five stars for the quick delivery. |
| 4 | 78 | 15 | 2025-04-21 | 3 | Good quality, but could be cheaper. |
| 5 | 64 | 2 | 2023-07-16 | 3 | Average experience, nothing special. |

### output of the query :

| ReviewID | CustomerID | ProductID | ReviewDate | Rating | ReviewText |
|---|---|---|---|---|---|
| 1 | 77 | 18 | 2023-12-23 | 3 | Average experience, nothing special. |
| 2 | 80 | 19 | 2024-12-25 | 5 | The quality is top-notch. |
| 3 | 50 | 13 | 2025-01-26 | 4 | Five stars for the quick delivery. |
| 4 | 78 | 15 | 2025-04-21 | 3 | Good quality, but could be cheaper. |
| 5 | 64 | 2 | 2023-07-16 | 3 | Average experience, nothing special. |


  ## How to Use



1. **Set Up the Database**.
2. **Run the Queries**: Use the SQL queries in the `lib_managment_sys.sql` file to perform the analysis.
3. **Explore and Modify**: Customize the queries as needed to explore different aspects of the data or answer additional questions.

## Key Outcomes:

The resulting Power BI dashboard provides a centralized view of marketing data, facilitating:
* Clear understanding of marketing campaign performance.
* Insights into customer segmentation and behavior patterns.
* Identification of trends and opportunities for optimization.
* Support for strategic decision-making based on concrete data.

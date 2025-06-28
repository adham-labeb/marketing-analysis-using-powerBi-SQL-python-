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
### tables the query : 
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

### output of the query 
| CustomerID | CustomerName | Email | Gender | Age | Country | City |
|---|---|---|---|---|---|---|
| 1 | Emma Anderson | emma.anderson@example.com | Male | 50 | Germany | Berlin |
| 2 | Sarah Brown | sarah.brown@example.com | Female | 37 | Spain | Madrid |
| 3 | Robert Hernandez | robert.hernandez@example.com | Female | 26 | Netherlands | Amsterdam |
| 4 | David Garcia | david.garcia@example.com | Male | 25 | Sweden | Stockholm |
| 5 | Emma Miller | emma.miller@example.com | Female | 41 | Spain | Madrid |

  
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

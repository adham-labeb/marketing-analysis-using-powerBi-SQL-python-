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

# project steps :
# 1- Data cleaning :
## 1- Data cleaning using SQl :
### 1- The customer and geography table :
#### The query :
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
#### customer table :
| CustomerID | CustomerName | Email | Gender | Age | GeographyID |
|---|---|---|---|---|---|
| 1 | Emma Anderson | emma.anderson@example.com | Male | 50 | 2 |
| 2 | Sarah Brown | sarah.brown@example.com | Female | 37 | 4 |
| 3 | Robert Hernandez | robert.hernandez@example.com | Female | 26 | 6 |
| 4 | David Garcia | david.garcia@example.com | Male | 25 | 8 |
| 5 | Emma Miller | emma.miller@example.com | Female | 41 | 4 |

#### geography table : 
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
#### The query :
```sql
-- 2- cleaning the product table ---

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
#### The query : 
```sql
-- 3- cleaning customer_reviews table ---

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

### 4- the engagement_data table : 

#### The query :
```sql
-- 4- cleaning the engagement_data table ---

SELECT  
         EngagementID , 
		 ContentID , 
		 CampaignID , 
		 ProductID , 
		 UPPER(REPLACE(ContentType, 'Socialmedia', 'Social Media')) AS ContentType, 
         LEFT(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined) - 1) AS Views,
         RIGHT(ViewsClicksCombined, LEN(ViewsClicksCombined) - CHARINDEX('-', ViewsClicksCombined)) AS Clicks, 
		 Likes,
         FORMAT(CONVERT(DATE, EngagementDate), 'dd/MM/yyyy') AS EngagementDate  
FROM
         engagement_data  
```

### table before the query :
| EngagementID | ContentID | ContentType | Likes | EngagementDate | CampaignID | ProductID | ViewsClicksCombined |
|---|---|---|---|---|---|---|---|
| 1 | 39 | Blog | 190 | 2023-08-30 | 1 | 9 | 1883-671 |
| 2 | 48 | Blog | 114 | 2023-03-28 | 18 | 20 | 5280-532 |
| 3 | 16 | video | 32 | 2023-12-08 | 7 | 14 | 1905-204 |
| 4 | 43 | Video | 17 | 2025-01-21 | 19 | 20 | 2766-257 |
| 5 | 16 | newsletter | 306 | 2024-02-21 | 6 | 15 | 5116-1524 |
### output of the query :
| EngagementID | ContentID | CampaignID | ProductID | ContentType | Views | Clicks | Likes | EngagementDate |
|---|---|---|---|---|---|---|---|---|
| 1 | 39 | 1 | 9 | BLOG | 1883 | 671 | 190 | 30/08/2023 |
| 2 | 48 | 18 | 20 | BLOG | 5280 | 532 | 114 | 28/03/2023 |
| 3 | 16 | 7 | 14 | VIDEO | 1905 | 204 | 32 | 08/12/2023 |
| 4 | 43 | 19 | 20 | VIDEO | 2766 | 257 | 17 | 21/01/2025 |
| 5 | 16 | 6 | 15 | NEWSLETTER | 5116 | 1524 | 306 | 21/02/2024 |

### 5- customer_journey table :
### The query : 
```sql
-- 5- cleaning the customer_journey table ---
WITH DuplicateRecords AS (
    SELECT 
        JourneyID,
        CustomerID,
        ProductID,  
        format(convert(Date, VisitDate), 'dd/MM/yyyy') as VisitDate,  
        UPPER(Stage) as Stage,  
        Action,  
        round(COALESCE(Duration, AVG(Duration) OVER (PARTITION BY VisitDate)), 2) AS Duration,  
        ROW_NUMBER() OVER (
            PARTITION BY CustomerID, ProductID, VisitDate, UPPER(Stage), Action  
            ORDER BY JourneyID  
        ) AS row_num
    FROM 
        dbo.customer_journey
)
    
SELECT 
        JourneyID,
        CustomerID,
        ProductID,
        VisitDate,  
        Stage,  
        Action,  
        Duration
FROM DuplicateRecords
WHERE row_num = 1  
ORDER BY JourneyID
```
### table before the query :
| JourneyID | CustomerID | ProductID | VisitDate | Stage | Action | Duration |
|---|---|---|---|---|---|---|
| 1 | 64 | 18 | 2024-06-10 | Checkout | Drop-off | NULL |
| 2 | 94 | 11 | 2025-07-09 | Checkout | Drop-off | NULL |
| 3 | 34 | 8 | 2024-06-14 | ProductPage | View | 235 |
| 4 | 33 | 18 | 2025-05-28 | Checkout | Drop-off | NULL |
| 5 | 91 | 10 | 2023-02-11 | Homepage | Click | 156 |
### output of the query :

| JourneyID | CustomerID | ProductID | VisitDate | Stage | Action | Duration |
|---|---|---|---|---|---|---|
| 1 | 64 | 18 | 10/06/2024 | CHECKOUT | Drop-off | 132.33 |
| 2 | 94 | 11 | 09/07/2025 | CHECKOUT | Drop-off | 169.25 |
| 3 | 34 | 8 | 14/06/2024 | PRODUCTPAGE | View | 235 |
| 4 | 33 | 18 | 28/05/2025 | CHECKOUT | Drop-off | 12 |
| 5 | 91 | 10 | 11/02/2023 | HOMEPAGE | Click | 156 |

  ## 2- Data cleaning using python :
  ### 1- correcting gender :
  After cleaning the data using SQL, I observed discrepancies in customer names and their corresponding genders (e.g., 'Emma Anderson' listed as 'Male', or 'Robert Hernandez' as 'Female'). To address these inconsistencies, I utilized Python, specifically employing the `gender_guesser library`, to correct the gender entries and modify the customer + geography merged table."
  #### the python script :
  ```python
#-- importing the pandas and gender_guesser libraries --
import pandas as pd
import gender_guesser.detector as gender


# Read the CSV file into a pandas DataFrame.
df = pd.read_csv(r'C:\Users\Home\Desktop\NTI-final-project\dim_customers.csv')

# Initialize the gender detector from the gender_guesser library.
d = gender.Detector()

# Define a function to correct gender based on a customer's name.
# This function will be applied row-wise to the DataFrame.
def correct_gender(row: pd.DataFrame):

# Extract the first word of the 'CustomerName' as the primary name for gender detection.

    name = row['CustomerName'].split(' ')[0]
    
# Get the current gender value from the DataFrame row

    current_gender = row['Gender']
    
# Use the gender detector to guess the gender based on the extracted name.

    guessed_gender = d.get_gender(name)
```
### Table before the script : 
| CustomerID | CustomerName | Email | Gender | Age | Country | City |
|---|---|---|---|---|---|---|
| 1 | Emma Anderson | emma.anderson@example.com | Male | 50 | Germany | Berlin |
| 2 | Sarah Brown | sarah.brown@example.com | Female | 37 | Spain | Madrid |
| 3 | Robert Hernandez | robert.hernandez@example.com | Female | 26 | Netherlands | Amsterdam |
| 4 | David Garcia | david.garcia@example.com | Male | 25 | Sweden | Stockholm |
| 5 | Emma Miller | emma.miller@example.com | Female | 41 | Spain | Madrid |

### Table after the script :
| CustomerID | CustomerName | Email | Gender | Age | Country | City |
|---|---|---|---|---|---|---|
| 1 | Emma Anderson | emma.anderson@example.com | Female | 50 | Germany | Berlin |
| 2 | Sarah Brown | sarah.brown@example.com | Female | 37 | Spain | Madrid |
| 3 | Robert Hernandez | robert.hernandez@example.com | Male | 26 | Netherlands | Amsterdam |
| 4 | David Garcia | david.garcia@example.com | Male | 25 | Sweden | Stockholm |
| 5 | Emma Miller | emma.miller@example.com | Female | 41 | Spain | Madrid |

### 2- Sentiment analysis :
The customer review table includes a 'ReviewText' column with string data and a 'Rating' column with integer data. To derive insights from these two fields, I chose to conduct a sentiment analysis, implemented as follows :
### The python script : 
```python
# pip install pandas nltk 
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis if not already present.
nltk.download('vader_lexicon')

# Get data from the csv file
pd.DataFrame = pd.read_csv(r"C:\Users\Home\Desktop\NTI-final-project\fact_customer_reviews.csv")
customer_reviews_df = pd.DataFrame 

# Initialize the VADER sentiment intensity analyzer for analyzing the sentiment of text data
sia = SentimentIntensityAnalyzer()

# Define a function to calculate sentiment scores using VADER
def calculate_sentiment(review):
    # Get the sentiment scores for the review text
    sentiment = sia.polarity_scores(review)
    # Return the compound score, which is a normalized score between -1 (most negative) and 1 (most positive)
    return sentiment['compound']

# Define a function to categorize sentiment using both the sentiment score and the review rating
def categorize_sentiment(score, rating):
    # Use both the text sentiment score and the numerical rating to determine sentiment category
    if score > 0.05:  # Positive sentiment score
        if rating >= 4:
            return 'Positive'  # High rating and positive sentiment
        elif rating == 3:
            return 'Mixed Positive'  # Neutral rating but positive sentiment
        else:
            return 'Mixed Negative'  # Low rating but positive sentiment
    elif score < -0.05:  # Negative sentiment score
        if rating <= 2:
            return 'Negative'  # Low rating and negative sentiment
        elif rating == 3:
            return 'Mixed Negative'  # Neutral rating but negative sentiment
        else:
            return 'Mixed Positive'  # High rating but negative sentiment
    else:  # Neutral sentiment score
        if rating >= 4:
            return 'Positive'  # High rating with neutral sentiment
        elif rating <= 2:
            return 'Negative'  # Low rating with neutral sentiment
        else:
            return 'Neutral'  # Neutral rating and neutral sentiment

# Define a function to bucket sentiment scores into text ranges
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'  # Strongly positive sentiment
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'  # Mildly positive sentiment
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'  # Mildly negative sentiment
    else:
        return '-1.0 to -0.5'  # Strongly negative sentiment

# Apply sentiment analysis to calculate sentiment scores for each review
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)

# Apply sentiment categorization using both text and rating
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)

# Apply sentiment bucketing to categorize scores into defined ranges
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# Display the first few rows of the DataFrame with sentiment scores, categories, and buckets
print(customer_reviews_df.head())

# Save the DataFrame with sentiment scores, categories, and buckets to a new CSV file
customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)
```
### Table before the script :
| ReviewID | CustomerID | ProductID | ReviewDate | Rating | ReviewText |
|---|---|---|---|---|---|
| 1 | 77 | 18 | 2023-12-23 | 3 | Average experience, nothing special. |
| 2 | 80 | 19 | 2024-12-25 | 5 | The quality is top-notch. |
| 3 | 50 | 13 | 2025-01-26 | 4 | Five stars for the quick delivery. |
| 4 | 78 | 15 | 2025-04-21 | 3 | Good quality, but could be cheaper. |
| 5 | 64 | 2 | 2023-07-16 | 3 | Average experience, nothing special. |
### Output of the script : 
| ReviewID | CustomerID | ProductID | ReviewDate | Rating | ReviewText | SentimentScore | SentimentCategory | SentimentBucket |
|---|---|---|---|---|---|---|---|---|
| 1 | 77 | 18 | 12/23/2023 | 3 | Average experience, nothing special. | -0.3089 | Mixed Negative | -0.49 to 0.0 |
| 2 | 80 | 19 | 12/25/2024 | 5 | The quality is top-notch. | 0 | Positive | 0.0 to 0.49 |
| 3 | 50 | 13 | 1/26/2025 | 4 | Five stars for the quick delivery. | 0 | Positive | 0.0 to 0.49 |
| 4 | 78 | 15 | 4/21/2025 | 3 | Good quality, but could be cheaper. | 0.2382 | Mixed Positive | 0.0 to 0.49 |
| 5 | 64 | 2 | 7/16/2023 | 3 | Average experience, nothing special. | -0.3089 | Mixed Negative | -0.49 to 0.0 |

# 2-Data Modeling and Analysis:
### 1- The cleaned and transformed data is loaded into Power BI.
### 2- Relationships between various data tables are established to create a robust data model, enabling cross-table analysis.


![Data Model Diagram](https://github.com/adham-labeb/marketing-analysis-using-powerBi-SQL-python-/blob/main/data_model.png)

### 3- Measures and calculated columns are defined to derive key marketing metrics and KPIs (Key Performance Indicators).
#### list of different measures : 
1- **AVG_Rating** : 
``` dax
AVG_Rating = AVERAGE(fact_customer_reviews[Rating])
``` 
2- **Clicks** :
```dax
clicks = sum(fact_engagement_data[Clicks])
```
3- Conversion rate :
```dax
Conversion Rate = 
VAR TotalVisitors = CALCULATE( COUNT (fact_customer_journey[JourneyID]) , fact_customer_journey[Action] = "View" )
VAR TotalPurchases = CALCULATE(
    COUNT(fact_customer_journey[JourneyID]),
    fact_customer_journey[Action] = "Purchase"
)
RETURN
IF(
    TotalVisitors = 0, 
    0, 
    DIVIDE(TotalPurchases, TotalVisitors))
```
4- Likes :
```dax
Likes = sum (fact_engagement_data[Likes])
```
5- Number of campaigns:
```dax
Number of Campaigns = DISTINCTCOUNT(fact_engagement_data[CampaignID])
```
6- Number of engagements :
```dax
Number of Engagements = DISTINCTCOUNT(fact_engagement_data[EngagementID])
```
7- Number of journeys :
```dax
Number of journeys = DISTINCTCOUNT(fact_customer_journey[JourneyID])
```
8- Number of reviews : 
```dax
number of reviews = DISTINCTCOUNT(fact_customer_reviews[ReviewID])
```
9- views :
```dax
Views = SUM ( fact_engagement_data[Views] )
```
# 3- Interactive Dashboard Development (Power BI):
## 1- Overview Dashboard :
![overview dashboard](https://github.com/adham-labeb/marketing-analysis-using-powerBi-SQL-python-/blob/main/overview_dashboard.png)
## 2- Conversion Details﻿ dashboard :
![Conversion Details﻿](https://github.com/adham-labeb/marketing-analysis-using-powerBi-SQL-python-/blob/main/conversion_details_dashboard.png)
## 3- Social Media Details dashboard  :
![Social Media Details](https://github.com/adham-labeb/marketing-analysis-using-powerBi-SQL-python-/blob/main/social_media_details_dashboard.png)
## 4- Customers Reviews Details dashboard :
![Customers Reviews Details](https://github.com/adham-labeb/marketing-analysis-using-powerBi-SQL-python-/blob/main/customers_review_details_dashboard.png)

  ## How to Use

1. **Set Up the Database**.
2. **Run the Queries**: Use the SQL queries in the `SQL_Data_Cleaning_queries.sql` file to clean the data .
3. **Run the python script : use the python script in the `corecting_gender_script.py` to correct the gender
4. **Run the python script : use the python script in the `customer_review_saintiment_analysis.py` to use the sentiment analysis
5. **Note :** make sure to change the csv file path in the both python file to the correct path on your pc
6. Save the output of the SQL cleaning queries and the output of the python script into CSVs files
7. Upload the cleaned CSVs to the power BI

## Key Outcomes:

The resulting Power BI dashboard provides a centralized view of marketing data, facilitating:
* Clear understanding of marketing campaign performance.
* Insights into customer segmentation and behavior patterns.
* Identification of trends and opportunities for optimization.
* Support for strategic decision-making based on concrete data.

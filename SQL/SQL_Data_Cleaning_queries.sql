--- cleaning tables ---
-- 1- cleaning the customer table and merge it with the geography table ---
SELECT * from customers
SELECT * from geography

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

---------------------------------------------------------------------------------------------------------------------------------------------------------
-- 2- cleaning the product table ---
SELECT  * FROM products

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
---------------------------------------------------------------------------------------------------------------------------------------------------------
-- 3- cleaning customer_reviews table ---
SELECT * FROM customer_reviews


SELECT 
           ReviewID , 
		   CustomerID,
		   ProductID , 
		   ReviewDate ,
		   Rating , 
		   Replace (ReviewText,'  ',' ') AS ReviewText
FROM       
           customer_reviews

---------------------------------------------------------------------------------------------------------------------------------------------------------
-- 4- cleaning the engagement_data table ---
SELECT top 5* FROM engagement_data


SELECT  top 5
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


---------------------------------------------------------------------------------------------------------------------------------------------------------
-- 5- cleaning the customer_journey table
select * from customer_journey
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
---------------------------------------------------------------------------------------------------------------------------------------------------------


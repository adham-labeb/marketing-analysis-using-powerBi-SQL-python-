SELECT * FROM products

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
        
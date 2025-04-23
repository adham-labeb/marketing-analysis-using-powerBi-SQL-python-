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
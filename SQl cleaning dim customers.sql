SELECT * from customers
SELECT * from geography


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
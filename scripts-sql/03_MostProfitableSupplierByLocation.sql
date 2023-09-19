SELECT  
	CASE                                        
		WHEN Country IN ( 'USA', 'Brazil', 'Canada' ) 
			THEN 'America'
                                                
		WHEN Country IN ( 'UK', 'Spain', 'Sweden', 'Germany', 'Italy', 'Norway', 
						  'France', 'Denmark', 'Netherlands', 'Finland' ) 
			THEN 'Europe'
                                                
		WHEN Country IN ( 'Japan', 'Australia', 'Singapore' ) 
			THEN 'Asia / Oceania'                                                                                              
	END 
		AS Location,                                     
	SupplierName, s.City, s.Country,
	ROUND( SUM( Price * Quantity ), 2 ) 
		AS Revenues
                                        
FROM [OrderDetails] od
JOIN [Products] p 
	ON od.ProductID = p.ProductID
JOIN [Suppliers] s 
	ON p.SupplierID = s.SupplierID 
                                
GROUP BY Location, s.SupplierID
ORDER BY Location, Revenues DESC
SELECT  p.ProductName, p.Unit, p.Price, 
		SUM( od.Quantity ) 
			AS TotalSoldProducts,
		ROUND( SUM( od.Quantity ) * p.Price, 2 ) 
			AS TotalRevenues
                                            
FROM [Products] p
JOIN [OrderDetails] od ON p.ProductID = od.ProductID
                                            
GROUP BY ProductName
ORDER BY TotalSoldProducts DESC 
LIMIT 10
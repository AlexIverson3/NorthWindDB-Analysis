SELECT 	c.CustomerName, c.Country,
		ROUND( ( od.Quantity * p.Price / 1.00 ), 2 ) 
			AS AvgPriceTicket

FROM 	[Customers] c
JOIN 	[Orders] o 
	ON o.CustomerID = c.CustomerID
JOIN 	[OrderDetails] od 
	ON od.OrderID = o.OrderID
JOIN 	[Products] p 
	ON p.ProductID = od.ProductID

GROUP BY c.CustomerName
ORDER BY AvgPriceTicket DESC
                                        
LIMIT 15
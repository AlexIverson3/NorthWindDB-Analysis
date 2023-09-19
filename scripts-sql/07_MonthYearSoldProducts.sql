SELECT	STRFTIME( "%Y", o.OrderDate ) AS Year,
		STRFTIME( "%Y-%m", o.OrderDate ) AS Month,
		p.ProductName, 
		SUM(od.Quantity) AS ProductSales
                                      		
FROM [Products] p
JOIN [Orders] o ON od.OrderID = O.OrderID
JOIN [OrderDetails] od ON p.ProductID = od.ProductID
                                    
GROUP BY Month, p.ProductName
ORDER BY OrderDate
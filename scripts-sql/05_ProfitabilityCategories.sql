SELECT  c.CategoryName,
		p.ProductName,
		Price, Cost,
		SUM( od.Quantity ) AS Sales,
		ROUND( SUM( od.Quantity )* Price ) AS Revenues,
		ROUND( ( Price - Cost ) / Price * 100, 2 ) AS Profitability
                                            
FROM [OrderDetails] od
JOIN [Products] p 
	ON od.ProductID = p.ProductID
JOIN [Categories] c 
	ON p.CategoryID = c.CategoryID 
                                            
GROUP BY c.CategoryName, Profitability
ORDER BY c.CategoryName, Profitability DESC
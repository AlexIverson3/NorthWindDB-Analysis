SELECT  p.ProductName,
		Price, Cost,
		SUM( od.Quantity ) AS Sales,
		ROUND( SUM( od.Quantity )* Price ) AS Revenues,
		ROUND( ( Price - Cost ) / Price * 100, 2 ) AS Profitability

FROM [OrderDetails] od
JOIN [Products] p 
	ON od.ProductID = p.ProductID

GROUP BY p.ProductName, Profitability
ORDER BY Profitability DESC
LIMIT 10
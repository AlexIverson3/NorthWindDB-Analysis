SELECT  SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName AS Employee,
		SUM( od.Quantity ) AS Sales,
		ROUND( SUM( od.Quantity )* p.Price ) 
			AS Revenues,
		ROUND( ROUND( SUM( od.Quantity )* p.Price ) / SUM( od.Quantity ) ) 
			AS AvgRevSale

FROM    [Employees] e
JOIN    [Orders] o 
	ON o.EmployeeID = e.EmployeeID
JOIN    [OrderDetails] od 
	ON od.OrderID = o.OrderID
JOIN    [Products] p
	ON od.ProductID = p.ProductID

GROUP BY e.EmployeeID
ORDER BY Sales DESC
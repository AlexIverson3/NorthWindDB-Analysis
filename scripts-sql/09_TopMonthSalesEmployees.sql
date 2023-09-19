SELECT	STRFTIME( '%Y-%m', o.OrderDate ) AS Month,
		SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName 
			AS Employee,
		COUNT(o.OrderID) AS TotalSales                                                 
                                        
FROM [Employees] e
JOIN [Orders] o 
	ON e.EmployeeID = o.EmployeeID
JOIN [OrderDetails] od 
	ON od.OrderID = O.OrderID
                                        
GROUP BY Month, Employee
ORDER BY TotalSales DESC, Month
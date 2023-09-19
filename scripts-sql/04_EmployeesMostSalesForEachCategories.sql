SELECT  SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName AS Employee,
		c.CategoryName,
		SUM(od.Quantity) AS SalesEmployee
                                          
FROM [Employees] e
JOIN [Orders] o 
	ON o.EmployeeID = e.EmployeeID
JOIN [OrderDetails] od 
	ON od.OrderID = o.OrderID
JOIN [Products] p 
	ON p.ProductID = od.ProductID
JOIN [Categories] c	
	ON c.CategoryID = p.CategoryID
                                        
GROUP BY c.CategoryName, Employee
ORDER BY SalesEmployee DESC
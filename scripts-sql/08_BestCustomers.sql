SELECT  c.ContactName, 
		COUNT( o.OrderID ) AS CustomerOrders,
		ROUND( SUM( od.Quantity ) * p.Price ) 
			AS PurchaseExpenditure,
		ROUND( SUM( od.Quantity ) * p.Price / COUNT( o.OrderID ) ) 
			AS AvgPurchase
                                        
FROM [Customers] c
JOIN [Orders] o 
	ON c.CustomerID = o.CustomerID
JOIN [OrderDetails] od 
	ON o.OrderID = od.OrderID
JOIN [Products] p
	ON od.ProductID = p.ProductID
                                        
GROUP BY c.ContactName
ORDER BY CustomerOrders DESC, AvgPurchase DESC
LIMIT 10
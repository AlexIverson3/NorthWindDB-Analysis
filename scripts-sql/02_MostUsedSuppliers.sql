SELECT  s.SupplierName, s.City, s.Country, 
		COUNT(s.SupplierID) 
			AS SuppliedProducts
                                        
FROM [Suppliers] s
JOIN [Products] p 
	ON s.SupplierID = p.SupplierID
                                
GROUP BY s.SupplierID
ORDER BY SuppliedProducts ASC
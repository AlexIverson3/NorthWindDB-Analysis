import matplotlib.pyplot as plt
from tabulate import tabulate
from northwind import conn_db


# [ BEST CUSTOMERS ]
#=============================================================================================================================
bestCustomers = conn_db( query = '''
                                        SELECT  c.ContactName, 
                                                COUNT( o.OrderID ) AS CustomerOrders,
                                                ROUND( SUM( od.Quantity ) * p.Price ) AS PurchaseExpenditure,
                                                ROUND( SUM( od.Quantity ) * p.Price / COUNT( o.OrderID ) ) AS AvgPurchase
                                        
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
                                 ''',
                                 
                         columns = [ 'CUSTOMERS', 'TOTAL ORDERS', 'PURCHASE', 'AVG PURCHASE' ] )

print("\n==[ BEST CUSTOMERS ]==")
print( tabulate( bestCustomers, headers = "keys", tablefmt= "pretty" ) )
print()


# GRÁFICA MATPLOTLIB
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
bestCustomers.plot( x = "ProductName", y = [ 'TOTAL ORDERS', 'PURCHASE', 'AVG. PURCHASE' ],
                    kind = "bar", figsize = ( 10, 5 ), legend = False )
plt.title( "BEST COSTUMERS" )
plt.xlabel( "PRODUCTS" )
plt.ylabel( "SALES" )
plt.xticks( rotation = 45 )
plt.show()
#=============================================================================================================================

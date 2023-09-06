import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db


# [ MONTHLY AND YEARLY PRODUCT SALES ]
#=============================================================================================================================
prodSalesMmYy = conn_db( query = '''
                                    SELECT	STRFTIME( "%Y", o.OrderDate ) AS Year,
											STRFTIME( "%Y-%m", o.OrderDate ) AS Month,
		                                    p.ProductName, 
                                      		SUM(od.Quantity) AS ProductSales
                                      		
                                    FROM [Products] p
                                    JOIN [Orders] o ON od.OrderID = O.OrderID
                                    JOIN [OrderDetails] od ON p.ProductID = od.ProductID
                                    
                                    GROUP BY Month, p.ProductName
                                    ORDER BY OrderDate
                                 ''',
                                 
                         columns = [ 'YEAR', 'MONTH', 'PRODUCT', 'TOTAL SALES' ] )

print("\n==[ MONTH SALES & YEAR SALES BY PRODUCTS ]==")
print( tabulate( prodSalesMmYy, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB (pivot_table)
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
p_table_m = prodSalesMmYy.pivot_table( index = "MONTH", columns = "PRODUCT", values = "TOTAL SALES", 
                          			   aggfunc = "sum", fill_value = None )
p_table_m.plot( kind = "bar", figsize = ( 10, 5 ) )

plt.title( "TOP MONTH SALES PRODUCTS" )
plt.xlabel( "MONTH OF THE YEAR" )
plt.ylabel( "TOTAL SALES" )
plt.xticks( rotation = 0 )
plt.legend( title = "PRODUCTS", loc = "upper left", bbox_to_anchor = ( 1, 1.05 ), 
            fontsize = 9, ncol = 2  )
plt.show()
#=============================================================================================================================
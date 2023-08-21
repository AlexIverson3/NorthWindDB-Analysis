import matplotlib.pyplot as plt
from tabulate import tabulate
from northwind import conn_db


# MOST SOLD PRODUCTS [ TOP 10 ]
#=============================================================================================================================
topSoldProduct = conn_db( query = ''' 
                                      SELECT  p.ProductName, p.Unit, p.Price, 
		                                      SUM( od.Quantity ) AS TotalSoldProducts,
		                                      ROUND( SUM( od.Quantity ) * p.Price, 2 ) AS TotalRevenues
                                        
                                      FROM [Products] p
                                      JOIN [OrderDetails] od ON p.ProductID = od.ProductID
                                      
                                      GROUP BY ProductName
                                      ORDER BY TotalSoldProducts DESC 
                                      LIMIT 10 
                                  ''',
                                  
                          columns = [ 'PRODUCT', 'UNIT CONTENT', 'PRICE', 'TOTAL SALES', 'TOTAL REVENUES' ] ) 

print("\n==[ MOST SOLD PRODUCTS (TOP 10) ]==")
print( tabulate( topSoldProduct, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.style.use( "bmh" )
fig, ( ax1, ax2 ) = plt.subplots( nrows = 2, ncols = 1, sharex = True )

plt.suptitle( "TOP 10 MOST SOLD PRODUCTS & PROFITABLE", fontsize = 40, color = "darkblue" )
topSoldProduct.plot( ax = ax1, kind = "bar", figsize = ( 10, 1 ), legend = True,
                     y = "TOTAL SALES", color = "skyblue" )
plt.xlabel( "PRODUCTS", fontsize = 14 )
plt.ylabel( "TOTAL SALES", fontsize = 14 )
plt.xticks()

topSoldProduct.plot( ax = ax2, kind = "bar", figsize = ( 10, 5 ), legend = True,
                     x = "PRODUCT", y = "TOTAL REVENUES" )
plt.xlabel( "PRODUCTS", fontsize = 14, color = "blue" )
plt.ylabel( "TOTAL REVENUES", fontsize = 14, color = "blue" )
plt.xticks( rotation = 45 )

plt.show()
#=============================================================================================================================

"""
topSoldProduct.plot( x = "ProductName", y = "TotalSoldProducts",
                     kind = "bar", figsize = ( 10, 5 ), legend = False )
plt.title( "TOP10 MOST SOLD PRODUCTS" )
plt.xlabel( "PRODUCTS" )
plt.ylabel( "SALES" )
plt.xticks( rotation = 90 )
plt.show()
"""
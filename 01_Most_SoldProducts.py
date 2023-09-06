import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db


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
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
products    = topSoldProduct[ "PRODUCT" ]
sales       = topSoldProduct[ "TOTAL SALES" ]
revenues    = topSoldProduct[ "TOTAL REVENUES" ]

plt.style.use( "bmh" )

fig, ax = plt.subplots( nrows = 2, ncols = 1, 
                        figsize = ( 15, 7 ) ) 
fig.align_labels()                                                 

plt.suptitle( "TOP 10 - MOST SOLD PRODUCTS", 
              fontsize = 40, color = "darkblue", fontweight = "bold" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 211 )
plt.title( "[ MOST SALES BY PRODUCT ]", color = "firebrick", 
           fontweight = "bold" )

bar_container1 = plt.bar( products, sales )
plt.bar( x = products, height = sales, 
         color = "cornflowerblue" )
plt.bar_label( bar_container1, fmt = "{:,.0f} uds.", label_type = "center",
               fontweight = "bold", color = "snow" )

plt.xlabel( "PRODUCTS", labelpad = 12, fontsize = 8, color = "snow",
            fontweight = "bold", bbox={ 'facecolor': 'firebrick', 
                                        'alpha': 0.5, 'pad': 5 } )
plt.ylabel( "TOTAL SALES", labelpad = 20, fontsize = 8, color = "white",
            fontweight = "bold", bbox={ 'facecolor': 'red',
                                        'alpha': 0.5, 'pad': 5 } )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 212 )
plt.title( "[ MOST REVENUES BY PRODUCT ]", color = "firebrick", 
           fontweight = "bold" )

bar_container2 = plt.bar( products, revenues )
plt.bar( x = products, height = revenues, 
         color = "orange" )
plt.bar_label( bar_container2, fmt = "${:,.0f}", label_type = "center",
               fontweight = "bold", color = "firebrick" )

plt.xlabel( "PRODUCTS", labelpad = 12, fontsize = 8, color = "snow",
            fontweight = "bold", bbox={ 'facecolor': 'firebrick', 
                                        'alpha': 0.5, 'pad': 5 } )
plt.ylabel( "TOTAL REVENUES", labelpad = 20, fontsize = 8, color = "white", 
            fontweight = "bold", bbox={ 'facecolor': 'red', 
                                        'alpha': 0.5, 'pad': 5 } )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
"""
topSoldProduct.plot( ax = ax1, kind = "bar", figsize = ( 10, 1 ), legend = True,        # MÉTODO PLOT DE PANDAS
                     y = "TOTAL SALES", color = "skyblue" )

topSoldProduct.plot( ax = ax2, kind = "bar", figsize = ( 10, 5 ), legend = True,        # MÉTODO PLOT DE PANDAS
                     x = "PRODUCT", y = "TOTAL REVENUES" )

plt.xlabel( "PRODUCTS", fontsize = 14, color = "blue" )                                 # MÉTODO PLT DE MATPLOTLIB
plt.ylabel( "TOTAL REVENUES", fontsize = 14, color = "blue" )
plt.xticks( rotation = 45 )
"""
plt.tight_layout()
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
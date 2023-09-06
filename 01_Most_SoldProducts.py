import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db


# MOST SOLD PRODUCTS [ TOP 10 ]
#=============================================================================================================================
topSoldProduct = conn_db(   query = ''' 
                                        SELECT  p.ProductName, p.Unit, p.Price, 
                                                SUM( od.Quantity ) 
                                                    AS TotalSoldProducts,
                                                ROUND( SUM( od.Quantity ) * p.Price, 2 ) 
                                                    AS TotalRevenues
                                            
                                        FROM [Products] p
                                        JOIN [OrderDetails] od ON p.ProductID = od.ProductID
                                            
                                        GROUP BY ProductName
                                        ORDER BY TotalSoldProducts DESC 
                                        LIMIT 10 
                                    ''',
                                  
                            columns = [ 'PRODUCT', 'UNIT CONTENT', 'PRICE', 'TOTAL SALES', 'TOTAL REVENUES' ]   ) 

print("\n==[ MOST SOLD PRODUCTS (TOP 10) ]==")
print( tabulate( topSoldProduct, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
products    = topSoldProduct[ "PRODUCT" ].apply( lambda x: x.replace(" ", "\n") )
sales       = topSoldProduct[ "TOTAL SALES" ]
revenues    = topSoldProduct[ "TOTAL REVENUES" ]
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.style.use( "bmh" )

fig, ax = plt.subplots( nrows = 2, ncols = 1, 
                        figsize = ( 16, 8 ) )
fig.align_labels()                                                 

plt.suptitle( "TOP 10 - MOST SOLD PRODUCTS", 
              fontsize = 35, color = "firebrick", fontweight = "bold" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# PLOT 1
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 211 )
plt.title( "[ MOST SALES BY PRODUCT ]", 
           color = "snow", fontweight = "bold", fontsize = 9, 
           loc = "right", bbox={ 'facecolor':'indianred', 
                                 'boxstyle': 'round, pad=0.30' } )

bar_sales = plt.bar( x = products, height = sales, 
                          edgecolor = "mediumblue", 
                          color = "cornflowerblue" )

plt.bar_label( bar_sales, fmt = "{:,.0f} uds.", label_type = "center",
               fontweight = "bold", color = "snow" )

plt.xlabel( "PRODUCTS", 
            labelpad = 0, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( "TOTAL SALES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "royalblue", labelsize = 9, 
                 grid_color = "skyblue", grid_alpha = 0.8 )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# PLOT 2
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 212 )
plt.title( "[ TOTAL REVENUES OF THE TOP 10 MOST SALES PRODUCTS ]", 
           color = "snow", fontweight = "bold", fontsize = 9,
           loc = "right", bbox={ 'facecolor':'indianred', 
                                 'boxstyle': 'round, pad=0.30' } )

bar_revenues = plt.bar( x = products, height = revenues, 
                          edgecolor = "darkred", 
                          color = "orange" )

plt.bar_label( bar_revenues, fmt = "${:,.0f}", label_type = "center",
               fontweight = "bold", color = "firebrick" )

plt.xlabel( "PRODUCTS", 
            labelpad = 0, fontsize = 8.25, color = "firebrick",
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( "TOTAL REVENUES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "firebrick", labelsize = 9, 
                 grid_color = "wheat", grid_alpha = 0.8 )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================
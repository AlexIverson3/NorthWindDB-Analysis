import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db



# [ EMPLOYEES - MOST SALES FOR EACH CATEGORIES ]
#=============================================================================================================================
mostProfitableProd = conn_db( query = '''
                                        SELECT  p.ProductName,
                                        		Price, Cost,
                                        		SUM( od.Quantity ) AS Sales,
                                        		ROUND( SUM( od.Quantity )* Price ) AS Revenues,
                                        		ROUND( ( Price - Cost ) / Price * 100, 2 ) AS Profitability

                                        FROM [OrderDetails] od
                                        JOIN [Products] p 
                                            ON od.ProductID = p.ProductID

                                        GROUP BY p.ProductName, Profitability
                                        ORDER BY Profitability DESC
                                        LIMIT 10
                                      ''',
                                  
                              columns = [ 'PRODUCT', 'PRICE', 'COST', 'SALES', 'REVENUES', 'PROFITABILITY' ] )

print("\n==[ MOST PROFITABLE PRODUCTS ]==")
print( tabulate( mostProfitableProd, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
products    = mostProfitableProd[ "PRODUCT" ].apply( lambda x: x.replace(" ", "\n") )
sales       = mostProfitableProd[ "SALES" ]
profitab    = mostProfitableProd[ "PROFITABILITY" ]
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.style.use( "bmh" )

fig, ( ax1, ax2 ) = plt.subplots( nrows = 2, ncols = 1, 
                                  figsize = ( 16, 8 ) )

fig.align_labels()

plt.suptitle( "TOP 10 - MOST PROFITABLE PRODUCTS", 
              fontsize = 35, color = "firebrick", fontweight = "bold" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# PLOT 1
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 211 )
plt.title( "[ MOST PROFITABLE PRODUCTS ]", 
           color = "snow", fontweight = "bold", fontsize = 9, 
           loc = "right", bbox={ 'facecolor':'indianred', 
                                 'boxstyle': 'round, pad=0.30' } )

bar_profitab = plt.bar( x = products, height = profitab, 
                        edgecolor = "darkred", 
                        color = "orange" )

plt.bar_label( bar_profitab, fmt = "{:,.0f} %", label_type = "center",
               fontsize = 14, fontweight = "bold", color = "firebrick" )

plt.xlabel( "PRODUCTS", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( " PROFITABILITY (%)", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "firebrick", labelsize = 9, rotation = 0, 
                 grid_color = "lightsalmon", grid_alpha = 0.8 )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# PLOT 2
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 212 )
plt.title( "[ TOTAL SALES OF THE PRODUCTS ]", 
           color = "snow", fontweight = "bold", fontsize = 9, 
           loc = "right", bbox={ 'facecolor':'indianred', 
                                 'boxstyle': 'round, pad=0.30' } )

bar_sales = plt.bar( x = products, height = sales, 
                     edgecolor = "mediumblue", 
                     color = "cornflowerblue" )

plt.bar_label( bar_sales, fmt = "{:,.0f} uds.", label_type = "center",
               fontweight = "bold", color = "snow" )

plt.xlabel( "PRODUCTS", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 }  )
plt.ylabel( " TOTAL SALES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "royalblue", labelsize = 9, rotation = 0, 
                 grid_color = "lightsalmon", grid_alpha = 0.8 )

plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================
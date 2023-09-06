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
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
plt.style.use( "bmh" )

p_table_m = prodSalesMmYy.pivot_table( index = "MONTH", columns = "PRODUCT", values = "TOTAL SALES", 
                          			   aggfunc = "sum", fill_value = None )
p_table_m.plot( kind = "bar", figsize = ( 16, 10 ), edgecolor = "dimgray", width = 0.85 )

plt.title( "TOP MONTH SALES PRODUCTS", 
           fontsize = 35, color = "firebrick", fontweight = "bold", pad = 30 )

plt.xlabel( "MONTH OF THE YEAR", 
            labelpad = 15, fontsize = 8.25, color = "firebrick",
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
                 rotation = 0, colors = "firebrick", labelsize = 10,
                 grid_color = "lightsalmon", grid_alpha = 0.8  )

plt.legend( title = "PRODUCTS", loc = "upper left", bbox_to_anchor = ( 1, 1 ), 
            facecolor= "ivory", edgecolor = "firebrick", shadow = True, ncol = 2,
            fontsize = 6, labelspacing = 1.0, borderaxespad = 3.0,
            title_fontproperties = { 'weight': 'bold', 'size': 11, 
                                     'style': 'italic' } )

plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================
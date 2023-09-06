import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db



# [ EMPLOYEES - MOST SALES FOR EACH CATEGORIES ]
#=============================================================================================================================
lessProfitCat = conn_db( query = '''
                                    SELECT  c.CategoryName,
                                    		p.ProductName,
                                    		Price, Cost,
                                    		SUM( od.Quantity ) AS Sales,
                                    		ROUND( SUM( od.Quantity )* Price ) AS Revenues,
                                    		ROUND( ( Price - Cost ) / Price * 100, 2 ) AS Profitability
                                          
                                    FROM [OrderDetails] od
                                    JOIN [Products] p 
                                        ON od.ProductID = p.ProductID
                                    JOIN [Categories] c 
                                        ON p.CategoryID = c.CategoryID 
                                        
                                    GROUP BY c.CategoryName, Profitability
                                    ORDER BY c.CategoryName, Profitability DESC
                                  ''',
                                  
                          columns = [ 'CATEGORY', 'PRODUCT', 'PRICE', 'COST', 'SALES', 'REVENUES', 'PROFITABILITY' ] )

print("\n==[ MOST SALES OF THE EMPLOYEES FOR EACH CATEGORY ]==")
print( tabulate( lessProfitCat, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
plt.style.use( "bmh" )

p_table = lessProfitCat.pivot_table( index = "CATEGORY", columns = "PRODUCT", values = "PROFITABILITY", 
                                     aggfunc = "sum", fill_value = None )
p_table.plot( kind = "bar", figsize = ( 16, 10 ), edgecolor = "dimgray", width = 0.85 )

plt.title( "PROFITABILITY BY CATEGORY", 
           fontsize = 35, color = "firebrick", fontweight = "bold", pad = 30 )
plt.xlabel( "CATEGORY", 
            labelpad = 15, fontsize = 8.25, color = "firebrick",
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( "PROFITABILITY (%)", 
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
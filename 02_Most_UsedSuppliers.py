import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db


# [ TOP USED SUPPLIERS ] 
#=============================================================================================================================
topUsedSuppliers = conn_db( query = '''
                                        SELECT  s.SupplierName, s.City, s.Country, 
                                                COUNT(s.SupplierID) 
                                                    AS SuppliedProducts
                                        
                                        FROM [Suppliers] s
                                        JOIN [Products] p 
                                            ON s.SupplierID = p.SupplierID
                                
                                        GROUP BY s.SupplierID
                                        ORDER BY SuppliedProducts ASC
                                    ''',

                            columns = [ 'SUPPLIER', 'CITY', 'COUNTRY', 'PRODUCTS' ] )

print("\n==[ MOST USED SUPPLIERS ]==")
print( tabulate( topUsedSuppliers, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
supplier = topUsedSuppliers[ "SUPPLIER" ]
products = topUsedSuppliers[ "PRODUCTS" ]
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.style.use( "bmh" )


topUsedSuppliers.plot( x = "SUPPLIER", y = "PRODUCTS", kind = "barh",
                       figsize = ( 16, 8 ), legend = False )

plt.suptitle( "MOST USED SUPPLIERS", 
              fontsize = 35, color = "firebrick", fontweight = "bold" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
barh_container = plt.barh( y = supplier, width = products,
                           color = ["indianred", "orange"], 
                           edgecolor = "darkred" )

plt.bar_label( barh_container, fmt = " {:,.0f} products", label_type = "edge",
               fontweight = "semibold", fontsize = 7, color = "dimgray" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.xlabel( "TOTAL SUPPLIED PRODUCTS", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( "SUPPLIERS", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "firebrick", labelsize = 8, 
                 grid_color = "lightsalmon", grid_alpha = 0.8 )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.get_current_fig_manager()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================


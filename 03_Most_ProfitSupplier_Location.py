import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db


# [ MOST PROFITABLE SUPPLIER BY GEOGRAPHIC ZONE ] 
#=============================================================================================================================
mostProfitSupplier = conn_db(        
                        query = '''
                                SELECT  
                                        CASE
                                            WHEN Country IN ( 'USA', 'Brazil', 'Canada' ) 
                                                THEN 'America'
                                            WHEN Country IN ( 'UK', 'Spain', 'Sweden', 'Germany', 'Italy', 'Norway', 
                                                              'France', 'Denmark', 'Netherlands', 'Finland' ) 
                                                THEN 'Europe'
                                            WHEN Country IN ( 'Japan', 'Australia', 'Singapore' ) 
                                                THEN 'Asia / Oceania'
                                        END AS Location,
                                        
                                        SupplierName, s.City, s.Country,
                                        ROUND( SUM( Price * Quantity ), 2 ) 
                                            AS Revenues
                                        
                                FROM [OrderDetails] od
                                JOIN [Products] p 
                                        ON od.ProductID = p.ProductID
                                JOIN [Suppliers] s 
                                        ON p.SupplierID = s.SupplierID 
                                
                                GROUP BY Location, s.SupplierID
                                ORDER BY Location, Revenues DESC        
                                ''',
                                      
                        columns = [ 'LOCATION', 'SUPPLIER', 'CITY', 'COUNTRY', 'REVENUES' ]    )

print( tabulate( mostProfitSupplier, headers = "keys", tablefmt= "pretty" ) )



# GRÁFICA MATPLOTLIB (pivot_table)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
plt.style.use( "bmh" )

p_table = mostProfitSupplier.pivot_table( index = "LOCATION", columns = "SUPPLIER", values = "REVENUES", 
                                          aggfunc = "sum", fill_value = None )
p_table.plot( kind = "bar", figsize = ( 16, 8 ), edgecolor = "firebrick", width = 0.65 )

plt.title( "SUPPLIERS REVENUE BY GEOGRAPHIC ZONE", 
           fontsize = 35, color = "firebrick", fontweight = "bold", pad = 30 )
plt.xlabel( "GEOGRAPHIC ZONE", 
            labelpad = 15, fontsize = 8.25, color = "firebrick",
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( " REVENUES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 rotation = 0, colors = "firebrick", labelsize = 10,
                 grid_color = "lightsalmon", grid_alpha = 0.8  )

plt.legend( title = "Suppliers", loc = "upper left", bbox_to_anchor = ( 1, 1 ), 
            facecolor= "ivory", edgecolor = "firebrick", shadow = True, 
            fontsize = 8, labelspacing = 1.0, borderaxespad = 3.0,
            title_fontproperties = { 'weight': 'bold', 'size': 11, 
                                     'style': 'italic' } )

plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from northwind import conn_db


# [ MOST PROFITABLE SUPPLIER BY GEOGRAPHIC ZONE ] 
#=============================================================================================================================
mostProfitSupplier = conn_db( query = '''
                                        SELECT  CASE
                                                        WHEN Country IN ( 'USA', 'Brazil', 'Canada' ) 
                                                                THEN 'America'
                                        			WHEN Country IN ( 'UK', 'Spain', 'Sweden', 'Germany', 'Italy', 'Norway', 
                                                                      'France', 'Denmark', 'Netherlands', 'Finland' ) 
                                                                THEN 'Europe'
                                        			WHEN Country IN ( 'Japan', 'Australia', 'Singapore' ) 
                                                                THEN 'Asia / Oceania'
                                        		END AS Location,
                                        
                                        		SupplierName, s.City, s.Country,
                                        		ROUND( SUM( Price * Quantity ), 2 ) AS Revenues
                                        
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
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
p_table = mostProfitSupplier.pivot_table( index = "LOCATION", columns = "SUPPLIER", values = "REVENUES", 
                          aggfunc = "sum", fill_value = None )
p_table.plot( kind = "bar", figsize = ( 10, 5 ) )

plt.title( "SUPPLIERS REVENUE BY GEOGRAPHIC ZONE" )
plt.xlabel( "GEOGRAPHIC ZONE" )
plt.ylabel( "REVENUES" )
plt.xticks( rotation = 0 )
plt.legend( title = "Suppliers", loc = "upper left", bbox_to_anchor = ( 1, 1 ) )
plt.show()
#=============================================================================================================================
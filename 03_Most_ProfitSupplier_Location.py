import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_pivotTable, create_labels, config_tickparams, create_legend


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
                                                
                                        FROM    [OrderDetails] od
                                        JOIN    [Products] p 
                                                ON od.ProductID = p.ProductID
                                        JOIN    [Suppliers] s 
                                                ON p.SupplierID = s.SupplierID 
                                        
                                        GROUP BY Location, s.SupplierID
                                        ORDER BY Location, Revenues DESC        
                                ''',
                                      
                        columns = [ 'LOCATION', 'SUPPLIER', 'CITY', 'COUNTRY', 'REVENUES' ]    )


print_table( title = "==[ SUPPLIERS REVENUE BY GEOGRAPHIC ZONE ]==", 
             df_name = mostProfitSupplier )



# GRÁFICA MATPLOTLIB (pivot_table)
#--------------------------------------------------------------------------------------------------------

create_pivotTable( style = "bmh", df_name = mostProfitSupplier, index = "LOCATION", 
                   columns = "SUPPLIER", values = "REVENUES", aggfunc = "sum", 
                   kind = "bar", figsize = ( 16, 10 ), edgecolor = "firebrick", 
                   width = 0.75, label = "SUPPLIERS REVENUE BY GEOGRAPHIC ZONE" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_labels( xlabel = "GEOGRAPHIC ZONE", 
               ylabel = " REVENUES" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 10, grid_color = "lightsalmon" )

create_legend( title = "Suppliers", loc = "upper left", bbox_to_anchor = ( 0, 1.02 ), 
               facecolor = "ivory", edgecolor = "firebrick", ncol = 3,
               fontsize = 8, labelspacing = 1.0, borderaxespad = 3.0 )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================
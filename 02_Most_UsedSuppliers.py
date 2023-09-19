import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_matplot, create_barh, create_labels, config_tickparams


# [ TOP USED SUPPLIERS ] 
#=============================================================================================================================
topUsedSuppliers = conn_db( query = '''
                                        SELECT  s.SupplierName, s.City, s.Country, 
                                                COUNT( s.SupplierID ) 
                                                    AS SuppliedProducts
                                        
                                        FROM    [Suppliers] s
                                        JOIN    [Products] p 
                                            ON s.SupplierID = p.SupplierID
                                
                                        GROUP BY s.SupplierID
                                        ORDER BY SuppliedProducts ASC
                                    ''',

                            columns = [ 'SUPPLIER', 'CITY', 'COUNTRY', 'PRODUCTS' ] )

print_table( title = "==[ MOST USED SUPPLIERS ]==", 
             df_name = topUsedSuppliers )



# GRÁFICA MATPLOTLIB
#--------------------------------------------------------------------------------------------------------

create_matplot( style = "bmh", nrows = 1, ncols = 1, figsize = ( 16, 8 ), 
                suptitle_label = "MOST USED SUPPLIERS" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_barh( y      = topUsedSuppliers[ "SUPPLIER" ], 
             width  = topUsedSuppliers[ "PRODUCTS" ], 
             edgecolor = "darkred", color_container = [ "indianred", "orange" ],
             fmt = " {:,.0f} products", label_type = "edge", 
             fontweight = "semibold", fontsize = 7, color_label = "dimgray" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_labels( xlabel = "TOTAL SUPPLIED PRODUCTS",
               ylabel = "SUPPLIERS" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 8, grid_color = "lightsalmon" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================


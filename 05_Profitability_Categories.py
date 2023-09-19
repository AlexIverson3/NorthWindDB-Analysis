import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_pivotTable, create_labels, config_tickparams, create_legend



# [ EMPLOYEES - PROFITABILITY BY CATEGORY ]
#=============================================================================================================================
profitProdCategory = conn_db( query = '''
                                        SELECT  c.CategoryName,
                                                p.ProductName,
                                                Price, Cost,
                                                SUM( od.Quantity ) AS Sales,
                                                ROUND( SUM( od.Quantity )* Price ) AS Revenues,
                                                ROUND( ( Price - Cost ) / Price * 100, 2 ) AS Profitability
                                            
                                        FROM    [OrderDetails] od
                                        JOIN    [Products] p 
                                            ON od.ProductID = p.ProductID
                                        JOIN    [Categories] c 
                                            ON p.CategoryID = c.CategoryID 
                                            
                                        GROUP BY c.CategoryName, Profitability
                                        ORDER BY c.CategoryName, Profitability DESC
                                     ''',
                                  
                          columns = [ 'CATEGORY', 'PRODUCT', 'PRICE', 'COST', 'SALES', 'REVENUES', 'PROFITABILITY' ] )


print_table( title = "==[ PROFITABILITY BETWEEN CATEGORIES ]==", 
             df_name = profitProdCategory )



# GRÁFICA MATPLOTLIB
#--------------------------------------------------------------------------------------------------------

create_pivotTable( style = "bmh", df_name = profitProdCategory, index = "CATEGORY", 
                   columns = "PRODUCT", values = "PROFITABILITY", aggfunc = "sum", 
                   kind = "bar", figsize = ( 16, 10 ), edgecolor = "dimgray", 
                   width = 0.85, label = "PROFITABILITY BETWEEN CATEGORIES" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_labels( xlabel = "CATEGORY", 
               ylabel = " PROFITABILITY (%)" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 10, grid_color = "lightsalmon" )

create_legend( title = "PRODUCTS", loc = "upper left", bbox_to_anchor = ( 1, 1 ), 
               facecolor = "ivory", edgecolor = "firebrick", ncol = 2, 
               fontsize = 6, labelspacing = 1.15, borderaxespad = 3.0 )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================
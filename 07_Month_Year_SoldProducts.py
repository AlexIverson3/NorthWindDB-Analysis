import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_pivotTable, create_labels, config_tickparams, create_legend


# [ MONTHLY AND YEARLY PRODUCT SALES ]
#=============================================================================================================================
prodSalesMmYy = conn_db( query = '''
                                    SELECT	STRFTIME( "%Y", o.OrderDate ) AS Year,
											STRFTIME( "%Y-%m", o.OrderDate ) AS Month,
		                                    p.ProductName, 
                                      		SUM(od.Quantity) AS ProductSales
                                      		
                                    FROM    [Products] p
                                    JOIN    [Orders] o 
                                            ON od.OrderID = O.OrderID
                                    JOIN    [OrderDetails] od 
                                            ON p.ProductID = od.ProductID
                                    
                                    GROUP BY Month, p.ProductName
                                    ORDER BY OrderDate
                                 ''',
                                 
                         columns = [ 'YEAR', 'MONTH', 'PRODUCT', 'TOTAL SALES' ] )


print_table( title = "==[ MONTH SALES & YEAR SALES BY PRODUCTS ]==", 
             df_name = prodSalesMmYy )



# GRÁFICA MATPLOTLIB (pivot_table)
#--------------------------------------------------------------------------------------------------------
create_pivotTable( style = "bmh", df_name = prodSalesMmYy, index = "MONTH", 
                   columns = "PRODUCT", values = "TOTAL SALES", aggfunc = "sum", 
                   kind = "bar", figsize = ( 16, 10 ), edgecolor = "dimgray", 
                   width = 0.85, label = "TOP MONTH SALES PRODUCTS" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_labels( xlabel = "MONTH OF THE YEAR", 
               ylabel = "TOTAL SALES" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 10, grid_color = "lightsalmon" )

create_legend( title = "Products", loc = "upper left", bbox_to_anchor = ( 1, 1 ), 
               facecolor = "ivory", edgecolor = "firebrick", ncol = 2, 
               fontsize = 6, labelspacing = 1.15, borderaxespad = 3.0 )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================
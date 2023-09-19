import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_matplot, create_subplot, create_bar, create_labels, config_tickparams



# [ TOP 10 - MOST PROFITABLE PRODUCTS ]
#=============================================================================================================================
mostProfitableProd = conn_db( query = '''
                                        SELECT  p.ProductName,
                                        		    Price, Cost,
                                        		    SUM( od.Quantity ) AS Sales,
                                        		    ROUND( SUM( od.Quantity )* Price ) AS Revenues,
                                        		    ROUND( ( Price - Cost ) / Price * 100, 2 ) AS Profitability

                                        FROM    [OrderDetails] od
                                        JOIN    [Products] p 
                                            ON od.ProductID = p.ProductID

                                        GROUP BY p.ProductName, Profitability
                                        ORDER BY Profitability DESC
                                        LIMIT 10
                                      ''',
                                  
                              columns = [ 'PRODUCT', 'PRICE', 'COST', 'SALES', 'REVENUES', 'PROFITABILITY' ] )


print_table( title = "==[ MOST PROFITABLE PRODUCTS (TOP 10) ]==", 
             df_name = mostProfitableProd )



# GRÁFICA MATPLOTLIB
#--------------------------------------------------------------------------------------------------------

products    = mostProfitableProd[ "PRODUCT" ].apply( lambda x: x.replace(" ", "\n") )
sales       = mostProfitableProd[ "SALES" ]
profitab    = mostProfitableProd[ "PROFITABILITY" ]

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_matplot ( style = "bmh", nrows = 2, ncols = 1, figsize = ( 16, 8 ), 
                 suptitle_label = "TOP 10 - MOST PROFITABLE PRODUCTS" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#  --[ PLOT 1 ]--
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_subplot( nrows = 2, ncols = 1, index = 1, 
                label = "[ MOST PROFITABLE PRODUCTS ]" )

create_bar( x       = products,
            height  = profitab, 
            edgecolor = "darkred", color_container = "orange", 
            fmt = "{:,.0f} %", label_type = "center", 
            fontweight = "bold", fontsize = 14, color_label = "firebrick" )

create_labels( xlabel = "PRODUCTS", 
               ylabel = " PROFITABILITY (%)" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 9, grid_color = "lightsalmon" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#  --[ PLOT 2 ]--
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_subplot( nrows = 2, ncols = 1, index = 2, 
                label = "[ TOTAL SALES OF THE PRODUCTS ]" )

create_bar( x       = products,
            height  = sales, 
            edgecolor = "mediumblue", color_container = "cornflowerblue", 
            fmt = "{:,.0f} uds.", label_type = "center", 
            fontweight = "bold", fontsize = 10, color_label = "snow" )

create_labels( xlabel = "PRODUCTS", 
               ylabel = " TOTAL SALES" )

config_tickparams( direction = "out", rotation = 0, colors = "royalblue", 
                   labelsize = 9, grid_color = "lightsalmon" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================
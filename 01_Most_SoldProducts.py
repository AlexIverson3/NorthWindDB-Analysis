import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_matplot, create_subplot, create_bar, create_labels, config_tickparams


# [ TOP 10 - MOST SOLD PRODUCTS ]
#=============================================================================================================================
topSoldProduct = conn_db(   query = ''' 
                                        SELECT  p.ProductName, p.Unit, p.Price, 
                                                SUM( od.Quantity ) 
                                                    AS TotalSoldProducts,
                                                ROUND( SUM( od.Quantity ) * p.Price, 2 ) 
                                                    AS TotalRevenues
                                            
                                        FROM    [Products] p
                                        JOIN    [OrderDetails] od 
                                            ON p.ProductID = od.ProductID
                                            
                                        GROUP BY ProductName
                                        ORDER BY TotalSoldProducts DESC 
                                        LIMIT 10 
                                    ''',
                                  
                            columns = [ 'PRODUCT', 'UNIT CONTENT', 'PRICE', 'TOTAL SALES', 'TOTAL REVENUES' ]   ) 


print_table( title = "==[ MOST SOLD PRODUCTS (TOP 10) ]==", 
             df_name = topSoldProduct )



# GRÁFICA MATPLOTLIB
#--------------------------------------------------------------------------------------------------------

products    = topSoldProduct[ "PRODUCT" ].apply( lambda x: x.replace(" ", "\n") )
sales       = topSoldProduct[ "TOTAL SALES" ]
revenues    = topSoldProduct[ "TOTAL REVENUES" ]

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_matplot ( style = "bmh", nrows = 2, ncols = 1, figsize = ( 16, 8 ), 
                 suptitle_label = "TOP 10 - MOST SOLD PRODUCTS" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
#  --[ PLOT 1 ]--
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_subplot( nrows = 2, ncols = 1, index = 1, 
                label = "[ MOST SALES BY PRODUCT ]" )

create_bar( x       = products,
            height  = sales, 
            edgecolor = "mediumblue", color_container = "cornflowerblue", 
            fmt = "{:,.0f} uds.", label_type = "center", 
            fontweight = "bold", fontsize = 9, color_label = "snow" )

create_labels( xlabel = "PRODUCTS", 
               ylabel = "TOTAL SALES" )

config_tickparams( direction = "out", rotation = 0, colors = "royalblue", 
                   labelsize = 9, grid_color = "skyblue" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

#  --[ PLOT 2 ]--
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_subplot( nrows = 2, ncols = 1, index = 2, 
                label = "[ TOTAL REVENUES OF THE TOP 10 MOST SALES PRODUCTS ]" )

create_bar( x       = products,
            height  = revenues, 
            edgecolor = "darkred", color_container = "orange", 
            fmt = "${:,.0f}", label_type = "center", 
            fontweight = "bold", fontsize = 9, color_label = "firebrick" )

create_labels( xlabel = "PRODUCTS", 
               ylabel = "TOTAL REVENUES" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 9, grid_color = "wheat" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

plt.tight_layout()
plt.show()
#--------------------------------------------------------------------------------------------------------

#=============================================================================================================================
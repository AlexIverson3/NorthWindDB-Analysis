import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_matplot, create_subplot, create_bar, create_labels, config_tickparams



# [ MOST EFFICIENT EMPLOYEES ]
#=============================================================================================================================
mostEfficEmployee = conn_db( query = '''
                                        SELECT  SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName AS Employee,
                                                SUM( od.Quantity ) AS Sales,
                                                ROUND( SUM( od.Quantity )* p.Price ) 
                                                    AS Revenues,
                                                ROUND( ROUND( SUM( od.Quantity )* p.Price ) / SUM( od.Quantity ) ) 
                                                    AS AvgRevSale

                                        FROM    [Employees] e
                                        JOIN    [Orders] o 
                                            ON o.EmployeeID = e.EmployeeID
                                        JOIN    [OrderDetails] od 
                                            ON od.OrderID = o.OrderID
                                        JOIN    [Products] p
                                            ON od.ProductID = p.ProductID

                                        GROUP BY e.EmployeeID
                                        ORDER BY Sales DESC
                                     ''',
                                  
                             columns = [ 'EMPLOYEE', 'TOTAL SALES', 'TOTAL REVENUES', 'AVG. REVENUE ORDER' ] )


print_table( title = "==[ MOST EFFICIENT EMPLOYEES ]==", 
             df_name = mostEfficEmployee )




# GRÁFICA MATPLOTLIB
#--------------------------------------------------------------------------------------------------------

employee    = mostEfficEmployee[ "EMPLOYEE" ]
sales       = mostEfficEmployee[ "TOTAL SALES" ]
revenue     = mostEfficEmployee[ "TOTAL REVENUES" ]
avg_revOrd  = mostEfficEmployee[ "AVG. REVENUE ORDER" ]

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_matplot ( style = "bmh", nrows = 2, ncols = 1, figsize = ( 16, 8 ), 
                 suptitle_label = "MOST EFFICIENT EMPLOYEES" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# --[ PLOT 1 ]--
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_subplot( nrows = 2, ncols = 1, index = 1, 
                label = "[ TOTAL SALES BY EMPLOYEE ]" )

create_bar( x       = employee,
            height  = sales, 
            edgecolor = "darkred", color_container = "orange", 
            fmt = "{:,.0f} uds.", label_type = "center", 
            fontweight = "bold", fontsize = 10, color_label = "firebrick" )

create_labels( xlabel = "EMPLOYEES", 
               ylabel = " TOTAL SALES" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 9, grid_color = "lightsalmon" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# --[ PLOT 2 ]--
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_subplot( nrows = 2, ncols = 1, index = 2, 
                label = "[ TOTAL REVENUE BY EMPLOYEE ]" )

create_bar( x       = employee,
            height  = revenue, 
            edgecolor = "mediumblue", color_container = "cornflowerblue", 
            fmt = "${:,.0f}", label_type = "center", 
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
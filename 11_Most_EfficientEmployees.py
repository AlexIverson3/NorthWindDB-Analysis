import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db



# [ MOST EFFICIENT EMPLOYEES ]
#=============================================================================================================================
mostEfficEmployee = conn_db( query = '''
                                        SELECT  SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName AS Employee,
                                                SUM( od.Quantity ) AS Sales,
                                                ROUND( SUM( od.Quantity )* p.Price ) AS Revenues,
                                                ROUND( ROUND( SUM( od.Quantity )* p.Price ) / SUM( od.Quantity ) ) AS AvgRevSale

                                        FROM [Employees] e
                                        JOIN [Orders] o 
                                            ON o.EmployeeID = e.EmployeeID
                                        JOIN [OrderDetails] od 
                                            ON od.OrderID = o.OrderID
                                        JOIN [Products] p
                                            ON od.ProductID = p.ProductID

                                        GROUP BY e.EmployeeID
                                        ORDER BY Sales DESC
                                     ''',
                                  
                             columns = [ 'EMPLOYEE', 'TOTAL SALES', 'TOTAL REVENUES', 'AVG. REVENUE ORDER' ] )

print("\n==[ MOST EFFICIENT EMPLOYEES ]==")
print( tabulate( mostEfficEmployee, headers = "keys", tablefmt= "pretty" ) )



# GRÁFICA MATPLOTLIB
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
employee    = mostEfficEmployee[ "EMPLOYEE" ]
sales       = mostEfficEmployee[ "TOTAL SALES" ]
revenue     = mostEfficEmployee[ "TOTAL REVENUES" ]
avg_revOrd  = mostEfficEmployee[ "AVG. REVENUE ORDER" ]
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.style.use( "bmh" )

fig, ( ax1, ax2 )  = plt.subplots( nrows = 2, ncols = 1, 
                                   figsize = ( 16, 8 ) )

fig.align_labels()

plt.suptitle( "MOST EFFICIENT EMPLOYEES", 
              fontsize = 35, color = "firebrick", fontweight = "bold" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# PLOT 1
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 211 )
plt.title( "[ TOTAL SALES BY EMPLOYEE ]", 
           color = "snow", fontweight = "bold", fontsize = 9, 
           loc = "right", bbox={ 'facecolor':'indianred', 
                                 'boxstyle': 'round, pad=0.30' } )

bar_profitab = plt.bar( x = employee, height = sales, 
                        edgecolor = "darkred", 
                        color = "orange" )

plt.bar_label( bar_profitab, fmt = "{:,.0f} uds.", label_type = "center",
               fontsize = 10, fontweight = "bold", color = "firebrick" )

plt.xlabel( "EMPLOYEES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( " TOTAL SALES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "firebrick", labelsize = 9, rotation = 0, 
                 grid_color = "lightsalmon", grid_alpha = 0.8 )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# PLOT 2
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 212 )
plt.title( "[ TOTAL REVENUE BY EMPLOYEE ]", 
           color = "snow", fontweight = "bold", fontsize = 9, 
           loc = "right", bbox={ 'facecolor':'indianred', 
                                 'boxstyle': 'round, pad=0.30' } )

bar_sales = plt.bar( x = employee, height = revenue, 
                     edgecolor = "mediumblue", 
                     color = "cornflowerblue" )

plt.bar_label( bar_sales, fmt = "${:,.0f}", label_type = "center",
               fontsize = 10, fontweight = "bold", color = "snow" )

plt.xlabel( "PRODUCTS", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 }  )
plt.ylabel( " TOTAL SALES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "royalblue", labelsize = 9, rotation = 0, 
                 grid_color = "lightsalmon", grid_alpha = 0.8 )

plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================
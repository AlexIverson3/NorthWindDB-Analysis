import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db


# [ TOP EMPLOYEES MONTH SALES ]
#=============================================================================================================================
topEmpMonthSales = conn_db( query = '''
                                        SELECT	STRFTIME( '%Y-%m', o.OrderDate ) AS Month,
                                                SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName AS Employee,
                                                COUNT(o.OrderID) AS TotalSales                                                 
                                        
                                        FROM [Employees] e
                                        JOIN [Orders] o ON e.EmployeeID = o.EmployeeID
                                        JOIN [OrderDetails] od ON od.OrderID = O.OrderID
                                        
                                        GROUP BY Month, Employee
                                        ORDER BY TotalSales DESC, Month
                                    ''',
                                 
                            columns = [ 'MONTH', 'EMPLOYEE', 'TOTAL SALES' ] )

print("\n==[ TOP EMPLOYEES MONTH SALES ]==")
print( tabulate( topEmpMonthSales, headers = "keys", tablefmt = "pretty" ) )


# GRÁFICA MATPLOTLIB (pivot_table)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
plt.style.use( "bmh" )

p_table = topEmpMonthSales.pivot_table( index = "MONTH", columns = "EMPLOYEE", values = "TOTAL SALES", 
                                        aggfunc = "sum", fill_value = None )
p_table.plot( kind = "bar", figsize = ( 16, 8 ), edgecolor = "firebrick", width = 0.65 )

plt.title( "TOP EMPLOYEES MONTH SALES", 
           fontsize = 35, color = "firebrick", fontweight = "bold", pad = 30 )
plt.xlabel( "MONTH OF THE YEAR", 
            labelpad = 15, fontsize = 8.25, color = "firebrick",
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( "TOTAL SALES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 rotation = 0, colors = "firebrick", labelsize = 10,
                 grid_color = "lightsalmon", grid_alpha = 0.8  )

plt.legend( title = "EMPLOYEES", loc = "best", bbox_to_anchor = ( 1, 1 ), 
            facecolor= "ivory", edgecolor = "firebrick", shadow = True, 
            fontsize = 9, labelspacing = 1.0, borderaxespad = 0.5,
            title_fontproperties = { 'weight': 'bold', 'size': 11, 
                                     'style': 'italic' } )

plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================
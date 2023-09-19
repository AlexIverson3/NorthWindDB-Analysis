import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_pivotTable, create_labels, config_tickparams, create_legend


# [ TOP EMPLOYEES MONTH SALES ]
#=============================================================================================================================
topEmpMonthSales = conn_db( query = '''
                                        SELECT	STRFTIME( '%Y-%m', o.OrderDate ) AS Month,
                                                SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName 
                                                        AS Employee,
                                                COUNT(o.OrderID) AS TotalSales                                                 
                                        
                                        FROM    [Employees] e
                                        JOIN    [Orders] o 
                                                ON e.EmployeeID = o.EmployeeID
                                        JOIN    [OrderDetails] od 
                                                ON od.OrderID = O.OrderID
                                        
                                        GROUP BY Month, Employee
                                        ORDER BY TotalSales DESC, Month
                                    ''',
                                 
                            columns = [ 'MONTH', 'EMPLOYEE', 'TOTAL SALES' ] )


print_table( title = "==[ TOP EMPLOYEES MONTH SALES ]==", 
             df_name = topEmpMonthSales )



# GRÁFICA MATPLOTLIB (pivot_table)
#--------------------------------------------------------------------------------------------------------

create_pivotTable( style = "bmh", df_name = topEmpMonthSales, index = "MONTH", 
                   columns = "EMPLOYEE", values = "TOTAL SALES", aggfunc = "sum", 
                   kind = "bar", figsize = ( 16, 8 ), edgecolor = "firebrick", 
                   width = 0.65, label = "TOP EMPLOYEES MONTH SALES" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_labels( xlabel = "MONTH OF THE YEAR", 
               ylabel = "TOTAL SALES" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 10, grid_color = "lightsalmon" )

create_legend( title = "Employees", loc = "best", bbox_to_anchor = ( 1, 1 ), 
               facecolor = "ivory", edgecolor = "firebrick", ncol = 1, 
               fontsize = 9, labelspacing = 1.0, borderaxespad = 0.5 )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================
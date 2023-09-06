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
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
p_table = topEmpMonthSales.pivot_table( index = "MONTH", columns = "EMPLOYEE", values = "TOTAL SALES", 
                          aggfunc = "sum", fill_value = None )
p_table.plot( kind = "bar", figsize = ( 10, 5 ) )

plt.title( "TOP EMPLOYEES MONTH SALES" )
plt.xlabel( "MONTH OF THE YEAR" )
plt.ylabel( "TOTAL SALES" )
plt.xticks( rotation = 0 )
plt.legend( title = "EMPLOYEES", loc = "upper left", bbox_to_anchor = ( 1, 1 ) )
plt.show()
#=============================================================================================================================
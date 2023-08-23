import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db



# [ EMPLOYEES - MOST SALES FOR EACH CATEGORIES ]
#=============================================================================================================================
empSalesForCat = conn_db( query = '''
                                        SELECT  SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName AS Employee,
                                        		c.CategoryName,
                                        		SUM(od.Quantity) AS SalesEmployee
                                          
                                        FROM [Employees] e
                                        JOIN [Orders] o ON o.EmployeeID = e.EmployeeID
                                        JOIN [OrderDetails] od ON od.OrderID = o.OrderID
                                        JOIN [Products] p ON p.ProductID = od.ProductID
                                        JOIN [Categories] c	ON c.CategoryID = p.CategoryID
                                        
                                        GROUP BY c.CategoryName, Employee
                                        ORDER BY SalesEmployee DESC
                                  ''',
                                  
                          columns = [ 'EMPLOYEE', 'CATEGORY', 'SALES' ] )

print("\n==[ MOST SALES OF THE EMPLOYEES FOR EACH CATEGORY ]==")
print( tabulate( empSalesForCat, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
p_table = empSalesForCat.pivot_table( index = "CATEGORY", columns = "EMPLOYEE", values = "SALES", 
                          aggfunc = "sum", fill_value = None )
p_table.plot( kind = "bar", figsize = ( 10, 5 ) )

plt.title( "TOP EMPLOYEE MOST SALES IN EACH CATEGORY" )
plt.xlabel( "CATEGORY" )
plt.ylabel( "SALES" )
plt.xticks( rotation = 0 )
plt.legend( title = "Suppliers", loc = "upper left", bbox_to_anchor = ( 1, 1 ) )
plt.show()
#=============================================================================================================================

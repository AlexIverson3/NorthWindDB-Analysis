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
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
plt.style.use( "bmh" )

p_table = empSalesForCat.pivot_table( index = "CATEGORY", columns = "EMPLOYEE", values = "SALES", 
                                      aggfunc = "sum", fill_value = None )
p_table.plot( kind = "bar", figsize = ( 16, 8 ), edgecolor = "firebrick", width = 0.65 )

plt.title( "TOP EMPLOYEE MOST SALES IN EACH CATEGORY", 
           fontsize = 35, color = "firebrick", fontweight = "bold", pad = 30 )
plt.xlabel( "CATEGORY", 
            labelpad = 15, fontsize = 8.25, color = "firebrick",
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( " SALES", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 rotation = 0, colors = "firebrick", labelsize = 10,
                 grid_color = "lightsalmon", grid_alpha = 0.8  )

plt.legend( title = "Employees", loc = "best", bbox_to_anchor = ( 1, 1 ), 
            facecolor= "ivory", edgecolor = "firebrick", shadow = True, 
            fontsize = 9, labelspacing = 1.0, borderaxespad = 0.5,
            title_fontproperties = { 'weight': 'bold', 'size': 11, 
                                     'style': 'italic' } )

plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================

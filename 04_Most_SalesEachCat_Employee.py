import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_pivotTable, create_labels, config_tickparams, create_legend



# [ EMPLOYEES - MOST SALES FOR EACH CATEGORIES ]
#=============================================================================================================================
empSalesForCat = conn_db( query = '''
                                        SELECT  SUBSTR( e.FirstName, 1, 1 ) || ". " || e.LastName AS Employee,
                                        		c.CategoryName,
                                        		SUM( od.Quantity ) AS SalesEmployee
                                          
                                        FROM    [Employees] e
                                        JOIN    [Orders] o 
                                          ON o.EmployeeID = e.EmployeeID
                                        JOIN    [OrderDetails] od 
                                          ON od.OrderID = o.OrderID
                                        JOIN    [Products] p 
                                          ON p.ProductID = od.ProductID
                                        JOIN    [Categories] c	
                                          ON c.CategoryID = p.CategoryID
                                        
                                        GROUP BY c.CategoryName, Employee
                                        ORDER BY SalesEmployee DESC
                                  ''',
                                  
                          columns = [ 'EMPLOYEE', 'CATEGORY', 'SALES' ] )


print_table( title = "==[ MOST SALES OF THE EMPLOYEES FOR EACH CATEGORY ]==", 
             df_name = empSalesForCat )



# GRÁFICA MATPLOTLIB
#--------------------------------------------------------------------------------------------------------

create_pivotTable( style = "bmh", df_name = empSalesForCat, index = "CATEGORY", 
                   columns = "EMPLOYEE", values = "SALES", aggfunc = "sum", 
                   kind = "bar", figsize = ( 16, 8 ), edgecolor = "firebrick", 
                   width = 0.65, label = "TOP EMPLOYEES MOST SALES IN EACH CATEGORY" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_labels( xlabel = "CATEGORY", 
               ylabel = " SALES" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 10, grid_color = "lightsalmon" )

create_legend( title = "Employees", loc = "best", bbox_to_anchor = ( 1, 1 ), 
               facecolor = "ivory", edgecolor = "firebrick", ncol = 1,
               fontsize = 8, labelspacing = 1.15, borderaxespad = 0.5 )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================

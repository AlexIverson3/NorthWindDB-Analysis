import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db


# [ AVG TICKET CUSTOMER ]
#=============================================================================================================================
avgTicketCustomer = conn_db( query = '''
                                        SELECT 	c.CustomerName, c.Country,
                                                ROUND( (od.Quantity * p.Price / 1.00), 2 ) AS AvgPriceTicket

                                        FROM 	[Customers] c
                                        JOIN 	[Orders] o 
                                                    ON o.CustomerID = c.CustomerID
                                        JOIN 	[OrderDetails] od 
                                                    ON od.OrderID = o.OrderID
                                        JOIN 	[Products] p 
                                                    ON p.ProductID = od.ProductID

                                        GROUP BY c.CustomerName
                                        ORDER BY AvgPriceTicket DESC
                                        
                                        LIMIT 15
                                     ''',
                                 
                            columns = [ 'CUSTOMER', 'COUNTRY', 'AVERAGE TICKET' ] )

print("\n==[ AVERAGE TICKET BY CUSTOMER ]==")
print( tabulate( avgTicketCustomer, headers = "keys", tablefmt = "pretty" ) )



# GRÁFICA MATPLOTLIB
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
customer = avgTicketCustomer[ "CUSTOMER" ].apply( lambda x: x.replace(" ", "\n") ) 
avg_ticket = avgTicketCustomer[ "AVERAGE TICKET" ]
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.style.use( "bmh" )

fig, ax = plt.subplots( nrows = 1, ncols = 1, 
                        figsize = ( 16, 10 ) )

plt.suptitle( "TOP 15 - AVERAGE TICKET BY CUSTOMER", 
              fontsize = 35, color = "firebrick", fontweight = "bold" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
bar_avgticket = plt.bar( x = customer, height = avg_ticket,
                         color = [ "indianred", "orange" ], 
                         edgecolor = "darkred" )

plt.bar_label( bar_avgticket, fmt = "${:,.0f}", label_type = "center",
               fontsize = 10, fontweight = "bold", color = "snow" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.xlabel( "CUSTOMER", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( " AVERAGE TICKET", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "firebrick", labelsize = 9,
                 grid_color = "lightsalmon", grid_alpha = 0.8 )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================
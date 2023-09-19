import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_matplot, create_bar, create_labels, config_tickparams


# [ AVG TICKET CUSTOMER ]
#=============================================================================================================================
avgTicketCustomer = conn_db( query = '''
                                        SELECT 	c.CustomerName, c.Country,
                                                ROUND( ( od.Quantity * p.Price / 1.00 ), 2 ) 
                                                        AS AvgPriceTicket

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


print_table( title = "==[ AVERAGE TICKET BY CUSTOMER (TOP 15) ]==", 
             df_name = avgTicketCustomer )



# GRÁFICA MATPLOTLIB
#--------------------------------------------------------------------------------------------------------

customer = avgTicketCustomer[ "CUSTOMER" ].apply( lambda x: x.replace(" ", "\n") ) 
avg_ticket = avgTicketCustomer[ "AVERAGE TICKET" ]

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_matplot ( style = "bmh", nrows = 1, ncols = 1, figsize = ( 16, 10 ), 
                 suptitle_label = "TOP 15 - AVERAGE TICKET BY CUSTOMER" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_bar( x       = customer,
            height  = avg_ticket, 
            edgecolor = "darkred", color_container = [ "indianred", "orange" ], 
            fmt = "${:,.0f}", label_type = "center", 
            fontweight = "bold", fontsize = 10, color_label = "snow" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_labels( xlabel = "CUSTOMER", 
               ylabel = " AVERAGE TICKET" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 9, grid_color = "lightsalmon" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================
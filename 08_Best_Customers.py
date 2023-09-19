import matplotlib.pyplot as plt
from functions import conn_db, print_table, create_matplot, create_subplot, create_bar, create_labels, config_tickparams


# [ BEST CUSTOMERS ]
#=============================================================================================================================
bestCustomers = conn_db( query = '''
                                        SELECT  c.ContactName, 
                                                COUNT( o.OrderID ) AS CustomerOrders,
                                                ROUND( SUM( od.Quantity ) * p.Price ) 
                                                        AS PurchaseExpenditure,
                                                ROUND( SUM( od.Quantity ) * p.Price / COUNT( o.OrderID ) ) 
                                                        AS AvgPurchase
                                        
                                        FROM    [Customers] c
                                        JOIN    [Orders] o 
                                                ON c.CustomerID = o.CustomerID
                                        JOIN    [OrderDetails] od 
                                                ON o.OrderID = od.OrderID
                                        JOIN    [Products] p
                                                ON od.ProductID = p.ProductID
                                        
                                        GROUP BY c.ContactName
                                        ORDER BY CustomerOrders DESC, AvgPurchase DESC
                                        LIMIT 10
                                 ''',
                                 
                         columns = [ 'CUSTOMERS', 'TOTAL ORDERS', 'PURCHASE', 'AVG PURCHASE' ] )


print_table( title = "==[ BEST CUSTOMERS (TOP 10) ]==", 
             df_name = bestCustomers )



# GRÁFICA MATPLOTLIB
#--------------------------------------------------------------------------------------------------------

customers       = bestCustomers[ "CUSTOMERS" ] 
orders          = bestCustomers[ "TOTAL ORDERS" ]
purchase        = bestCustomers[ "PURCHASE" ]
avg_purchase    = bestCustomers[ "AVG PURCHASE" ]

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_matplot ( style = "bmh", nrows = 2, ncols = 1, figsize = ( 16, 10 ), 
                 suptitle_label = "BEST COSTUMERS" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# --[ PLOT 1 ]--
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_subplot( nrows = 2, ncols = 1, index = 1, 
                label = "TOTAL ACCUMULATED PURCHASE" )

create_bar( x       = customers,
            height  = purchase, 
            edgecolor = "mediumblue", color_container = "cornflowerblue", 
            fmt = "${:,.0f}", label_type = "center", 
            fontweight = "bold", fontsize = 8, color_label = "snow" )

create_labels( xlabel = "CUSTOMERS", 
               ylabel = " PURCHASE" )

config_tickparams( direction = "out", rotation = 0, colors = "royalblue", 
                   labelsize = 9, grid_color = "skyblue" )


#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# --[ PLOT 2 ]--
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
create_subplot( nrows = 2, ncols = 1, index = 2, 
                label = "AVERAGE PURCHASE PER ORDER" )

create_bar( x       = customers,
            height  = avg_purchase, 
            edgecolor = "darkred", color_container = "orange", 
            fmt = "{:,.0f} €/order", label_type = "center", 
            fontweight = "bold", fontsize = 8, color_label = "firebrick" )

create_labels( xlabel = "CUSTOMERS", 
               ylabel = " AVG PURCHASE" )

config_tickparams( direction = "out", rotation = 0, colors = "firebrick", 
                   labelsize = 9, grid_color = "lightsalmon" )

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------
#=============================================================================================================================
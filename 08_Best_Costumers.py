import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db


# [ BEST CUSTOMERS ]
#=============================================================================================================================
bestCustomers = conn_db( query = '''
                                        SELECT  c.ContactName, 
                                                COUNT( o.OrderID ) AS CustomerOrders,
                                                ROUND( SUM( od.Quantity ) * p.Price ) AS PurchaseExpenditure,
                                                ROUND( SUM( od.Quantity ) * p.Price / COUNT( o.OrderID ) ) AS AvgPurchase
                                        
                                        FROM [Customers] c
                                        JOIN [Orders] o 
                                                ON c.CustomerID = o.CustomerID
                                        JOIN [OrderDetails] od 
                                                ON o.OrderID = od.OrderID
                                        JOIN [Products] p
                                                ON od.ProductID = p.ProductID
                                        
                                        GROUP BY c.ContactName
                                        ORDER BY CustomerOrders DESC, AvgPurchase DESC
                                        LIMIT 10
                                 ''',
                                 
                         columns = [ 'CUSTOMERS', 'TOTAL ORDERS', 'PURCHASE', 'AVG PURCHASE' ] )

print("\n==[ BEST CUSTOMERS ]==")
print( tabulate( bestCustomers, headers = "keys", tablefmt= "pretty" ) )
print()


# GRÁFICA MATPLOTLIB
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
customers       = bestCustomers[ "CUSTOMERS" ] 
orders          = bestCustomers[ "TOTAL ORDERS" ]
purchase        = bestCustomers[ "PURCHASE" ]
avg_purchase    = bestCustomers[ "AVG PURCHASE" ]
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.style.use( "bmh" )

fig, ax = plt.subplots( nrows = 2, ncols = 1, 
                        figsize = ( 16, 10 ) )

fig.align_labels()

plt.suptitle( "BEST COSTUMERS", 
              fontsize = 35, color = "firebrick", fontweight = "bold" )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# PLOT 1
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 211 )

bar_purchase = plt.bar( x = customers, height = purchase,
                        edgecolor = "mediumblue", color = "cornflowerblue" )

plt.bar_label( bar_purchase, fmt = "${:,.0f}", label_type = "center",
               fontsize = 8, fontweight = "bold", color = "snow" )

plt.title( "TOTAL ACCUMULATED PURCHASE", 
           color = "snow", fontweight = "bold", fontsize = 9, 
           loc = "right", bbox={ 'facecolor':'indianred', 
                                 'boxstyle': 'round, pad=0.30' } )

plt.xlabel( "CUSTOMERS", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( " PURCHASE", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "royalblue", labelsize = 9, rotation = 0, 
                 grid_color = "skyblue", grid_alpha = 0.8 )
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
# PLOT 2
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.subplot( 212 )

bar_avgpurchase = plt.bar( x = customers, height = avg_purchase,
                           edgecolor = "darkred", color = "orange" )

plt.bar_label( bar_avgpurchase, fmt = "{:,.0f} €/order", label_type = "center",
               fontsize = 8, fontweight = "bold", color = "firebrick" )


plt.title( "AVERAGE PURCHASE PER ORDER", 
           color = "snow", fontweight = "bold", fontsize = 9, 
           loc = "right", bbox={ 'facecolor':'indianred', 
                                 'boxstyle': 'round, pad=0.30' } )

plt.xlabel( "CUSTOMERS", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )
plt.ylabel( " AVG PURCHASE", 
            labelpad = 15, fontsize = 8.25, color = "firebrick", 
            fontweight = "bold", bbox = { 'boxstyle': 'round', 
                                          'facecolor': 'linen',
                                          'edgecolor': 'firebrick', 
                                          'pad': 0.6 } )

plt.tick_params( direction = "out", length = 5, width = 1.5, 
                 colors = "firebrick", labelsize = 9, rotation = 0, 
                 grid_color = "lightsalmon", grid_alpha = 0.8 )


plt.tight_layout()
plt.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#=============================================================================================================================
import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db



# [ EMPLOYEES - MOST SALES FOR EACH CATEGORIES ]
#=============================================================================================================================
mostProfitableProd = conn_db( query = '''
                                        SELECT  p.ProductName,
                                        		Price, Cost,
                                        		SUM( od.Quantity ) AS Sales,
                                        		ROUND( SUM( od.Quantity )* Price ) AS Revenues,
                                        		ROUND( ( Price - Cost ) / Price * 100, 2 ) AS Profitability

                                        FROM [OrderDetails] od
                                        JOIN [Products] p 
                                            ON od.ProductID = p.ProductID

                                        GROUP BY p.ProductName, Profitability
                                        ORDER BY Profitability DESC
                                        LIMIT 10
                                      ''',
                                  
                              columns = [ 'PRODUCT', 'PRICE', 'COST', 'SALES', 'REVENUES', 'PROFITABILITY' ] )

print("\n==[ MOST PROFITABLE PRODUCTS ]==")
print( tabulate( mostProfitableProd, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
plt.style.use( "bmh" )
fig, ( ax1, ax2 ) = plt.subplots( nrows = 2, ncols = 1, sharex = True )
plt.suptitle( "MOST PROFITABLE PRODUCTS", fontsize = 40, color = "darkblue" )

mostProfitableProd.plot( ax = ax1, kind = "bar", figsize = ( 10, 1 ), legend = True,
                         y = "SALES", color = "skyblue" )
ax1.set_xlabel( "PRODUCTS", fontsize = 14 )
ax1.set_ylabel( "TOTAL SALES", fontsize = 14, color = "steelblue"  )
plt.xticks()

mostProfitableProd.plot( ax = ax2, kind = "bar", figsize = ( 10, 5 ), legend = True,
                         x = "PRODUCT", y = "PROFITABILITY" )
ax2.set_xlabel( "PRODUCTS", fontsize = 14, color = "blue" )
ax2.set_ylabel( "PROFITABILITY", fontsize = 14, color = "steelblue" )
plt.xticks( rotation = 45 )

plt.show()
#=============================================================================================================================
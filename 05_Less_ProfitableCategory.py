import matplotlib.pyplot as plt
from tabulate import tabulate
from functions import conn_db



# [ EMPLOYEES - MOST SALES FOR EACH CATEGORIES ]
#=============================================================================================================================
lessProfitCat = conn_db( query = '''
                                    SELECT  c.CategoryName,
                                    		p.ProductName,
                                    		Price, Cost,
                                    		SUM( od.Quantity ) AS Sales,
                                    		ROUND( SUM( od.Quantity )* Price ) AS Revenues,
                                    		ROUND( ( Price - Cost ) / Price * 100, 2 ) AS Profitability
                                          
                                    FROM [OrderDetails] od
                                    JOIN [Products] p 
                                        ON od.ProductID = p.ProductID
                                    JOIN [Categories] c 
                                        ON p.CategoryID = c.CategoryID 
                                        
                                    GROUP BY c.CategoryName, Profitability
                                    ORDER BY c.CategoryName, Profitability DESC
                                  ''',
                                  
                          columns = [ 'CATEGORY', 'PRODUCT', 'PRICE', 'COST', 'SALES', 'REVENUES', 'PROFITABILITY' ] )

print("\n==[ MOST SALES OF THE EMPLOYEES FOR EACH CATEGORY ]==")
print( tabulate( lessProfitCat, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
p_table = lessProfitCat.pivot_table( index = "CATEGORY", columns = "PRODUCT", values = "PROFITABILITY", 
                                     aggfunc = "sum", fill_value = None )
p_table.plot( kind = "bar", figsize = ( 10, 5 ) )

plt.title( "PROFITABILITY BY CATEGORY" )
plt.xlabel( "CATEGORY" )
plt.ylabel( "PROFITABILITY (%)" )
plt.xticks( rotation = 0 )
plt.legend( title = "PRODUCTS", loc = "upper left", bbox_to_anchor = ( 1, 1.05 ), 
            fontsize = 9, ncol = 2 )
plt.show()
#=============================================================================================================================
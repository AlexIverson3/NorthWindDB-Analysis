import matplotlib.pyplot as plt
from tabulate import tabulate
from northwind import conn_db


# [ TOP USED SUPPLIERS ] 
#=============================================================================================================================
topUsedSuppliers = conn_db( query = '''
                                        SELECT  s.SupplierName, s.City, s.Country, 
                                                COUNT(s.SupplierID) AS SuppliedProducts
                                        FROM [Suppliers] s
                                        JOIN [Products] p ON s.SupplierID = p.SupplierID
                                        GROUP BY s.SupplierID
                                        ORDER BY SuppliedProducts DESC
                                    ''',
                                    
                            columns = [ 'SUPPLIER', 'CITY', 'COUNTRY', 'PRODUCTS' ] )

print("\n==[ MOST USED SUPPLIERS ]==")
print( tabulate( topUsedSuppliers, headers = "keys", tablefmt= "pretty" ) )


# GRÁFICA MATPLOTLIB
#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
topUsedSuppliers.plot( x = "SUPPLIER", y = "PRODUCTS", kind = "bar",
                       figsize = ( 10, 5 ), legend = False )
plt.title( "MOST USED SUPPLIERS" )
plt.xlabel( "SuppliedProducts" )
plt.ylabel( "Suppliers" )
plt.xticks( rotation = 90 )
plt.show()
#=============================================================================================================================
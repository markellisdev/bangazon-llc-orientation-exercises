stockDict = { 'GM': 'General Motors', 'APL': 'Apple', 'CAT': 'Caterpillar' }

purchases = [ ( 'APL', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'APL', 200, '1-jul-1998', 56 ) ]

for purchase in purchases:
 	ticker = purchase[0]
 	full_company_name = stockDict[ticker]
 	full_purchase_price = purchase[1] * purchase[3]

 	print("I purchased {0} stock for ${1}".format(full_company_name, full_purchase_price))
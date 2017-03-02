# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(qty, prices,t,i):
	sale_price = []
	regular_price = []
	unknown = []
	res = []
	
	while (len(prices) > 0):
		
		'''
		print(prices)
		print(unknown)
		print(sale_price)
		print(regular_price)
		print("-------")
		'''
		price = prices.pop(0)
		
		if price % 4 == 0:
			# candidato a regular
			pct = int(price*0.75)

			if pct in sale_price:
				regular_price.append(price)
				sale_price.remove(pct)
				res.append(pct)
			else:
				sale_price.append(price)
		else:
			# No es regular
			sale_price.append(price)

	res = res
	res.sort()
	return res

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  itemqty = int(input())
  prices = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  
  #if i == 94:
  res = solve(itemqty,prices,itemqty, i)

  print("Case #{}:".format(str(i)) , " ".join([str(x) for x in res]))
  # check out .format's specification for more formatting options


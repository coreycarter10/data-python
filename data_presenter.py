cupcakes = open('CupcakeInvoices.csv')


# for line in cupcakes:
#     print(line)

for line in cupcakes:
  values = line.split(',')
  print(values[2])

cupcakes.seek(0, 0)
for line in cupcakes:
    invoice_total = 0
    line = line.rstrip('\n').split(',')
    cost = []
    value_one = float(line[-1])
    value_two = float(line[-2])
    order_total = value_one * value_two
    cost.append(order_total)
    print(cost)

invoice_total = 0

for line in cupcakes:
    values = line.split(',')
    invoice_total = invoice_total + (int(values[3]) * float(values[4]))

print(invoice_total)

cupcakes.close()

## Note: This will need to be run in Replit.com for visualization.
import matplotlib.pyplot as plt 
    
# x axis values 
x = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"] 
# corresponding y axis values 
y = [10,40,32,84,60,52,18] 
    
# plotting the points  
plt.plot(x, y) 
    
# naming the x axis 
plt.xlabel('Day Purchased') 
# naming the y axis 
plt.ylabel('Cupcakes Purchased') 
    
# giving a title to my graph 
plt.title('My Cupcake Sales') 
    
# function to show the plot 
plt.show() 
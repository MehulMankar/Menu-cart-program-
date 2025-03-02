#Menu cart program
menu={"fries":70,"burger":150,"pizza":250,"coke":50,"ice cream":100,"cold coffe":80,"popcorn":170,"sandwich":15,"tea":20}
cart=[]
total=0
print("********Menu*********")
for key,value in menu.items():
  print(f"{key:10}:::Rs.{value}")
print("***********************")  
while True:
  item=input("Enter the item you eould like to add to cart(q to quit):").lower()
  if item=="q":
    break
  elif menu.get(item) is not None:
   cart.append(item)
  else:
    print("Item not available" )
for item in cart:
  total+=menu.get(item)
  print(item,end= " ")
print()
print(f"Your total bill is Rs.{total}")
print("***********THANK YOU**********")
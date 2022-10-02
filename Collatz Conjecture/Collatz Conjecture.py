import matplotlib.pyplot as plt 
data = []
number = int(input("Type a number : "))
data.append(number)
new_number = 0 
while True:
  if number % 2 == 0:
    new_number = number / 2
    data.append(new_number)

  if number % 2 == 1:
    new_number = (number * 3) + 1
    data.append(new_number)
    
  if new_number == 1:
    break

  elif new_number == 0:
    print("Impossible")
    break
  number = new_number
  
print(data)

plt.plot(data)
plt.show()
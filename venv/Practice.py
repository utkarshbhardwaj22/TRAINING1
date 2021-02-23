profit=23.45
profit2= 76.45

total=profit+profit2
("The total is {}. The type is {}. The id is {}".format(total,type(total),id(total)))

total2=total

del total
#print(total) # total and corresponding data will be deleted

print(total2)

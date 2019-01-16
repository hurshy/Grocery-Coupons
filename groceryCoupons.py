#Tyler Hegewald
#Grocery Coupons
cost = float(input("Please enter the cost of your groceries: "))

if cost < 10:
    print("You earned a discount coupon of $0.")
elif cost >= 10 and cost <= 60:
    discount = cost * .08
    print("You earned a discount of $",discount,".", "(8% of your purchase)")
elif cost > 60 and cost <= 150:
    discount = cost * .1
    print("You earned a discount of $", discount, "(10% of your purchase)")
elif cost > 150 and cost <= 210:
    discount = cost * .12
    print("You earned a discount of $", discount, "(12% of your purchase)")
else:
    discount = cost * .14
    print("You earned a discount of $", discount, "(14% of your purchase)")



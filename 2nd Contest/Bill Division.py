def bonAppetit(bill, k, b):
    # Write your code here
    actual = 0
    for i in range(len(bill)):
        if i != k:
            actual += bill[i]
    actual = int(actual / 2)
    if b == actual:
        print("Bon Appetit")
    else:
        print(b - actual)
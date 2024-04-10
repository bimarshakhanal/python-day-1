def calculate_total_cost(**kwargs):
    total = 0
    print("*"*5,"Bill","*"*5)
    for item,price in kwargs.items():
        total += int(price)
        print(item,"\t",price)
    return total

if __name__=="__main__":
    print("Enter name and price of items bought. (item price)")
    print("Enter 0 to exit.")
    #dict to store item-price
    items = {}
    while True:
        item = input()
        
        #check end of input
        if item=='0': 
            break
        
        item = item.split()
        #update dict of item-price
        items[item[0]] = item[1]
    print("Total price: ",calculate_total_cost(**items))

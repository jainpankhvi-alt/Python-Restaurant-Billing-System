item=[]

def add():
    name=input('enter the name')
    price=float(input('enter the price'))
    qty=int(input('enter the qty'))

    data={'name':name
          ,'price':price,
          'qty':qty}
    item.append(data)
    print(name,'is added sucessfully')
    
def view():
    for i in item:
        print(f"""
Name       : {i['name']}
Price      : {i['price']}
Quantity   : {i['qty']}
Item Total : {i['price'] * i['qty']}
""")

def subtotal():
    total=0
    for i in item:
        total+=i['price']*i['qty']
    return total

def discount(subtotal):
    discount=0
    if subtotal>=5000: 
        discount=subtotal*0.20
    elif subtotal>=3000:
        discount=subtotal*0.15  
    elif subtotal>=2000:
        discount=subtotal*0.10
    else:
        discount=0
    subtotal-= discount
    return discount ,  subtotal    

def bill():
    total= subtotal()
    dis=discount(total)[0]
    final=discount(total)[1]
    print("\n==============================================")
    print("         RESTAURANT BILL")
    print("==============================================")
    view()
    print(f"\nsubtotal                                                      {total}")
    print(f"\ndiscount                                                      {dis}")
    print(f"\nfinal total amount                                            {final}")
    # print(discount(total))
        

        
while True:
    choice = input("""
========== RESTAURANT BILLING SYSTEM ==========

1. Add Item
2. Generate Bill & Exit

Enter your choice: """)
    if choice=='1':
          add()
    elif choice=='2':
        bill()
        print("\nThank you for visiting our restaurant!")
        print("Exiting...")
        break
    else:
        print('invalid input')    
    
    
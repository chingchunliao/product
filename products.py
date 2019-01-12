#記帳程式
products = [] #建立大清單
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
    p = [] #建立小清單
    # p.append(name) 
    # p.append(price)
    p = [name, price]
    products.append(p)
print(products)

for product in products:
    print(product[0], '的價格是', product[1])
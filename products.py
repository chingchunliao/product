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

with open('products.csv', 'w', encoding='utf-8') as f: # 打開檔案(csv檔)
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n' ) # 寫入檔案
import os # 載入模組


# 讀取檔案
def read_file(filename): # 加入參數可讀取不同檔案
    products = [] #建立大清單
    if os.path.isfile(filename): # 在同樣的資料夾檢查檔案 
        print('找到檔案')
        with open (filename, 'r', encoding='utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue #跳到下一個迴圈
                name, price = line.strip().split(',') #去掉換行符號\n 在切割字串
                products.append([name, price])
        print(products)
    else:
        print('找不到檔案.........')
    return products # 有return 才能存取

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break #跳出回圈
        price = input('請輸入價格: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products
# 印出所有購買紀錄
def print_product(products):
    for product in products:
        print(product[0], '的價格是', product[1]) # 沒有改變會增加所以不用回傳

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: # 打開檔案(csv檔)
        f.write('商品,價格\n')
        for product in products:
            f.write(product[0] + ',' + product[1] + '\n' ) 

# 使用function 
products = read_file('products.csv')
products = user_input(products)
print_product(products)
write_file('products.csv', products)
import os # 載入模組

products = [] #建立大清單
# 讀取檔案
if os.path.isfile('products.csv'): # 在同樣的資料夾檢查檔案 
    print('找到檔案')
    with open ('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #跳到下一個迴圈
            name, price = line.strip().split(',') #去掉換行符號\n 在切割字串
            products.append([name, price])
    print(products)
else:
    print('找不到檔案.........')

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break #跳出回圈
    price = input('請輸入價格: ')
    price = int(price)
    products.append([name, price])
print(products)
# 印出所有購買紀錄
for product in products:
    print(product[0], '的價格是', product[1])
# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: # 打開檔案(csv檔)
    f.write('商品,價格\n')
    for p in products:
        f.write(product[0] + ',' + product[1] + '\n' ) 
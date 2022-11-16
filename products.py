# While Loop通常適合: 執行未知次數的情況下使用

products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格:　')

    # 方法1
   	# p = []
	# p.append(name)
    # p.append(price)
    # products.append(p)
     
    # 方法2
    # p = [name, price]
    # products.append(p)

    # 方法三
    # products.append(p)
	products.append([name,price])

print(products)

for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
# +法 字串合併、\n 換行
# 檔案格式為csv檔

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
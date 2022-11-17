# 讀取檔案
# .split(',') 用逗點做分割,切割完結果會是清單
# .strip()除掉換行符號(\n)
# encoding = 'utf-8'讀取
# continue跟break一樣只能寫在迴圈裡
# continue即跳到下一迴
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 繼續
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)

# While Loop通常適合: 執行未知次數的情況下使用
# 讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格:　')
	prrice = int(price)
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

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
# +法 字串合併、\n 換行
# 檔案格式為csv檔
# 寫檔遇到整數
# 寫檔加入 encoding ='utf-8' 解決中文字變亂碼問題
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
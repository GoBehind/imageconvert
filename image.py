from PIL import Image
import os

#參數值'.'為目前資料夾可自己打目標資料夾名稱
for file in os.listdir('orig'):
	if file.endswith('.jpg'):
		#檔案前須加上資料夾名稱不然會找不到檔案
		#os.path.join()重要!!
		image_file = Image.open(os.path.join('orig/', file))
		image_file = image_file.convert('L')
		#儲存位置也需要打上目標資料夾名稱
		image_file.save(os.path.join('result/' + file[:-4] + '_grey.jpg'))
	else:
		print('not found')

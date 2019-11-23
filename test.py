import requests
import re
#1.'modify the uniform resource locator(url)html page'
html_url = 'https://www.711ci.com/pic/html28/2717.html'
#2.'modify the storage path root
path_root = '"D://Python_catch//picture//MZ_one//MZ_'
#3.'modify the regular_expression, but we can not modify in here'

'''
html_url = 'https://www.711ci.com/pic/html28/2717.html'
html_url_two = 'https://www.711ci.com/pic/html28/2711.html'

url_1 = 'https://img.997pp.com/tp/2018/08/2xrkbjvtabt.jpg'
url_4 = 'https://img.997pp.com/tp/2018/08/m3u03pnwh1e.jpg'
'''
pic_url_list = requests.get(html_url)

txt = pic_url_list.text
url_list = re.findall(r'"https://img.997pp.com/tp/2018/08/.*?"',txt)
print(len(url_list))
for url in url_list:
    print(url)
count = 1

try:
    for i in range(len(url_list)):
        catch_url = eval(url_list[i])
        pic = requests.get(catch_url)

        pic_name = url_list[i].split('/')[-1]

        path = eval(path_root + pic_name)

        with open(path, 'wb') as f:
            f.write(pic.content)
            
            f.close()
        print('第 {: ^2} 张图片抓取成功,图片名称 {}'.format(i + 1, pic_name))

except:
    print('图片存储失败!')
else:
    print('图片存储成功！')


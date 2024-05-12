import pytesseract
import re
from PIL import Image
import matplotlib.pyplot as plt

def EnglishGet(image_path):
    image = Image.open(image_path)
    image_str = pytesseract.image_to_string(image, lang='eng')
    print(image_str)
    return image_str

def ChineseGet(image_path):
    image = Image.open(image_path)
    image_str = pytesseract.image_to_string(image, lang='chi_sim')
    #print(image_str)
    image_str = DeletSpace(image_str)
    a = NameGet(image_str)
    b = NumberGet(image_str)
    c = EmailGet(image_str)
    #print(a,b,c)
    return a,b,c

def DeletSpace(string):#删除空格和空行
    string = re.sub(r'\n\s*\n','\n',string)
    #print(string)
    return string

def NumberGet(string):
    pattern = r'\d+'
    number = re.findall(pattern, string)
    number = "".join(number)
    #print(number)
    number = re.findall(r'\d{11}', number)
    print("电话号码是"+"".join(number))
    a = "".join(number)
    return a


def EmailGet(string):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", string)
    print("邮箱是 " + "".join(emails))
    a = "".join(emails)
    return a
    #print("邮箱是 "+ "".join(map(str,emails)))

def NameGet(string):
    #string = re.sub("[A-Za-z0-9\,\。]", "", string)
    pattern = "[\u4e00-\u9fa5]{2,4}"
    string = re.findall(pattern, string)
    #string = "".join(string)
    #string = string[0]+string[1]+string[2]
    #print("姓名是 " + string[0])
    #print("123"+str(string))
    if len(string) == 0:
        #string = ["未找到姓名"]
        a = ""
    else:
        a = string[0]
    print(a)
    return a

#EnglishGet('English.png')
ChineseGet('card2.png')


# 指定饼图的每个切片名称
'''labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# 指定每个切片的数值，从而决定了百分比
sizes = [15, 30, 45, 10]
#向外扩展率
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()'''

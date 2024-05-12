from peewee import *
import psycopg2
import os
db = PostgresqlDatabase('Card', host='127.0.0.1', port=5432, user='postgres', password='potato')
# 继承自 BaseModel，直接关联 db，并且也继承了 Model，Model 提供增删改查的函数


class BaseModel(Model):
    class Meta:
        database = db  # 将实体与数据库进行绑定


# 继承自 BaseModel，直接关联 db，并且也继承了 Model，Model 提供增删改查的函数
class card(BaseModel):
    user = CharField (verbose_name='用户名', max_length=10, null=False, index=True)
    name = CharField (verbose_name='姓名', max_length=10, null=False, index=True,default="未填写")
    gender = CharField(verbose_name='性别', null=False, default="未填写")
    number = CharField(verbose_name='手机号', max_length=11, null=False, default='未填写')
    email = CharField(verbose_name='邮箱', default='未填写')
    part = CharField(verbose_name='部门',default='未填写')

class users(BaseModel):
    accounts = CharField(verbose_name='用户名',max_length=10, null=False)
    passwords = CharField(verbose_name='用户名',max_length=20, null=False)

class iduser(BaseModel):
    accounts = CharField()
    passwords = CharField()

class potato8_card(BaseModel):
    name = CharField()
    gender = CharField()
    number = CharField()
    email = CharField()

class Image(BaseModel):
    name = CharField()
    image_data = BlobField()


class event(BaseModel):
    describe = CharField()
    members = CharField()
    time = CharField()
    place = CharField()

def save_images_from_directory():
    current_directory = os.getcwd()
    for file_name in os.listdir(current_directory):
        if file_name.endswith(".jpg") or file_name.endswith(".png"):  # 只处理jpg和png文件
            file_path = os.path.join(current_directory, file_name)
            existing_image = Image.select().where(Image.name == file_name).first()
            if existing_image:  # 如果已存在同名图片，则更新内容
                with open(file_path, 'rb') as f:
                    image_bytes = f.read()
                    existing_image.image_data = image_bytes
                    existing_image.save()
            else:  # 否则创建新的图片条目
                with open(file_path, 'rb') as f:
                    image_bytes = f.read()
                    Image.create(name=file_name, image_data=image_bytes)

#测试函数
'''    def NewPerson(self):
        name_list = []
        conn = psycopg2.connect(database='Card', user='postgres', password='potato', host='127.0.0.1', port='5432')
        cur = conn.cursor()
        cur.execute(f"select * from {user_now}_card")
        # 把访问到的所有数据都递给rows
        rows = cur.fetchall()
        print(rows)
        for row in rows:
            name_list.append(row[1])
        print(name_list)
        print(name_list[0])
        name = self.ui.lineEditName.text()
        print("name is "+ name)
        gender = self.ui.lineEditGender.text()
        print("gender is "+ gender)
        number = self.ui.lineEditNumber.text()
        email = self.ui.lineEditEmail.text()
        text = self.ui.lineEditText.text()
        print("text is "+ text)
        for i in range(len(name_list)):
            print(name_list[i])
            print("szq")
            print(i)
            a = 0
            b = 0
            if name == name_list[i-1]:  # 用户名已经存在
                print("该联系人已存在")
                a = a + 1
                self.ui.stackedWidget.setCurrentIndex(2)
            elif len(name) == 0 :
                self.ui.stackedWidget.setCurrentIndex(1)
                b = b + 1
            print(a)
            if a == 0:
                c = len(name_list)+1
                cur.execute(f"insert into {user_now}_card values('{c}','{name}','{gender}','{number}','{email}','{text}')")
                conn.commit()
                conn.close()
                self.close()
'''
if __name__ == "__main__":
    # 查询数据库是否连接
    db.is_closed()
    # 连接数据库
    db.connect()
    #all_event = event.select()
    #all_name = [event.describe for event in all_event]
    #print(all_name)
    # 创建table
    Image.create_table()
    #Person.create_table()
    #p = iduser.create(accounts="bbb",passwords = "123456")
    #p = potato8_card.create(name="张三",gender="女",number="33333333333",email="55324@qq.com")
    #card.create_table()
    '''p = card.get(user='kkk')
    p.name = "kkk"
    p.save()'''

    #测试


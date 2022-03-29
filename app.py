import string

from flask import Flask, render_template, request, flash, redirect, url_for

# 导入wtf扩展的表单类
from flask_wtf import FlaskForm

# 导入自定义表单需要的字段
from wtforms import SubmitField, IntegerField , StringField

# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired


#数据库配置
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a random string'


class adduserForm(FlaskForm):
    username = StringField(label='username:', validators=[DataRequired()])
    password = StringField(label='password:', validators=[DataRequired()])
    sex = StringField(label='sex:', validators=[DataRequired()])
    age = IntegerField(label='age:', validators=[DataRequired()])
    phone = IntegerField(label='phone:', validators=[DataRequired()])
    description = StringField(label='description:', validators=[DataRequired()])
    submit = SubmitField('add')


@app.route('/', methods=['get', 'post'])
def hello_world():  # put application's code here
    connection = pymysql.connect(host='rm-bp151716jpy7k5711zo.mysql.rds.aliyuncs.com', user='root',
                                 password='123456789yY', database='ryxs')
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sex = request.form.get('sex')
        age = request.form.get('age')
        phone = request.form.get('phone')
        description = request.form.get('description')
        if not all([username, password, sex, age, phone, description]):
            flash('params error')
        else:
            sql = "insert into Users VALUES (%s, %s, %s ,%s, %s , %s)"
            cursor.execute(sql, [username, password, sex, age, phone, description])
            connection.commit()
    cursor.execute("select * from Users")
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", result=result, form=adduserForm())


@app.route('/delete_id/<string:id>', methods=['get', 'post'])
def delete_id(id):
    connection = pymysql.connect(host='rm-bp151716jpy7k5711zo.mysql.rds.aliyuncs.com', user='root',
                                 password='123456789yY', database='ryxs')
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "delete from Users2 where username = %s"
    cursor.execute(sql, [id])
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for('hello_world'))


@app.route('/login', methods=['post'])
def testhello2():

    connection = pymysql.connect(host='rm-bp151716jpy7k5711zo.mysql.rds.aliyuncs.com', user='root',
                                 password='123456789yY', database='ryxs')
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
    # 1 成功 2 不存在用户名 3 密码错误
    username = request.form['username']
    password = request.form['password']
    sql = "select username,password from users where username = "+username

    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) == 0:
        return "2"
    elif result[0]['password'] != password:
        return "3"
    else:
        return "1"


@app.route('/user', methods=['post'])
def testhello():
    connection = pymysql.connect(host='rm-bp151716jpy7k5711zo.mysql.rds.aliyuncs.com', user='root',
                                 password='123456789yY', database='ryxs')
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
    # 1 成功 2 不存在用户名 3 密码错误
    username = request.form['username']
    password = request.form['password']
    sql = "select username,password from users where username = "+username

    cursor.execute(sql)
    result = cursor.fetchall()
    print(username+"log")
    if len(result) == 0:
        return "2"
    elif result[0]['password'] != password:
        return "3"
    else:
        return "1"


# 注册
@app.route('/register', methods=[ 'post'])
def register():
    # 1 成功 2 用户已存在
    connection = pymysql.connect(host='rm-bp151716jpy7k5711zo.mysql.rds.aliyuncs.com', user='root',
                                 password='123456789yY', database='ryxs')
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

    username = request.form['username']
    sql = "select username from users where username = " +username
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) != 0:
        return "2"
    username = request.form.get('username')
    password = request.form.get('password')
    sex = request.form.get('sex')
    age = request.form.get('age')
    phone = request.form.get('phone')
    description = request.form.get('description')

    sql = "insert into Users VALUES (%s, %s, %s ,%s, %s , %s, %s)"
    cursor.execute(sql, [username, password, sex, age, phone, description, ""])
    connection.commit()

    cursor.close()
    connection.close()
    return "1"


# 返回其他人坐标
@app.route('/location', methods=['get'])
def location():
    connection = pymysql.connect(host='rm-bp151716jpy7k5711zo.mysql.rds.aliyuncs.com', user='root',
                                 password='123456789yY', database='ryxs')
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from location"
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return str(result)


@app.route('/location/<string:username_1>', methods=['post'])
def location_for(username_1):
    connection = pymysql.connect(host='rm-bp151716jpy7k5711zo.mysql.rds.aliyuncs.com', user='root',
                                 password='123456789yY', database='ryxs')
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
    #
    sql = u"select * from location where usrname = '11'"
    #
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    cursor.close()
    connection.close()
    return str(result)



@app.route('/updatalocation', methods=['post'])
def updatalocation():
    Bluetoothid = request.form.get('Bluetoothid')
    x = request.form.get('x')
    y = request.form.get('y')
    return str(Bluetoothid)+str(x)+str(y)


if __name__ == '__main__':
    app.run()


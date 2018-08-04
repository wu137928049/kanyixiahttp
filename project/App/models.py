from django.db import models

# Create yoauth_userur models here.


# 相同数据
class Main(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=36)
    trackid = models.CharField(max_length=20)
    # 改类名
    class Meta:
        abstract = True


# 轮播图数据模型
class AppHome(Main):
    class Meta:
        db_table = 'axf_wheel'

# 每日比抢数据模型
class Everyday(Main):
    class Meta:
        db_table = 'axf_nav'


# 必买、
class MustBuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


# 商品
class Shop(Main):
    class Meta:
        db_table = 'axf_shop'



# 主页展示的商品模型
class MainShow(Main):
    categoryid = models.CharField(max_length=25,)
    brandname = models.CharField(max_length=25)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=25)
    productid1 = models.CharField(max_length=25)
    longname1 = models.CharField(max_length=25)
    price1 = models.CharField(max_length=25,default=0)
    marketprice1 = models.CharField(max_length=25,default=0)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=25)
    productid2 = models.CharField(max_length=25)
    longname2 = models.CharField(max_length=25)
    price2 = models.CharField(max_length=25,default=0)
    marketprice2 = models.CharField(max_length=25,default=0)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=25)
    productid3 = models.CharField(max_length=25)
    longname3 = models.CharField(max_length=25)
    price3 = models.CharField(max_length=25,default=0)
    marketprice3 = models.CharField(max_length=25,default=0)
    class Meta:
        db_table = 'axf_mainshow'


# 闪送超市展示的模型
class MainMarket(models.Model):
    typeid = models.CharField(max_length=25)
    typename = models.CharField(max_length=25)
    childtypenames = models.CharField(max_length=200)
    typesort = models.CharField(max_length=25)
    class Meta:
        db_table = 'axf_foodtypes'


# 闪送超市中的商品
class Goods(models.Model):
    '''
    产品目录  产品图片 产品名字 产品长名 isxf  产品描述
    详情  价格 市场价格  分类ID   子类编号   子类名字
    交易编号   储藏数量   产品数量
    '''
    productid = models.CharField(max_length=25)
    productimg = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=25)
    isxf = models.BooleanField(default=False)
    pmdesc = models.IntegerField(default=0)
    specifics = models.CharField(max_length=10)
    price = models.FloatField(default=1)
    marketprice = models.FloatField(default=1)
    categoryid = models.IntegerField(default=0)
    childcid = models.IntegerField(default=0)
    childcidname = models.CharField(max_length=25)
    dealerid = models.CharField(max_length=25)
    storenums = models.IntegerField(default=0)
    productnum = models.IntegerField(default=0)
    class Meta:
        db_table = 'axf_goods'


# 用户信息
class User(models.Model):
    '''
    姓名  邮箱  手机号 密码 性别 头像 逻辑删除

    '''
    name = models.CharField(max_length=36,unique=True)
    email = models.CharField(max_length=25,unique=True)
    phone = models.CharField(max_length=18,unique=True)
    pwd = models.CharField(max_length=200)
    gender = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icons',default=None)
    is_delete = models.BooleanField(default=False)
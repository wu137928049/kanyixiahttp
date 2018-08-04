from django.shortcuts import render

from django.http import HttpResponseRedirect,JsonResponse
# Create your views here.
from App.models import AppHome,Everyday,MustBuy,Shop,MainShow,MainMarket
from App.models import Goods,User
from django.urls import reverse
import hashlib
import time

# 主页页面的数据操作
def home(request):
    wheel = AppHome.objects.all()
    nav = Everyday.objects.all()
    mustbuy = MustBuy.objects.all()
    shop = Shop.objects.all()
    shows = MainShow.objects.all()
    data = {
        'wheel':wheel,
        'title': '主页',
        'nav' : nav,
        'mustbuy':mustbuy,
        'shop0':shop[0:1],
        'shop_1':shop[1:3],
        'shop_3':shop[3:7],
        'shop_7':shop[7:11],
        'shows':shows,
    }
    return render(request,'home/home.html',context=data)

def market(request):
    return HttpResponseRedirect(reverse('app:markert', args=('104749','0','0')))

def markert(request,typeid,cid,sort):
    foot = MainMarket.objects.all()

    if cid == '0':
        good = Goods.objects.filter(categoryid=typeid)
    else:
        good = Goods.objects.filter(categoryid=typeid).filter(childcid=cid)
    if sort == '0':
        pass
    elif sort == '1':
        good = good.order_by('productnum')
    elif sort == '2':
        good = good.order_by('-price')
    elif sort == '3':
        good = good.order_by('price')

    # 根据传递的typeid获取数据
    all_type_list = []
    t = MainMarket.objects.filter(typeid=typeid)
    # 如果数据存在获取这条数据
    if t.exists():
        tt = t.first()
        # 获取这条数据的全部分类信息
        chilname = tt.childtypenames
        one = chilname.split('#')
        for two in one:
            three = two.split(':')
            # 把这条数据的全部分类填加到空列表中提供给前段进行展示
            all_type_list.append(three)

    data = {
        'title':'闪送超市',
        'foot':foot,
        'goods':good,
        'all_type_list':all_type_list,
        'typeid':typeid,
        'cid':cid,
    }
    return render(request,'market/market.html',context=data)
def cart(request):
    return render(request,'cart/cart.html')
def mine(request):
    use = request.session.get('username')
    if use:
        u = User.objects.filter(name=use)
        if u:
            user = u.first()
            data = {}
            data['photo'] = '/static/uploads/' + str(user.icon)
            data['name'] = user.name
        return render(request, 'mine/mine.html',context=data)
    else:
        data = {
            'register': '注册',
            'login': '登录',
        }
        print('222222222222')
        return render(request, 'mine/mine.html', context=data)






def register(request):
    method = request.method
    if method == 'GET':
        return render(request,'user/user_register.html')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        gender = request.POST.get('usergendrer')
        icon = request.FILES.get('usericon')
        user = User()
        user.name = username
        user.email = email
        user.phone = phone
        user.pwd = md5(pwd)
        user.gender = gender
        user.icon = icon
        user.save()
        return HttpResponseRedirect(reverse('app:mine'))
    else:
        raise Exception('登录错误')
# md5加密
def md5(pwd):
    sha = hashlib.sha512()
    sha.update(pwd.encode('utf-8'))
    return sha.hexdigest()


# 监听
def monitor(request):
    username = request.GET.get('name')
    data = {
        'stat': '600',
    }
    use = User.objects.filter(name=username)
    if use.exists():
        data['stat'] = '700'
        data['describe'] = '用户名以存在，不可用'
    else:
        data['describe'] = '用户名可用'
    return JsonResponse(data)


# 登录
def longin(request):
    method = request.method
    if method == 'GET':
        return render(request,'user/user_login.html')
    elif method == 'POST':
        username = request.POST.get('uname')
        pwd = request.POST.get('upwd')
        u = User.objects.filter(name=username)
        span = request.POST.get('span')
        if span == '密码错误':
            time.sleep(1)
            return render(request, 'user/user_register.html')
        if u.exists():
            use = u.first()
            if md5(pwd) == use.pwd:
                # 创建session id并保存
                request.session['username'] = username
                data = {}
                data['name'] = use.name
                data['photo'] = '/static/uploads/'+ str(use.icon)
                reg = request.POST.get('reg')
                login = request.POST.get('logi')
                reg = ''
                login = ''
                return render(request,'mine/mine.html',context=data)
            else:
                return render(request, 'user/user_login.html')
        return render(request, 'user/user_login.html')
# 监听密码 判断是否正确
def pwd_login(request):
    data = {
        'stat':'200'
    }
    pd = request.GET.get('p')
    pdd = md5(pd)
    u = User.objects.filter(pwd=pdd)
    print(u)
    if u.exists():
        data['msg'] = 'ok'
    else:
        data['stat'] = '300'
    return JsonResponse(data)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('app:home'))
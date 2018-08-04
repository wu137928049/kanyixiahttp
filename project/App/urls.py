
from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'^home/',views.home,name="home"),
    url(r'^market/$',views.market,name="market"),
    url(r'^market/(\d+)/(\d+)/(\d+)/',views.markert,name="markert"),
    url(r'^cart/',views.cart,name="cart"),
    url(r'^mine/',views.mine,name="mine"),
    url(r'^register/',views.register,name="register"),
    url(r'^monitor/',views.monitor,name="monitor"),
    url(r'^login/',views.longin,name="login"),
    url(r'^pwdlogin/',views.pwd_login,name="pwdlogin"),
    url(r'^logout/',views.logout,name="logout"),
]
from django.urls import path
from .views import MembershipSelectView, PaymentView

app_name='membership'
urlpatterns=[
path('', MembershipSelectView.as_view(), name= 'memberships'),
path('payment/',PaymentView, name='payment')


]

from django.contrib import admin
from .models import Seller, AccountRechargeOrder, SaleOrder, Transaction

admin.site.register(Seller)
admin.site.register(AccountRechargeOrder)
admin.site.register(SaleOrder)
admin.site.register(Transaction)


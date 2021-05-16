from django.contrib import admin
from .models import product, banner,contact,Orders,OrderUpdate


admin.site.register(product)
admin.site.register(banner)
admin.site.register(contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)


from django.contrib import admin

from .models import About,Coupon,Order,OrderItem, Product,Blog,AuthorAbout,Comment,Job,JobApplication,AboutUs,New,ContactU,WholeSale,Customer,Address,Payment

admin.site.register(About)

admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(AuthorAbout)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(AboutUs)
admin.site.register(New)
admin.site.register(ContactU)
admin.site.register(WholeSale)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Coupon)
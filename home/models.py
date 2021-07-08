from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save


CATEGORY_CHOICES = (
	('Solid Neon Colour Adapter','Solid Neon Colour Adapter'),
	('Solid Neon Color Blunt Box','Solid Neon Color Blunt Box'),
	('Day Glow Colour Adapter','Day Glow Colour Adapter'),
	('Day Glow Blunt Colour Box','Day Glow Blunt Colour Box'),
	('Glow-In-The-Dark Adapter','Glow-In-The-Dark Adapter'),
)
LABEL_CHOICES = (
	('D','New'),
	('P','Best Seller'),

	)

JOB_CATEGORY={
	('Creative Designer','Creative Designer'),
	('Engineering','Engineering'),
	('Finance','Finance'),
	('Job1','Job1'),
	('Job2','Job2'),
	('Job3','Job3'),
}
CHOICES = (
	('Solid Neon Adaptor','Solid Neon Adaptor'),
	('Solid Neon Blunt Box','Solid Neon Blunt Box'),
	('Royal Splits Collection','Royal Splits Collection'),
	('Special Order','Special Order'),
)
SHIPPING_CHOICE = (
	('Residential Address','Residential Address'),
	('Commercial Address','Commercial Address')

)




class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    email = models.EmailField(max_length = 254)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    class Meta:
    	verbose_name_plural = 'Address'
    def __str__(self):
    	return self.name
    
    

class AuthorAbout(models.Model):
	name = models.CharField(max_length=225)
	about_author = models.TextField()

	def __str__(self):
		return self.name

class Blog(models.Model):
	title = models.CharField(max_length=225)
	blog_image = models.ImageField(upload_to='images/')
	body = models.TextField()
	pub_date = models.DateTimeField()
	author = models.ForeignKey(AuthorAbout,on_delete=models.CASCADE)


	def __str__(self):
		return self.title

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
	def summary(self):
		return self.body[:100]



class Comment(models.Model):
	blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
	your_name = models.CharField(max_length=20)
	comment_text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)



class About(models.Model):
  
    
    
    description = models.TextField()
  
    # renames the instances of the model
    # with their title name



    



class Job(models.Model):
 	title = models.CharField(choices=JOB_CATEGORY,max_length=225)
 	city = models.CharField(max_length=200)
 	prerequisites = models.CharField(max_length=225)
 	number = models.IntegerField(default=0,null=True,blank=True)
 	def __str__(self):
 		return self.title

class JobApplication(models.Model):
	job_title = models.ForeignKey(Job, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=225)
	email = models.EmailField(max_length = 254)
	reason = models.TextField()
	resume = models.FileField(null=True,blank=True)
	def __str__(self):
		return self.full_name



class AboutUs(models.Model):
	story = models.TextField()
	mission = models.TextField()


class New(models.Model):
	news_title = models.CharField(max_length=225)
	news_image = models.ImageField(upload_to='images/')
	news_desc = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.news_title
	def pub_date_pretty(self):
		return self.date_added.strftime('%b %e %Y')





class ContactU(models.Model):
	name = models.CharField(max_length=225,null=True)
	email = models.EmailField(max_length = 225,null=True)
	phone_no = models.CharField(max_length=13,null=True)
	description = models.TextField(null=True)
	def __str__(self):
		return self.name



class WholeSale(models.Model):
	cname = models.CharField(max_length=225,null=True)
	fname = models.CharField(max_length=225,null=True)
	lname = models.CharField(max_length=225,null=True)
	ctitle = models.CharField(max_length=225,null=True)
	email = models.EmailField(max_length=225,null=True)
	phnumber = models.CharField(max_length=225,null=True)
	fnum = models.CharField(max_length=225,null=True)
	product_choice = models.CharField(max_length=225,choices=CHOICES,null=True)
	quantity = models.CharField(max_length=3,null=True)
	address = models.TextField(null=True)
	city = models.CharField(max_length=225,null=True)
	state = models.CharField(max_length=225,null=True)
	zip_code = models.CharField(max_length=225,null=True)
	country = models.CharField(max_length=225,null=True)
	federal_tax_id = models.CharField(max_length=225,null=True)
	reseller_lisence = models.CharField(max_length=225,null=True)
	inst_id =models.CharField(max_length=225,null=True)
	fb_id = models.CharField(max_length=225,null=True)
	shipping_add_field = models.CharField(max_length=225,choices=SHIPPING_CHOICE,null=True)
	shipping_add = models.TextField(null=True)
	shipping_city = models.CharField(max_length=225,null=True)
	shipping_state = models.CharField(max_length=225,null=True)
	shipping_zip = models.CharField(max_length=225,null=True)
	shipping_country = models.CharField(max_length=225,null=True)
	shipping_person_name = models.CharField(max_length=225,null=True)
	shipping_person_num = models.CharField(max_length=225,null=True)

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	fname = models.CharField(max_length=225,null=True)
	lname =models.CharField(max_length=225,null=True)
	email = models.EmailField(max_length=225,null=True)
	location = models.CharField(max_length=225,null=True)
	website = models.CharField(max_length=225,null=True,blank=True)
	bio = models.TextField(null=True)
	def __str__(self):
		return self.user.username

def create_profile(sender, instance, created, **kwargs):
	if created:
	    Customer.objects.create(user=instance)
post_save.connect(create_profile,sender=User)


# def update_profile(sender, instance, created, **kwargs):
# 	if created == False:
# 		instance.customer.save()
# post_save.connect(update_profile,sender=User)

class Product(models.Model):
	title = models.CharField(max_length=225)
	image1 = models.ImageField(upload_to='images/')
	category = models.CharField(choices=CATEGORY_CHOICES,max_length=40,null=True, blank=True)
	label = models.CharField(choices=LABEL_CHOICES,max_length=1,null=True, blank=True)
	thumbnail_1 = models.ImageField(upload_to='images/')
	thumbnail_2 = models.ImageField(upload_to='images/')
	thumbnail_3 = models.ImageField(upload_to='images/',null=True, blank=True)
	thumbnail_4 = models.ImageField(upload_to='images/',null=True, blank=True)
	thumbnail_5 = models.ImageField(upload_to='images/',null=True, blank=True)
	thumbnail_6 = models.ImageField(upload_to='images/',null=True, blank=True)
	thumbnail_7 = models.ImageField(upload_to='images/',null=True, blank=True)
	price= models.FloatField(default=0.00)
	description = models.TextField(null=True,blank=True)

	def __str__(self):
		return self.title
class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.code

class Order(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
	ordered_date = models.DateTimeField(auto_now_add =True)
	complete = models.BooleanField(default=False,null=True,blank=True)
	transaction_id = models.CharField(max_length=225,null=True,blank=True)
	coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, blank=True, null=True)
	def __str__(self):
		return str(self.id)
	
	def get_sub_total(self):
		total=0
		total = sum([order_item.get_total for order_item in self.orderitem_set.all()])
		return total

	def get_cart_total(self): 
		total=0
		total = sum([order_item.get_total for order_item in self.orderitem_set.all()])
		if self.coupon:
			total -= self.coupon.amount
		return total


class OrderItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
	order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
	quantity = models.IntegerField(default=0,null=True,blank=True)
	color= models.CharField(max_length=225,null=True,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

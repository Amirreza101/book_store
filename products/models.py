from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='نام')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='اسلاگ')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField("عنوان", max_length=200,db_index=True)
    slug = models.SlugField("اسلاگ", max_length=220, unique=True, blank=True,db_index=True)
    author = models.CharField(max_length=50, verbose_name='نویسنده')
    publisher = models.CharField(max_length=20, verbose_name='انتشارات', null=True, blank=True)
    translator = models.CharField(max_length=20, verbose_name='مترجم', null=True, blank=True)
    language = models.CharField(max_length=20, verbose_name='زبان', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='دسته بندی')
    image = models.ImageField("عکس", upload_to="image/books/", blank=True)
    short_description = models.CharField(max_length=20,db_index=True, verbose_name='توضیحات کوتاه')
    body = models.TextField(db_index=True,verbose_name='توضیحات')
    price = models.CharField('قیمت به هزار تومان', max_length=50)
    discount = models.CharField('تخفیف', max_length=50, blank=True, null=True)
    price_after_discount = models.CharField('قیمت بعد از تخفیف', max_length=50, blank=True, null=True)
    rating = models.DecimalField("امتیاز", max_digits=3, decimal_places=1, default=0,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    is_available = models.BooleanField(verbose_name='موجود است/نیست')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title}- {self.language} - ({self.price})"

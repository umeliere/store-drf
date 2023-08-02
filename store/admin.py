from django.contrib import admin
from .models import Product, Producer, Category, Review


class ReviewAdmin(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('discount',)
    inlines = (ReviewAdmin,)

    def save_formset(self, request, obj, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
            formset.save()


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

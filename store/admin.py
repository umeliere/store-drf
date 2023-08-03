from django.contrib import admin
from store.models import Product, Producer, Category, Review
from mptt.admin import MPTTModelAdmin


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


@admin.register(Review)
class ReviewAdmin(MPTTModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user

        super(ReviewAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )

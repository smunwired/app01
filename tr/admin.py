from django.contrib import admin

from .models import Project,Vendor,Branch,Transaction,Reader,Account,Transaction_type,Payment_type

class AccountAdmin(admin.ModelAdmin):
    model = Account
    readonly_fields = ["id",]
    list_display = ["id", "name",]
    pass

admin.site.register(Project)
admin.site.register(Vendor)
admin.site.register(Branch)
admin.site.register(Transaction)
admin.site.register(Reader)
admin.site.register(Account)
admin.site.register(Transaction_type)
admin.site.register(Payment_type)


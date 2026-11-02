from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Vendor, Branch, Transaction, Project, Account, Transaction_type, Transaction_sub_type
from .forms import TransactionForm
from django.views.generic.detail import DetailView
from django.utils import timezone
from datetime import timedelta, date
from django.db.models.functions import Coalesce

class AccountListView(ListView):
    model = Account
    ordering = ['name']

class AccountTransactionListView(ListView):
    fields = "__all__"
    model = Transaction
    template_name = "tr/transaction_list.html"
    ordering = '-statement_date'
    paginate_by = 22

    def get_queryset(self):
        account = self.kwargs["pk"]
        queryset = Transaction.objects.all().annotate(new_date=Coalesce("receipt_date","transaction_date","statement_date",date.today())).filter(account_id=account).order_by('-new_date')
        return queryset

class AccountTransactionYearListView(ListView):
    fields = "__all__"
    model = Transaction
    template_name = "tr/transaction_list.html"
    ordering = '-statement_date'
    paginate_by = 22

    def get_queryset(self):
        account = self.kwargs["pk"]
        year = self.kwargs["year"]
        queryset = Transaction.objects.all().annotate(new_date=Coalesce("receipt_date","transaction_date","statement_date",date.today())).filter(account_id=account,new_date__year=year).order_by('-new_date')
        return queryset

class AccountTotals(ListView):
    fields = "__all__"
    model = Account
    template_name = "tr/account_totals.html"

    def get_queryset(self):
        queryset = Account.objects.raw(" select a.id as id,a.name as name,sum(amount*cr_dr) as amount from tr_account a join tr_transaction t on t.account_id=a.id group by a.id,a.name order by 2")
        return queryset

class AccountTotalsYear(ListView):
    fields = "__all__"
    model = Account
    template_name = "tr/account_totals.html"
    def get_queryset(self):
        self.year = self.kwargs['year']
        queryset = Account.objects.raw('''select a.id as id,a.name as name,sum(amount*cr_dr) as amount from tr_account a join tr_transaction t on t.account_id=a.id where date_part('year',statement_date)=%s group by a.id,a.name order by 2''',[self.year])
        return queryset

class AccountTotalsYearMonth(ListView):
    fields = "__all__"
    model = Account
    template_name = "tr/account_year_month_totals.html"
    def get_queryset(self):
        self.year = self.kwargs['year']
        self.month = self.kwargs['month']
        queryset = Account.objects.raw('''select a.id as id,a.name as name,sum(amount*cr_dr) as amount,
		date_part('year',statement_date)::integer as year,
		date_part('month',statement_date)::integer as month
		from tr_account a join tr_transaction t on t.account_id=a.id 
		where date_part('year',statement_date)=%s and date_part('month',statement_date)=%s 
		group by a.id,a.name,date_part('year',statement_date)::integer,date_part('month',statement_date)::integer
		order by 2''',[self.year,self.month])
        return queryset

class TypeListView(ListView):
    model = Transaction_type
    template_name = "tr/type_list.html"
    ordering = ['name']

class SubTypeListView(ListView):
    model = Transaction_sub_type
    template_name = "tr/sub_type_list.html"
    ordering = ['name']

class TransactionTypeTransactionListView(ListView):
    fields = "__all__"
    model = Transaction_type
    template_name = "tr/transaction_list.html"
    ordering = '-statement_date'
    paginate_by = 22

    def get_queryset(self):
        account = self.kwargs["pk"]
        queryset = Transaction.objects.all().annotate(new_date=Coalesce("receipt_date","transaction_date","statement_date",date.today())).filter(transaction_type_id=account).order_by('-new_date')
        return queryset

class TransactionSubTypeTransactionListView(ListView):
    fields = "__all__"
    model = Transaction_sub_type
    template_name = "tr/transaction_list.html"
    ordering = '-statement_date'
    paginate_by = 22

    def get_queryset(self):
        account = self.kwargs["pk"]
        queryset = Transaction.objects.all().annotate(new_date=Coalesce("receipt_date","transaction_date","statement_date",date.today())).filter(transaction_sub_type_id=account).order_by('-new_date')
        return queryset

class TransactionTypeTotalsYear(ListView):
    fields = "__all__"
    model = Transaction_type
    template_name = "tr/type_totals.html"
    def get_queryset(self):
        self.year = self.kwargs['year']
        queryset = Transaction_type.objects.raw('''select a.id as id,a.name as name,sum(amount*cr_dr) as amount from tr_transaction_type a join tr_transaction t on t.transaction_type_id=a.id where date_part('year',statement_date)=%s group by a.id,a.name order by 2''',[self.year])
        return queryset

class TransactionTypeTotalsYearMonth(ListView):
    fields = "__all__"
    model = Transaction_type
    template_name = "tr/type_year_month_totals.html"
    def get_queryset(self):
        self.year = self.kwargs['year']
        self.month = self.kwargs['month']
        queryset = Account.objects.raw('''select a.id as id,a.name as name,sum(amount*cr_dr) as amount,
		date_part('year',statement_date)::integer as year,
		date_part('month',statement_date)::integer as month
		from tr_transaction_type a join tr_transaction t on t.account_id=a.id 
		where date_part('year',statement_date)=%s and date_part('month',statement_date)=%s 
		group by a.id,a.name,date_part('year',statement_date)::integer,date_part('month',statement_date)::integer
		order by 2''',[self.year,self.month])
        return queryset

class TransactionTypeTotals(ListView):
    fields = "__all__"
    model = Transaction_type
    template_name = "tr/type_totals.html"

    def get_queryset(self):
        queryset = Transaction_type.objects.raw(" select a.id as id,a.name as name,sum(amount*cr_dr) as amount from tr_transaction_type a join tr_transaction t on t.transaction_type_id=a.id group by a.id,a.name order by 2")
        return queryset

class TransactionTypeAddView(CreateView):
    model = Transaction_type
    success_url = reverse_lazy('tr:type_list')
    fields = "__all__"
    template_name = "tr/type_form.html"

class TransactionSubTypeAddView(CreateView):
    model = Transaction_sub_type
    success_url = reverse_lazy('tr:sub_type_list')
    fields = "__all__"
    template_name = "tr/sub_type_form.html"

class TransactionTypeDetailView(DetailView):
    model = Transaction_type
    template_name = "tr/account_detail.html"

class TransactionTypeUpdateView(UpdateView):
    model = Transaction_type
    fields = "__all__"

class TransactionTypeDeleteView(DeleteView):
    model = Transaction_type
    success_url = reverse_lazy('tr:type_list')

class TransactionSubTypeUpdateView(UpdateView):
    model = Transaction_sub_type
    fields = "__all__"
    success_url = reverse_lazy('tr:sub_type_list')

class TransactionSubTypeDeleteView(DeleteView):
    model = Transaction_sub_type
    success_url = reverse_lazy('tr:sub_type_list')

class VendorListView(ListView):
    fields = "__all__"
    model = Vendor
    ordering = 'name'
    paginate_by = 22

class VendorListUnattachedView(ListView):
    fields = "__all__"
    queryset = Vendor.objects.raw("select * from tr_vendor where id in (select id from tr_vendor except select vendor_id from tr_transaction)");

class VendorListStartswithView(ListView):
    fields = "__all__"
    model = Vendor
    ordering = 'name'
    paginate_by = 22

    def get_queryset(self):
      self.startswith = self.kwargs['startswith']
      return Vendor.objects.filter(name__startswith=(self.startswith))

class VendorDetailView(DetailView):
    model = Vendor

class VendorBranchDetailView(DetailView):
    model = Branch

class VendorAddView(CreateView):
    fields = "__all__"
    model = Vendor
    success_url = reverse_lazy('tr:vendor_list')

class VendorUpdateView(UpdateView):
    fields = "__all__"
    model = Vendor
    success_url = reverse_lazy('tr:vendor_list')

class VendorDeleteView(DeleteView):
    model = Vendor
    success_url = reverse_lazy('tr:vendor_list')

class BranchUpdateView(UpdateView):
    fields = "__all__"
    model = Branch
    success_url = "/tr/recent/"

class BranchAddView(CreateView):
    fields = "__all__"
    model = Branch
    success_url = "tr/vendors"

class ReceiptAddView(CreateView):
    model = Transaction
    fields = "__all__"
    template_name = "recent/receipt_form.html"
    success_url = "/recent/recent"

class MonthListViewNew(ListView):
    fields = "__all__"
    model = Transaction

#class MonthListView(ListView):
#    fields = "__all__"
#    model = Transaction
##   This format only works first time
##    queryset = Transaction.objects.filter(statement_date__year=self.year ,statement_date__month=self.month)
#    template_name = "tr/transaction_list.html"
#    ordering = '-statement_date'
#    paginate_by = 22
#
#    def get_queryset(self):
#
#        self.year = self.kwargs['year']
#        self.month = self.kwargs['month']
#        #queryset = super(Yearly, self).get_queryset()
#        #queryset = Transaction.objects.filter(oldest_date__year=self.year,oldest_date__month=self.month).order_by('oldest_date')
#        #queryset = Transaction.objects.filter(statement_date__year=self.year,statement_date__month=self.month).order_by('statement_date')
#        #queryset = Transaction.objects.filter(receipt_date__year=self.year,receipt_date__month=self.month).order_by('receipt_date')
#        #queryset = Transaction.objects.all().annotate(new_date=Coalesce("transaction_date",date.today())).filter(new_date__year=self.year,new_date__month=self.month).order_by('new_date')
#        queryset = Transaction.objects.filter(statement_date__year=self.year,statement_date__month=self.month).exclude(statement_date__isnull=True).exclude(statement_date__exact='').order_by('statement_date')
#        #queryset = Transaction.objects.all().filter(newest_date__year=self.year,newest_date__month=self.month).order_by('newest_date')
#        return queryset

class AmountListView(ListView):
    fields = "__all__"
    model = Transaction
    template_name = "tr/transaction_list.html"
    ordering = '-statement_date'
    paginate_by = 22

    def get_queryset(self):
        self.amount = self.kwargs['amount']
        queryset = Transaction.objects.all().annotate(new_date=Coalesce("receipt_date","transaction_date","statement_date",date.today())).filter(amount=float(self.amount)).order_by('-new_date')
        return queryset

class MonthListView(ListView):
    fields = "__all__"
    model = Transaction
#   I thought this stuff below was excessive but this simple queryset immediately below was not enough
#    queryset = Transaction.objects.filter(statement_date__year=self.year ,statement_date__month=self.month)
    template_name = "tr/transaction_list.html"
    ordering = '-statement_date'
    paginate_by = 22

    def get_queryset(self):
        self.year = self.kwargs['year']
        self.month = self.kwargs['month']
        #queryset = super(Yearly, self).get_queryset()
        #queryset = Transaction.objects.filter(oldest_date__year=self.year,oldest_date__month=self.month).order_by('oldest_date')
        #queryset = Transaction.objects.filter(statement_date__year=self.year,statement_date__month=self.month).order_by('statement_date')
        #queryset = Transaction.objects.filter(receipt_date__year=self.year,receipt_date__month=self.month).order_by('receipt_date')
        #queryset = Transaction.objects.all().annotate(new_date=Coalesce("statement_date","transaction_date","receipt_date",date.today())).filter(account=self.account_id).filter(new_date__year=self.year,new_date__month=self.month).order_by('new_date')
        queryset = Transaction.objects.filter(statement_date__year=self.year,statement_date__month=self.month).order_by('statement_date')
        return queryset

class Dateless(ListView):
    fields = "__all__"
    model = Transaction
    def get_queryset(self):
        queryset = Transaction.objects.filter(statement_date__isnull=True,transaction_date__isnull=True,receipt_date__isnull=True)
        return queryset

class MonthAccountListView(ListView):
    fields = "__all__"
    model = Transaction
#   I thought this stuff below was excessive but this simple queryset immediately below was not enough
#    queryset = Transaction.objects.filter(statement_date__year=self.year ,statement_date__month=self.month)
    template_name = "tr/transaction_list.html"
    ordering = '-statement_date'
    paginate_by = 22

    def get_queryset(self):
        self.year = self.kwargs['year']
        self.month = self.kwargs['month']
        self.account_id = self.kwargs['account_id']
        #queryset = super(Yearly, self).get_queryset()
        #queryset = Transaction.objects.filter(oldest_date__year=self.year,oldest_date__month=self.month).order_by('oldest_date')
        #queryset = Transaction.objects.filter(statement_date__year=self.year,statement_date__month=self.month).order_by('statement_date')
        #queryset = Transaction.objects.filter(receipt_date__year=self.year,receipt_date__month=self.month).order_by('receipt_date')
        #queryset = Transaction.objects.all().annotate(new_date=Coalesce("statement_date","transaction_date","receipt_date",date.today())).filter(account=self.account_id).filter(new_date__year=self.year,new_date__month=self.month).order_by('new_date')
        queryset = Transaction.objects.annotate(best_date=Coalesce('statement_date','transaction_date','receipt_date')).filter(best_date__year=self.year,best_date__month=self.month,account_id=self.account_id).order_by('best_date')
        return queryset

class RecentListView(ListView):
    fields = "__all__"
    model = Transaction
    #queryset = Transaction.objects.filter(statement_date__year=2024, statement_date__month=9)
    template_name = "tr/transaction_list.html"
    ordering = ['-date_amended','-date_created']
    paginate_by = 22
    def get_queryset(self):
        thirty_days_ago = timezone.now() - timedelta(days=30)
        return Transaction.objects.filter(date_created__gte=thirty_days_ago)

class NoVendorListView(ListView):
    fields = "__all__"
    model = Transaction
    queryset = Transaction.objects.filter(vendor_id__isnull=True)
    template_name = "tr/transaction_list.html"
    ordering = ['-date_amended','-date_created']
    paginate_by = 22

class TransactionListView(ListView):
    model = Transaction
    context_object_name = 'transaction'
    ordering = ['-date_created']

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('tr:recent_list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('tr:recent_list')
    def form_valid(self, form):
        if 'addlike' in self.request.POST:
            self.object.pk = None
            self.object.date_amended = None
            self.object.user_amended = None
            self.object.user_created = 'addlike'
# this was saving it twice, postgresql update trigger was firing on second save(seemingly)
#            self.object = form.save()
        return super().form_valid(form)
#this updates the existing row and creates a new one
#    def get_success_url(self):
#        if 'addlike' in self.request.POST:
#            self.object.pk = None
#    #        self.object.save()
#        url = reverse_lazy('tr:recent_list')
#        return url


class BranchDeleteView(DeleteView):
    model = Branch
    success_url = reverse_lazy('tr:recent_list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    success_url = reverse_lazy('tr:recent_list')

def load_branches(request):
    vendor_id = request.GET.get('vendor')
    branches = Branch.objects.filter(vendor_id=vendor_id).order_by('name')
    return render(request, 'tr/branch_dropdown_list_options.html', {'branches': branches})

class AccountAddView(CreateView):
	model = Account
	fields = "__all__"
class AccountUpdateView(UpdateView):
	model = Account
	fields = "__all__"
class AccountDeleteView(DeleteView):
	model = Account
class AccountDetailView(DetailView):
	model = Account
	template_name = "tr/account_detail.html"

class TransactionAccountYearMonthListView(ListView):
    model=Transaction
    fields = "__all__"
    template_name = "tr/transaction_month_list.html"
    ordering = '-statement_date'
    paginate_by = 22
    def get_queryset(self):
        self.year = self.kwargs['year']
        self.month = self.kwargs['month']
        self.account_id = self.kwargs['pk']
        #self.date = Coalesce(self.statement_date,self.receipt_date)
        self.date = Coalesce('statement_date','receipt_date')
        queryset = Transaction.objects.filter(statement_date__year=self.year,statement_date__month=self.month,account_id=self.account_id).order_by('statement_date')
        #queryset = Transaction.objects.filter(self.date__year==self.year,self.date__month==self.month,account_id==self.account_id).order_by('self.date')
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account"] = self.kwargs['pk']
        this_account_name = Account.objects.filter(pk=self.kwargs['pk'])
        context["account_name"] = this_account_name
        context["thismonth"] = self.kwargs['month']
        context["thisyear"] = self.kwargs['year']
        if self.kwargs['month'] == 1:
          context["lastmonth"] = 12
          context["lastyear"] = self.kwargs['year']-1
          context["nextmonth"] = self.kwargs['month']+1
          context["nextyear"] = self.kwargs['year']
        elif self.kwargs['month'] == 12:
          context["lastmonth"] = self.kwargs['month']-1
          context["lastyear"] = self.kwargs['year']
          context["nextmonth"] = 1
          context["nextyear"] = self.kwargs['year']+1
        else:
          context["lastmonth"] = self.kwargs['month']-1
          context["lastyear"] = self.kwargs['year']
          context["nextmonth"] = self.kwargs['month']+1
          context["nextyear"] = self.kwargs['year']
        return context
        

class TransactionTypeYearMonthListView(ListView):
    model=Transaction
    fields = "__all__"
    template_name = "tr/transaction_month_list.html"
    ordering = '-statement_date'
    paginate_by = 22
    def get_queryset(self):
        self.year = self.kwargs['year']
        self.month = self.kwargs['month']
        self.account_id = self.kwargs['pk']
        #self.date = Coalesce(self.statement_date,self.receipt_date)
        self.date = Coalesce('statement_date','receipt_date')
        queryset = Transaction.objects.filter(statement_date__year=self.year,statement_date__month=self.month,transaction_type_id=self.transaction_type_id).order_by('statement_date')
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = self.kwargs['pk']
        this_type_name = Transaction_type.objects.filter(pk=self.kwargs['pk'])
        context["type_name"] = this_type_name
        context["thismonth"] = self.kwargs['month']
        context["thisyear"] = self.kwargs['year']
        if self.kwargs['month'] == 1:
          context["lastmonth"] = 12
          context["lastyear"] = self.kwargs['year']-1
          context["nextmonth"] = self.kwargs['month']+1
          context["nextyear"] = self.kwargs['year']
        elif self.kwargs['month'] == 12:
          context["lastmonth"] = self.kwargs['month']-1
          context["lastyear"] = self.kwargs['year']
          context["nextmonth"] = 1
          context["nextyear"] = self.kwargs['year']+1
        else:
          context["lastmonth"] = self.kwargs['month']-1
          context["lastyear"] = self.kwargs['year']
          context["nextmonth"] = self.kwargs['month']+1
          context["nextyear"] = self.kwargs['year']
        return context
        

class AccountYearListView(ListView):
    fields = "__all__"
    model = Account
    template_name = "tr/account_totals.html"
#    def get_queryset(self):
#        self.year = self.kwargs['year']
##        queryset = Account.objects.raw("select a.id as id,a.name as name,sum(amount*cr_dr) as amount from tr_account a join tr_transaction t on t.account_id=a.id where date_part('year',statement_date)='2026' and date_part('month',statement_date)='01' group by a.id,a.name order by 2")
#        queryset = Account.objects.raw("select a.id as id,a.name as name,sum(amount*cr_dr) as amount from tr_account a join tr_transaction t on t.account_id=a.id where date_part('year',statement_date)=%s group by a.id,a.name order by 2",[year])
#        return queryset

#.filter(new_date__year=self.year,new_date__month=self.month).order_by('new_date')
class ProjectListView(ListView):
	model = Project
	ordering = ['name']
class ProjectAddView(CreateView):
	model = Project
	fields = "__all__"
class ProjectUpdateView(UpdateView):
	model = Project
	fields = "__all__"
class ProjectDeleteView(DeleteView):
	model = Project
class ProjectDetailView(DetailView):
	model = Project

from django import forms
from .models import Transaction, Branch

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
#        fields = ('name', 'birthdate', 'vendor', 'branch')
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'vendor' in self.data:
            try:
                vendor_id = int(self.data.get('vendor'))
                self.fields['branch'].queryset = Branch.objects.filter(vendor_id=vendor_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.vendor.branch_set.order_by('name')
        else:
          pass
        #form.fields['account'].initial = 3
        self.account = 3

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        def __init__(self, *args, **kwargs):
            super(BranchForm, self).__init__(*args, **kwargs)
            vendor = self.kwargs['vendor']
            self.initial['vendor_id'] = vendor

from django import forms

class EmployeeUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload Employee CSV')

    def clean_csv_file(self):
        file = self.cleaned_data['csv_file']
        if not file.name.endswith('.csv'):
            raise forms.ValidationError('Only CSV files are allowed')
        return file

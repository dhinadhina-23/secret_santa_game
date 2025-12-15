from django.shortcuts import render, redirect
from django.conf import settings
import os

from .forms import EmployeeUploadForm
from .services.secret_santa_service import SecretSantaManager
from .services.previous_year_assignment import PreviousYearAssignmentReader


def upload_employees(request):
    if request.method == 'POST':
        form = EmployeeUploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']

            # Save uploaded file
            csv_file_path = os.path.join(settings.MEDIA_ROOT, csv_file.name)
            with open(csv_file_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            # Load previous year assignments
            previous_csv = os.path.join(settings.MEDIA_ROOT, 'previous_year.csv')
            previous_pairs = {}

            if os.path.exists(previous_csv):
                reader = PreviousYearAssignmentReader(previous_csv)
                previous_pairs = reader.get_previous_pairs()

            # Generate Secret Santa
            manager = SecretSantaManager(
                csv_file_path=csv_file_path,
                previous_pairs=previous_pairs
            )
            manager.load_employees()
            manager.generate_assignments()
            output_file = manager.export_to_csv()

            # ✅ Store output file path in session
            request.session['output_file'] = output_file

            # ✅ Redirect (POST → GET)
            return redirect('result')

    else:
        form = EmployeeUploadForm()

    return render(request, 'santa_app/upload.html', {'form': form})


def result_view(request):
    output_file = request.session.get('output_file')
    return render(request, 'santa_app/result.html', {'output_file': output_file})

from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report


def upload_report(request):

    if request.method == 'POST':

        form = ReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('/dashboard')

    else:

        form = ReportForm()

    return render(
        request,
        'reports/upload_report.html',
        {'form': form}
    )
# Create your views here.
def doctor_reports(request):
    reports = Report.objects.all()
    
    return render(
        request,
        'reports/doctor_reports.html',
        {'reports': reports}
    )

from django.shortcuts import render, redirect
from .forms import IssueForm
from .models import Issue


# 🔹 Report Issue View
def report_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save()

            # Debug (optional)
            print("Saved Issue:", issue.id, issue.issue_type, issue.description)

            return redirect('success', issue_id=issue.id)
        else:
            print("Form Errors:", form.errors)
    else:
        form = IssueForm()

    return render(request, 'issues/report.html', {'form': form})


# 🔹 Success Page (shows submitted issue)
def success(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    return render(request, 'issues/success.html', {'issue': issue})


# 🔹 Dashboard / Track Issues Page
def my_reports(request):
    issues = Issue.objects.all().order_by('-created_at')  # newest first
    return render(request, 'issues/my_reports.html', {'issues': issues})
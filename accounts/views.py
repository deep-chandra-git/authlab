from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm

def home(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    return redirect("account_login")

@login_required
def dashboard(request):

    return render(
        request,
        "dashboard.html"
    )


@login_required
def profile(request):

    profile = request.user.profile

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():
            form.save()

            messages.success(request, "Profile updated successfully!")

            return redirect("profile")
    else:

        form = ProfileForm(instance=profile)

    return render(request, "profile.html",
        {
            "form": form
        }
    )
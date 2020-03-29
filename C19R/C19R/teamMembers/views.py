from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, RedirectView, UpdateView, DetailView, DeleteView
from django.contrib.messages.views import messages
from django.contrib.auth.decorators import login_required

from .models import Business, StoreInfo


def teamHome(request):
    return render(request, 'teamMembers/teamHome.html', {"title": "Team-Members-Home"})


@login_required
def viewBusinesses(request):
    context = {
        "businesses": Business.objects.order_by('name')
    }

    return render(request, 'teamMembers/business_view.html', context)


class BusinessDetailView(DetailView, LoginRequiredMixin):
    model = StoreInfo
    template_name = "teamMembers/businessDetailView.html"


class BusinessUpdateView(UpdateView, LoginRequiredMixin):
    model = Business

    fields = ["name", "status", "businessType"]

    def form_valid(self, form):
        messages.success(self.request, f'Business has been updated')  # Awaiting admin approval for publishing
        return super().form_valid(form)


class BusinessDeleteView(DeleteView, LoginRequiredMixin):
    model = Business
    success_url = '/teamMembers/view_businesses'
    template_name = 'teamMembers/business_confirm_delete.html'



class AddBusiness(CreateView, LoginRequiredMixin, RedirectView):
    model = Business
    fields = ["name", "status", "businessType"]

    def form_valid(self, form):
        messages.success(self.request, f'Business has been created')  # Awaiting admin approval for publishing
        return super().form_valid(form)

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


class AddStoreInfo(UpdateView, LoginRequiredMixin):
    # UI form to add a new business to the main app
    # any team member can add a new business
    # only admins can add a new "type" of business
    # ToDo: Use a form w/ widget to change how open and closing times are inputted

    model = StoreInfo
    fields = ['phoneNumber', 'website', 'timeOpen', 'timeClose', 'ordering', 'inStorePickUp', 'deliveryOption', 'specialNotes', 'ownerMessage']

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        messages.success(self.request, f'Store info has been updated')  # Awaiting admin approval for publishing
        return super().form_valid(form)

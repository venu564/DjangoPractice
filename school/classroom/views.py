from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm
from classroom.models import Teachers

# Create your views here.
def welcome_view(request):
    return render(request,'classroom/home.html')

class WelcomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankYouView(TemplateView):
    template_name = "classroom/thankyou.html"

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    success_url = "/classroom/thank_you"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class TeacherCreateView(CreateView):
    model = Teachers
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")

class TeacherListView(ListView):
    model = Teachers
    queryset = Teachers.objects.order_by('last_name')
    context_object_name = "teachers_list"

class TeacherDetailView(DetailView):
    model = Teachers

class TeacherUpdateView(UpdateView):
    model = Teachers
    fields = "__all__"
    success_url = reverse_lazy("classroom:list")

class TeacherDeleteView(DeleteView):
    model = Teachers
    success_url = reverse_lazy("classroom:list")
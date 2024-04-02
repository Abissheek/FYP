import requests
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import ContactForm
from .models import Contact
from django.contrib import messages


class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "pages/contact.html"
    success_url = '/'
    # success_message = "Your message was sent successfully"
    # error_message = "Please verify Captcha...!"

    def form_valid(self, form):
        # Validate reCAPTCHA
        recaptcha_response = self.request.POST.get("g-recaptcha-response")
        data = {
            "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            "response": recaptcha_response
        }
        response = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
        result = response.json()
        if result["success"]:
            # CAPTCHA verification successful, proceed with form processing
            # Add success message
            messages.success(self.request, "Message send sucessfully.")
            # return HttpResponse("Success!")
            return super().form_valid(form)
        else:
            messages.error(self.request, "error!!")
            # return HttpResponse("Success!")
            return self.form_invalid(form)



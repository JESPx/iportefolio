from django.shortcuts import render

# Create your views here.
from django.views import View

from myCV.models import Profile, Skills, Education, Category

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        # Obtenez le profil avec l'ID 1 (vous pouvez également utiliser une autre logique pour obtenir le profil souhaité)
        profile = Profile.objects.get(id=1)
        
        # Calculez l'âge en utilisant la méthode calculate_age sur l'instance de Profile
        age = profile.calculate_age()

        #status marital
        marital_status = profile.marital_status

        # Construisez le contexte avec l'âge calculé
        context = {
            "profile": profile,
            "age": age,
            "marital_status": marital_status,
            "skills": Skills.objects.all().order_by('-pourcentage'),
            "educations": Education.objects.all(),
            "categories": Category.objects.all(),
        }

        return render(request, self.template_name, context)

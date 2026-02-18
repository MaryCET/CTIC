
# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def trial(request):
    return render(request, 'home/trial.html')

def president(request):
    return render(request, 'about/president.html')

def clientlist(request):
    return render(request, 'about/client-list.html')
def services(request):
    return render(request, 'about/services.html')
def aboutfitout(request):
    return render(request, 'fitout/about-fitout.html')
def fitoutphotos(request):
    return render(request, 'fitout/fitout-photos.html')
def fitout_misc(request):
    return render(request, 'fitout/fitout-misc.html')
def project_photos(request, year=2026):
    # If no year is provided in URL, it defaults to 2026
    context = {
        'selected_year': year,
    }
    return render(request, 'project_photos/project-photos/project-photos.html', context)

def project_list(request, year=None):
    context = {
        'selected_year': year,
    }
    return render(request, 'about/project-list.html', context)


def projects_2026(request):
    return render(request, 'about/proj_years/2026_list.html')

def projects_2025(request):
    return render(request, 'about/proj_years/2025_list.html')

def projects_2024(request):
    return render(request, 'about/proj_years/2024_list.html')

def projects_2023(request):
    return render(request, 'about/proj_years/2023_list.html')

def projects_2022(request):
    return render(request, 'about/proj_years/2022_list.html')

def projects_2021(request):
    return render(request, 'about/proj_years/2021_list.html')

def projects_2020(request):
    return render(request, 'about/proj_years/2020_list.html')

def projects_2019(request):
    return render(request, 'about/proj_years/2019_list.html')

def projects_2018(request):
    return render(request, 'about/proj_years/2018_list.html')

def projects_2017(request):
    return render(request, 'about/proj_years/2017_list.html')

def projects_2016(request):
    return render(request, 'about/proj_years/2016_list.html')

def unlisted_list(request):
    return render(request, 'about/proj_years/unlisted_list.html')

def electrical_design(request):
    return render(request,'project_photos/electrical-design.html')

def electrical_dist(request):
    return render(request,'project_photos/electrical-distribution.html')

def preventive_maintenance(request):
    return render(request,'project_photos/preventive-maintenance.html')

def gen_construction(request):
    return render(request,'project_photos/gen-construction.html')

def water_refill(request):
    return render(request,'project_photos/water-refill.html')

def renewable_energy(request):
    return render(request,'renewable-energy/renewable-energy.html')

def solar_energy(request):
    return render(request,'renewable-energy/solar-energy.html')
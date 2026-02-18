from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trial', views.trial, name='trial'),
    path('projects-2026', views.trial, name='projects-2026'),
    path('about/president', views.president, name='president'),
    path('about/project-list', views.project_list, name='project_list'),
    path('about/client-list', views.clientlist, name='clientlist'),
    path('about-fit-out/', views.aboutfitout, name='aboutfitout'),
    path('fitout/fitout-photos', views.fitoutphotos, name='fitoutphotos'),
    path('fitout/fitout-misc', views.fitout_misc, name='fitout_misc'),
     path('about/services-and-specializations', views.services, name='services'),
# Project List (The bulleted text list)
    path('about/project-list/', views.project_list, name='project_list'),
    path('about/project-list/<int:year>/', views.project_list, name='project_list_by_year'),
    path('about/project-list/unlisted', views.unlisted_list, name='unlisted_list'),

    # Featured Projects (The Photo Gallery)
    path('featured-projects/', views.project_photos, name='project_photos'),
    path('featured-projects/<int:year>/', views.project_photos, name='projects_by_year'),

    path('electrical-design/', views.electrical_design, name='electrical_design'),
    path('electrical-distribution/', views.electrical_dist, name='electrical_dist'),
    path('preventive-maintenance/', views.preventive_maintenance, name='preventive_maintenance'),
    path('gen-construction/', views.gen_construction, name='gen_construction'),
    path('water-refill/', views.water_refill, name='water_refill'),
    path('renewable-energy/', views.renewable_energy, name='renewable_energy'),
    path('solar-energy/', views.solar_energy, name='solar_energy'),


]
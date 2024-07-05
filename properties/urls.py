from django.urls import path

from .views import (AvailableUnitsView, LeasedPropertyListView,
                    PropertyCreateView, PropertyDeleteView, PropertyDetailView,
                    PropertyListView, PropertyUpdateView, UnitCreateView,
                    UnitDeleteView, UnitDetailView, UnitListView,
                    UnitUpdateView, load_cities, load_states,
                    load_sub_localities)

urlpatterns = [
    path('', PropertyListView.as_view(), name='property_list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('create/', PropertyCreateView.as_view(), name='property_create'),
    path('<int:pk>/update/', PropertyUpdateView.as_view(), name='property_update'),
    path('<int:pk>/delete/', PropertyDeleteView.as_view(), name='property_delete'),
    path('leased/', LeasedPropertyListView.as_view(), name='leased_property_list'),
    path('<int:property_pk>/unit/create/', UnitCreateView.as_view(), name='unit_create'),
    path('unit/<int:pk>/update/', UnitUpdateView.as_view(), name='unit_update'),
    path('unit/<int:pk>/delete/', UnitDeleteView.as_view(), name='unit_delete'),
    path('unit/<int:pk>/', UnitDetailView.as_view(), name='unit_detail'),
    path('units/', UnitListView.as_view(), name='unit_list'),
    path('available-units/', AvailableUnitsView.as_view(), name='available_units'),
    path('ajax/load-states/', load_states, name='ajax_load_states'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
    path('ajax/load-sub-localities/', load_sub_localities, name='ajax_load_sub_localities'),
]

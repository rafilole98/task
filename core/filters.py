import django_filters
from django import forms
from .models import Person,Job,PersonJobDetail
from django.db.models import Q


class PersonFilter(django_filters.FilterSet):


    search = django_filters.CharFilter(field_name='search',label='search',method='filter_by_all_name_fields')
    
    def filter_by_all_name_fields(self, queryset, name, value):
        search_terms = value.split()
        queries = Q()

        for term in search_terms:
            queries |= Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(address__icontains=term) | Q(mobile__icontains=term)

        return queryset.filter(queries)



    class Meta:
        model = Person
        fields = ['search']  



class JobFilter(django_filters.FilterSet):


    search = django_filters.CharFilter(field_name='search',label='search',method='filter_by_all_name_fields')
    
    def filter_by_all_name_fields(self, queryset, name, value):
        search_terms = value.split()
        queries = Q()

        for term in search_terms:
            queries |= Q(title_ar__icontains=term) | Q(title_en__icontains=term) 

        return queryset.filter(queries)



    class Meta:
        model = Job
        fields = ['search']  



class JobDetailFilter(django_filters.FilterSet):


    search = django_filters.CharFilter(field_name='search',label='search',method='filter_by_all_name_fields')
    
    def filter_by_all_name_fields(self, queryset, name, value):
        search_terms = value.split()
        queries = Q()

        for term in search_terms:
            queries |= Q( person__first_name__icontains=term) | Q(person__last_name__icontains=term) | Q(job__title_en__icontains=term) 

            
 
   
 

        return queryset.filter(queries)



    class Meta:
        model = PersonJobDetail
        fields = ['search'] 
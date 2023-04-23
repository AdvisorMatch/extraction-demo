import django_filters

from .models import Work, Advisor


class WorkFilter(django_filters.FilterSet):
    advisor = django_filters.ModelChoiceFilter(queryset=Advisor.objects.all())
    class Meta:
        model = Work
        fields = ['year', 'work_type']


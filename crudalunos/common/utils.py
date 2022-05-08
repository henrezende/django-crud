import operator
from django.db.models import Q
from functools import reduce


def create_student_filter(request):
    query_list = Q()
    search_condition = ""
    reserved_keys = ['limit', 'offset']
    for key in request.GET:
        if key in reserved_keys:
            continue

        valuelist = request.GET.getlist(key)
        search_condition = reduce(
            operator.or_, (
                Q(**{key: value}) for values in valuelist for value in values.split(',')
            )
        )
        query_list.add(search_condition, Q.AND)

    return query_list

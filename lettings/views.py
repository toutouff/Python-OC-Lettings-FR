from django.shortcuts import render

from .models import Letting


def index(request):
    """Index view
    :param request: HTTP request
    :type request: HttpRequest
    :return: HTTP response
    :rtype: HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Letting view
    :param request: HTTP request
    :type request: HttpRequest
    :param letting_id: letting id
    :type letting_id: int
    :return: HTTP response
    :rtype: HttpResponse

    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        return render(request, 'lettings/letting.html',
                      {'error': 'Error : Letting not found'}, status=404)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

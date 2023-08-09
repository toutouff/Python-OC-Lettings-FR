from django.shortcuts import render


def index(request):
    """View function for home page of site.
    :param request: request
    :type request: HttpRequest
    :return: Render of the index.html template
    :rtype: HttpResponse

    """
    return render(request, 'index.html')


def error_404(request, exception):
    """View function for error 404 page of site.
    :param request: request
    :type request: HttpRequest
    :param exception: exception
    :type exception: Exception
    :return: Render of the error_404.html template
    :rtype: HttpResponse"""
    data = {}
    return render(request, 'error_404.html', data)


def error_500(request):
    """View function for error 500 page of site.
    :param request: request
    :type request: HttpRequest
    :return: Render of the error_500.html template
    :rtype: HttpResponse""
    """
    data = {}
    return render(request, 'error_500.html', data)

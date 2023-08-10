from django.shortcuts import render

from .models import Profile


def index(request):
    """
    Index view
    :param request: HTTP request
    :type request: HttpRequest
    :return: HTTP response
    :rtype: HttpResponse
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Profile view
    @param request: HTTP request
    @type request: HttpRequest
    @param username: username
    @type username: str
    @return: HTTP response
    @rtype: HttpResponse
    """

    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        return render(request, 'profiles/profile.html',
                      {'error': 'Error : Profile not found'}, status=404)

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

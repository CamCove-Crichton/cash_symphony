from django.shortcuts import render

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, 'errors/404.html', status=404)

def handler418(request, *args, **kwargs):
    """ Error Handler 418 - I'm a Teapot """
    return render(request, 'errors/418.html', status=418)

def handler505(request, *args, **kwargs):
    """ Error Handler 505 - HTTP Version Not Supported """
    return render(request, 'errors/505.html', status=505)
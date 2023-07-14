from django.shortcuts import render
from django.http import JsonResponse
from .CAPTCHA import createCaptcha, checkCaptcha

def index(request):
    return render(request, "index.html")

def captcha(request, params = None):
    if request.method == "POST":
        if not params:
            cpt = createCaptcha()
            return JsonResponse({"token":cpt[0], "image":cpt[1]})
        else:
            try:
                token, value = params.split(",")
                response = checkCaptcha(token, value)
            except: return JsonResponse({"response": False})
    else: return JsonResponse({"response": False})
    
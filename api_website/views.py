from django.shortcuts import render
from django.http import HttpResponse

def simple_test(request):
    """Simple test view for App Runner deployment testing"""
    return render(request, 'simple_home.html')

def health_check(request):
    """Health check endpoint for App Runner"""
    return HttpResponse("OK", content_type="text/plain")

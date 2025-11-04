# core/views/api_views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def test_api(request):
    return JsonResponse({"message": "Core API is working!"})

import json
from rest_framework import viewsets
from .models import SnsPost, UserProfile
from .serializers import SnsPostSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate,login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth.models import User

class SnsPostViewSet(viewsets.ModelViewSet):
    queryset = SnsPost.objects.all()
    serializer_class = SnsPostSerializer


@method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(View):

    def post(self, request):
        params = json.loads(request.body)
        username = params['username']
        password = params['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'is_authenticated': True, 'user_id': user.id})

        return JsonResponse({'is_authenticated': False}, status=403)


@csrf_exempt  # CSRF保護を無効化（開発時のみ）
def create_user(request):
    if request.method == 'POST':
        params = json.loads(request.body)
        username = params.get('username')
        password = params.get('password')

        if username and password:
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'message': 'User created successfully.'})
        else:
            return JsonResponse({'message': 'Username and password are required.'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)


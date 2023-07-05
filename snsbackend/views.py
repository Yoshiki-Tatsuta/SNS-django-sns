import json
from rest_framework import viewsets
from .models import SnsPost, UserProfile
from .serializers import SnsPostSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
# from rest_framework_jwt.views import ObtainJSONWebToken
# from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth.models import User

class SnsPostViewSet(viewsets.ModelViewSet):
    queryset = SnsPost.objects.all()
    serializer_class = SnsPostSerializer
    

# class CustomObtainJSONWebToken(ObtainJSONWebToken):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)
#         if user:
#             response = super().post(request, *args, **kwargs)
#             # ログインが成功した場合に追加の情報をレスポンスに含める場合は、ここで処理を追加します
#             return response

#         return Response({'detail': 'Invalid credentials'}, status=400)

# login_view = CustomObtainJSONWebToken.as_view()

@method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(View):

    def post(self, request):
        params = json.loads(request.body)
        username = params['username']
        password = params['password']
        user = User.objects.get(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'is_authenticated': True, 'user_id': user.id})

        return JsonResponse({'is_authenticated': False}, status=403)

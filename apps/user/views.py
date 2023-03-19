from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import get_authorization_header
from apps.user.api.serializers import PasswordSerializer, UserTokenSerializer


def remove_indices(list_to_check: list, item_to_find: str):
    list_of_permissions = []
    for item in list_to_check:
        spl = item.split('_')
        if spl[1] != item_to_find:
            list_of_permissions.append(item)
    return list_of_permissions       

class UserToken(APIView):
    def post(self,request,*args,**kwargs):
        email = request.data['email']
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(email = email).first()
            )
            return Response({
                'token': user_token.key
            })
        except:
            return Response({'error': 'The credentials received are incorrect.'},status = status.HTTP_401_UNAUTHORIZED)
                            
class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializaer = UserTokenSerializer(user)
                permissions = user.get_all_permissions()
                cl_permissions = remove_indices(permissions, 'historicaluser')
                if created:
                    return Response({
                        'token': token.key,
                        'user':user_serializaer.data,
                        'permissions': cl_permissions
                        }, status = status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializaer.data,
                        'permissions': cl_permissions
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'This user is disabled'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Invalid username or password'}, status = status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = get_authorization_header(request).split()
            try:
                token = token[1].decode()
            except:
                return None
            token = Token.objects.filter(key=token).first()

            if token:
                user = token.user
                all_sessions = Session.objects.filter(
                    expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                return Response({'token_message': 'Deleted token.', 'session_message': 'Deleted user sessions.'},
                                status=status.HTTP_200_OK)

            return Response({'error': 'A user with these credentials was not found.'},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No token found in request.'},
                            status=status.HTTP_409_CONFLICT)
            

class ManagePassword(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request, pk=None):
        id = pk or request.query_params.get('id')
        try:
            token = get_authorization_header(request).split()
            try:
                token = token[1].decode()
            except:
                return None
            token = Token.objects.filter(key=token).first()

            if token:
                user = token.user
                if user.id == id:
                    password_serializer = PasswordSerializer(data=request.data)
                    if password_serializer.is_valid():
                        user.set_password(password_serializer.validated_data['password'])
                        user.save()
                        return Response({
                            'message': 'Password updated successfully'
                        })
                    return Response({
                        'message': 'There are errors in the information received',
                        'errors': password_serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
                return Response({
                    'message': "You're not the owner of this account",
                }, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'A user with these credentials was not found.'},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No token found in request.'},
                            status=status.HTTP_409_CONFLICT)
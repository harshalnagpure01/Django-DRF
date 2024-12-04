from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.messages import USER_MESSAGES , ERROR_MESSAGES

class CountryView(APIView):
    def get(self,request,id=None,format=None):
        try:
            if id:
                obj= Country.objects.get(id=id)
                serializer = CountrySerializer(obj)
                context={'message':USER_MESSAGES['fetch_data'],'data':serializer.data}
                return Response(context,status=200)
            else:
                obj= Country.objects.all()
                serializer = CountrySerializer(obj,many=True)
                context={'message':USER_MESSAGES['fetch_data'],'data':serializer.data}
                return Response(context,status=200)
        except Country.DoesNotExist:
            context ={'message':ERROR_MESSAGES['fetch_error'],'error':'Country not found'}
            return Response(context,status=404)
        except Exception as e:
            context ={'message':ERROR_MESSAGES['fetch_error'],'error':str(e)}
            return Response(context,status=500)

    def post(self,request):
        try:
            country_name=request.data.get('country_name')
            code=request.data.get('code')
            short_name=request.data.get('short_name')
            flag= request.data.get('flag')

            obj=Country.objects.create(
                country_name=country_name,
                code=code,
                short_name=short_name,
                flag=flag
            )

            obj.save()

            """ 
            <--------Another Way-------->

                obj = Country(
                country_name=request.data['country_name'],
                code=request.data['code'],
                short_name=request.data['short_name'],
                flag=request.data['flag']
            )
            obj.save()

            """
            serializer=CountrySerializer(obj)
            context={'message':USER_MESSAGES['post_data'],'data':serializer.data}
            return Response(context)
        except Exception as e:
            context={'message':ERROR_MESSAGES['post_error'],'error':f'{e}'}
            return Response(context)           

    def delete(self,request,id=None):
        try:
            if id:
                obj=Country.objects.get(id=id)
                obj.delete()
                context= {
                    'message':USER_MESSAGES['delete_data']
                }
                return Response(context)

        except:
            context={'message':ERROR_MESSAGES['delete_error']}
            return Response(context)
    
    def put(self,request,id):
        try:
            if id:
                obj= Country.objects.get(id=id)
                country_name= request.data.get('country_name')
                code=request.data.get('code')
                short_name=request.data.get('short_name')
                flag=request.data.get('flag')

                obj.country_name=country_name
                obj.code=code
                obj.short_name=short_name
                obj.flag=flag

                obj.save()
                serializer=CountrySerializer(obj)
                context= {'messages':USER_MESSAGES['update_data'],'data':serializer.data}
                return Response(context)        
        except Exception as e:
            context ={'message':ERROR_MESSAGES['updata_error'],'error':f"{e}"}
            return Response(context)


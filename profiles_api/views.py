from rest_framework.views import APIView
from rest_framework.response import response


class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Users HTTP as function (get,post,patch,delete,put)',
            'Gives you the most control of your application logic',
            'It is mapped manually to URL',
        ]

        return Response({'message:' 'Hello', 'apiview:' an_apiview})
from rest_framework.response import Response

def success_response(data=None, message="Success"):
    return Response({
        "estatus": True,
        "emessage": message,
        "data": data
    })

def error_response(message="Something went wrong", status=400):
    return Response({
        "estatus": False,
        "emessage": message
    }, status=status)

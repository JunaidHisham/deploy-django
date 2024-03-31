import OTPLessAuthSDK
from django.http.response import HttpResponse
from django.conf import settings as SETTINGS


def index(request):
    client_id = SETTINGS.OTP_LESS_CLIENT_ID
    client_secret = SETTINGS.OTP_LESS_CLIENT_SECRET
    # code = "your_id_token_here"
    audience = None
    mobile_number="919846945506"
    email=""
    redirect_uri="http://127.0.0.1:8001/authentication/verify-code/"
    channel="WHATSAPP"
    try:
        user_details = OTPLessAuthSDK.UserDetail.generate_magic_link(
            mobile_number=mobile_number, 
            client_id=client_id, 
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            channel=channel,
            email=email
        )
        print('user_details', user_details)
        
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong!!")


    print(f"User details: {user_details}")

    return HttpResponse("Done")


def verify_code(request):
    client_id = SETTINGS.OTP_LESS_CLIENT_ID
    client_secret = SETTINGS.OTP_LESS_CLIENT_SECRET
    # code = "your_id_token_here"
    audience = None
    code = request.GET.get('code')
    print('====code====', code)
    try:
        user_details = OTPLessAuthSDK.UserDetail.verify_code(code, client_id, client_secret, audience)

        print(user_details.success)
        print(user_details.auth_time)
        print(user_details.phone_number)
        print(user_details.email)
        print(user_details.name)
        print(user_details.country_code)
        print(user_details.national_phone_number)
        print(f"Returning User details: {user_details}")
    except Exception as e:
        print('===error==', e)
        return HttpResponse("Something went wrong!!")

    return HttpResponse("Return Response")


from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt




from web_project import settings

User = get_user_model()


@api_view(['POST'])
def password_reset_request(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        reset_link = f"{settings.DOMAIN}/api/reset-password/?uid={uid}&token={token}"

                 # Adjust as needed
        send_mail(
        'Password Reset',
        f'Reset your password: {reset_link}',
        settings.DEFAULT_FROM_EMAIL,  # Use the configuredGmail
        [email],
        )
        return Response({"message": "Password reset email sent."}, status=200)
    except User.DoesNotExist:
        return Response({"error": "User with this email does not exist."}, status=404)

@api_view(['POST'])
def password_reset_confirm(request):
    uid = request.data.get('uid')
    token = request.data.get('token')
    new_password = request.data.get('new_password')

    if not uid or not token or not new_password:
        return Response({"error": "Missing uid, token, or new_password."}, status=400)

    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = get_object_or_404(User, pk=uid)

        if default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successful."})
        else:
            return Response({"error": "Invalid token or UID."}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


def reset_password_form(request):
    uid = request.GET.get('uid')
    token = request.GET.get('token')
    return render(request, 'reset_form.html', {'uid': uid, 'token': token})

@csrf_exempt
def reset_password_submit(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        token = request.POST.get('token')
        new_password = request.POST.get('new_password')

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)

            if default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset successfully.')
                return redirect('/')  # Or any success page
            else:
                messages.error(request, 'Invalid or expired token.')
        except Exception as e:
            messages.error(request, f"Error: {e}")

    return redirect('/reset-password/')  # Redirect back on failure
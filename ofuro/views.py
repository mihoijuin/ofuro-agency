from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth


@login_required
def ordered(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    return render(request, 'ordered.html', {'user': user})

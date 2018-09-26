from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

from .twitbot import TweetBot


@login_required
def ordered(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    try:
        reply_bot = TweetBot()
        reply_bot.reply_result(user.access_token['screen_name'])
    except:
        return render(request, 'wait.html')
    return render(request, 'ordered.html', {'user': user})

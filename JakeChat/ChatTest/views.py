from django.shortcuts import render, redirect

def ChatPage(request):
    if not request.user.is_authenticated:
        return redirect('login-user')
    context = {

    }
    return render(request, 'ChatTest/chatPage.html', context)

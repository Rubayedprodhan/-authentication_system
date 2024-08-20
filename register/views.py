from django.shortcuts import render,redirect
from .forms import Registerfrom,ChangeUserFrom
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=='POST':
        register_form=Registerfrom(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('user_login')
    else:
        register_form = Registerfrom()
    return render(request, 'signup.html', {'form': register_form})


def user_login(request):
    if request.method=='POST':
        form =AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=username, password=user_pass)
            if user is not None:
                messages.success(request,"Logged in Successfully")
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Login information incorrect')
        else:
            messages.warning(request,'Invalid form submission')
    else:
        form=AuthenticationForm()

    return render(request,'signup.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,'Account Logout Successfully')
    return redirect('user_login')

@login_required
def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=ChangeUserFrom(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Account Updated Successfully')
                form.save()

        else:
            form = ChangeUserFrom(instance=request.user)
        return render(request,'profile.html',{'form':form})
    
    else:
        return redirect('signup')
    

@login_required
def profile_edit(request):
    if request.method=="POST":
        profile_form=ChangeUserFrom(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,"Profile Updated successfully")
            return redirect('profile')
    else:
        profile_form=ChangeUserFrom(instance=request.user)
    return render(request,'updateprofile.html',{'form': profile_form})

@login_required
def profile_edit_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'passchange.html',{'form':form})


def pass_change(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                messages.success(request,'Password Updated Successfully')
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('user_login')
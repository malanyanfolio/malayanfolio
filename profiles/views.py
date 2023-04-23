from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import *
from profiles.forms import UserProfileForm, ExtraCurriForm, InterestForm, LanguageForm
# Create your views here.

@login_required
def MyProfile(request):
    userProfile = UserProfile.objects.get(user_id = get_user_account(request))
    userOutputs = Outputs.objects.get(user_id = userProfile.id)
    userClubs = Clubs.objects.filter(user_id = userProfile.id)
    userLanguages = Languages.objects.filter(user_id = userProfile.id)
    userInterests = Interests.objects.filter(user_id = userProfile.id)
    userEducation = Education.objects.filter(user_id = userProfile.id)

    context={
        'userProfile' : userProfile,
        'userOutputs':userOutputs,
        'userClubs':userClubs,
        'userLanguages':userLanguages,
        'userInterests':userInterests,
        'userEducation':userEducation,
    }
    return render(request, 'profile/myprofile.html', context)

@login_required
def EditProfile(request):
    userProfile = UserProfile.objects.get(user_id = get_user_account(request))
    form = UserProfileForm(request.POST,request.FILES)
    context={
        'userProfile' : userProfile,
        'form':form
    }
    if request.method=="POST":
        save_profile(request, userProfile)
        messages.success(request, "Profile successfully Edited")
        return redirect('edit-profile-contact')
    return render(request, 'profile/edit_profile.html', context)

@login_required
def EditProfileContact(request):
    userProfile = UserProfile.objects.get(user_id = get_user_account(request))
    userOutputs = Outputs.objects.get(user_id = userProfile.id)
    context={
        'userProfile':userProfile,
        'userOutputs':userOutputs,
    }
    if request.method == "POST":
        save_profile_contacts(request, userProfile)
        save_outputs(request, userOutputs)
        messages.success(request, "Profile successfully Edited")
        return redirect("edit-profile-about-me")
    return render(request, 'profile/edit_profile_contact.html', context)

@login_required
def EditProfileAbout(request):
    userProfile = UserProfile.objects.get(user_id = get_user_account(request))
    educProfile = Education.objects.filter(user_id = userProfile.id)
    club_list = []
    interest_list = []
    

    ECProfile, club_list = get_ECProfile(userProfile)
    
    InterestsProfile, interest_list = get_InterestsProfile(userProfile)
    
    LangProfile = get_LanguageProfile(userProfile)

    


    ECForm = ExtraCurriForm
    INTForm = InterestForm
    LANGform = LanguageForm
    context={
        'userProfile':userProfile,
        'educProfile':educProfile,
        'ExtraCurriForm':ECForm,
        'InterestForm':INTForm,
        'ECProfile':ECProfile,
        'club_list':club_list,
        'InterestsProfile':InterestsProfile,
        'interest_list':interest_list,
        'LanguageForm':LANGform,
        'LangProfile':LangProfile,
    }
    if request.method == "POST":
        save_profile_about(request, userProfile)
        save_educ(request, educProfile)
        save_EC(request, userProfile)
        save_Interest(request, userProfile)
        save_Language(request, userProfile)
        messages.success(request, "Profile successfully Edited")
        return redirect("edit-profile-about-me")
    return render(request, 'profile/edit_profile_about.html', context)

@login_required
def DeleteEC(request, ec_id):
    club_data = Clubs.objects.get(id=ec_id)
    club_data.delete()
    return redirect('edit-profile-about-me')


@login_required
def DeleteINT(request, int_id):
    interest_data = Interests.objects.get(id=int_id)
    interest_data.delete()
    return redirect('edit-profile-about-me')


@login_required
def DeleteLANG(request, lang_id):
    lang_data = Languages.objects.get(id=lang_id)
    lang_data.delete()
    return redirect('edit-profile-about-me')





# functions (MOVE TO UTILS.PY)

def get_user_account(request):
    return request.user.id

def save_outputs(request, userOutputs):
    try:
        userOutputs.img_output1 = request.FILES['img_output1']
    except: pass
    try:
        userOutputs.img_output2 = request.FILES['img_output2']
    except: pass
    try:
        userOutputs.img_output3 = request.FILES['img_output3']
    except: pass
    userOutputs.save()

def save_profile_contacts(request, userProfile):
    userProfile.email = request.POST['email']
    userProfile.onedlink = request.POST['onedlink']
    userProfile.save() 

def save_profile(request, userProfile):
    userProfile.fname  = request.POST['fname']
    userProfile.lname = request.POST['lname'] 
    userProfile.strand = request.POST['strand'] 
    try:
        userProfile.pfp  = request.FILES['pfp']
    except:
        pass
    userProfile.pronouns = request.POST['pronouns']
    userProfile.save()

def save_profile_about(request, userProfile):
    userProfile.about = request.POST['about']
    userProfile.save()

def save_educ(request, educProfile):
    for educ in educProfile:
        if educ.educ_type == "PS":
            educ.year = request.POST['year_PS']
            educ.school = request.POST['name_PS']
            educ.save()
        if educ.educ_type == "GS":
            educ.year = request.POST['year_GS']
            educ.school = request.POST['name_GS']
            educ.save()
        if educ.educ_type == "HS":
            educ.year = request.POST['year_HS']
            educ.school = request.POST['name_HS']
            educ.save()
        if educ.educ_type == "SHS":
            educ.year = request.POST['year_SHS']
            educ.school = request.POST['name_SHS']
            educ.save()

def save_EC(request,userProfile):
    count = request.POST['EC-count']
    for i in range(int(count)):
        try:
            Clubs.objects.create(
                user_id = userProfile,
                user_club = request.POST[f'new_EC-{i+1}']
            )
        except:
            pass

def save_Interest(request,userProfile):
    count = request.POST['INT-count']
    for i in range(int(count)):
        try:
            Interests.objects.create(
                user_id = userProfile,
                user_interest = request.POST[f'new_INT-{i+1}']
            )
        except:
            pass

def save_Language(request, userProfile):
    count = int(request.POST['lang_count'])
    for i in range(int(count)):
        try:
            Languages.objects.create(
                user_id = userProfile,
                user_lang = request.POST[f'user_lang-{i+1}'],
                lang_proficiency = request.POST[f'lang_proficiency-{i+1}']
            )
        except Exception as e:
            print("----------")
            print(e)

def get_ECProfile(userProfile):
    club_list = []
    if Clubs.objects.filter(user_id = userProfile.id).count() > 0 :
        ECProfile  = Clubs.objects.filter(user_id = userProfile.id)
        for ec in ECProfile:
            club_list.append(ec.user_club)
    else:
        ECProfile = None
    return ECProfile, club_list

def get_InterestsProfile(userProfile):
    interest_list=[]
    if Interests.objects.filter(user_id = userProfile.id).count() > 0 :
        InterestsProfile  = Interests.objects.filter(user_id = userProfile.id)
        for intP in InterestsProfile:
            interest_list.append(intP.user_interest)
    else:
        InterestsProfile = None
    return InterestsProfile, interest_list

def get_LanguageProfile(userProfile):
    if Languages.objects.filter(user_id = userProfile.id).count() > 0 :
        LangProfile  = Languages.objects.filter(user_id = userProfile.id)
    else:
        LangProfile = None

    return LangProfile







   
from django.urls import path

from profiles import views



urlpatterns = [
    
    path(
        #"register/", views.RegisterAccount.as_view(), name="register-account"
        "myprofile/", views.MyProfile, name="my-profile"
    ),
    
    path(
        #"register/", views.RegisterAccount.as_view(), name="register-account"
        "edit_profile/profile-and-info", views.EditProfile, name="edit-profile"
    ),
    path(
        #"register/", views.RegisterAccount.as_view(), name="register-account"
        "edit_profile/contact", views.EditProfileContact, name="edit-profile-contact"
    ),
    path(
        #"register/", views.RegisterAccount.as_view(), name="register-account"
        "edit_profile/about-me", views.EditProfileAbout, name="edit-profile-about-me"
    ),
    path(
        #"register/", views.RegisterAccount.as_view(), name="register-account"
        "edit_profile/about-me/delete/<ec_id>", views.DeleteEC, name="delete-ec"
    ),

    path(
        #"register/", views.RegisterAccount.as_view(), name="register-account"
        "edit_profile/about-me/delete/interest/<int_id>", views.DeleteINT, name="delete-int"
    ),
    path(
        #"register/", views.RegisterAccount.as_view(), name="register-account"
        "edit_profile/about-me/delete/language/<lang_id>", views.DeleteLANG, name="delete-lang"
    ),
    
    
]

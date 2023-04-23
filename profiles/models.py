from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserProfile(models.Model):
    class Strands(models.TextChoices):
            STEM = "STEM", _("Science, Technology, Engineering, And Mathematics")
            ABM = "ABM", _("Accountancy, Business, and Management")
            HUMSS = "HUMSS",_("Humanities and Social Sciences")
            TVL = "TVL", _("Technical-Vocational Livelihood")
            ADT = "ADT",_("Arts and Design")
            ICT = "ICT", _("Information and Communications Technology")

    class Pronouns(models.TextChoices):
        F = "F", _("She / Her")
        M = "M", _("He / Him")
        T = "T",_("They / Them")
        AP = "AP", _("Any Pronouns")
        X = "X",_("Rather Not Say")

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_constraint=False)
    fname = models.CharField(max_length=255, null=True, blank=True)
    lname = models.CharField(max_length=255, null=True, blank=True)
    strand = models.CharField(max_length=100, choices=Strands.choices, null=True, blank=True)
    pronouns = models.CharField(max_length=100, choices=Pronouns.choices, null=True, blank=True)
    pfp = models.ImageField(upload_to = 'images', null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    onedlink = models.URLField(max_length=200, null=True, blank=True)
    about = models.CharField(max_length=2550, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.fname} {self.lname}, {self.strand}"
    
class Clubs(models.Model):
    class ClubList(models.TextChoices):
        acads = "acads", _("Academics (Math, Science, Etc.)")
        red_cross = "red_cross", _("Red Cross")
        photo = "photo",_("Photography")
        sports = "sports", _("Sports")
        arts = "arts",_("Art")
        school_news = "school_news", _("School Newspaper")
        performance = "performance", _("Performance")

    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_club = models.CharField(max_length=100, choices=ClubList.choices, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id.id} - {self.user_id.lname} | {self.user_club}"

class Interests(models.Model): 
    class InterestList(models.TextChoices):
        sports = "sports", _("Sports")
        travel = "travel", _("Travelling")
        photo = "photo",_("Photography / Films")
        art = "art", _("Art")
        gaming = "gaming",_("Gaming")
        pets = "pets", _("Pets")
        music = "music", _("Music")
        literature = "literature", _("Literature")

    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_interest = models.CharField(max_length=100, choices=InterestList.choices, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id.id} - {self.user_id.lname} | {self.user_interest}"

class Education(models.Model): 
    class EducList(models.TextChoices):
        PS = "PS",_("Preschool")
        GS = "GS", _("Grade School")
        HS = "HS", _("High School")
        SHS = "SHS", _("Senior High School")
        COL = "COL",_("College")
        
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    educ_type = models.CharField(max_length=255, choices=EducList.choices, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id.id} - {self.user_id.lname} | {self.educ_type}"

class Outputs(models.Model): 
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    img_output1 = models.ImageField(upload_to="media", null=True, blank=True)
    img_output2 = models.ImageField(upload_to="media", null=True, blank=True)
    img_output3 = models.ImageField(upload_to="media", null=True, blank=True)

    def __str__(self):
        return f"{self.user_id.id} - {self.user_id.lname}, {self.user_id.fname} "

class Languages(models.Model):
    class LanguageProficiency(models.TextChoices):
        BG = "BG",_("Beginner | limited working")
        MR = "MR", _("Mid-range | Conversation")
        AD = "AD", _("Advanced | Native speaker")

    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_lang = models.CharField(max_length=255, null=True, blank=True)
    lang_proficiency = models.CharField(choices=LanguageProficiency.choices, max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user_id.id} - {self.user_id.lname} | {self.user_lang}"

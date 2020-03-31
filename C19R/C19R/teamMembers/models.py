from django.db import models
from phone_field import PhoneField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_auto_one_to_one import AutoOneToOneModel


class Sector(models.Model):
    name = models.CharField(max_length=35, primary_key=True, unique=True, verbose_name="Sector of Business",
                            help_text="What sector does this business work in?  Coffee, retail, restaurant, etc")
    # type of business


class Business(models.Model):
    name = models.CharField(max_length=35, primary_key=True, unique=True, help_text="Name of the business. 35 characters max.", verbose_name="Name")
    # name of the business
    status = models.BooleanField(verbose_name="Currently open", help_text="Check for yes, leave blank for no")
    # is the store open or not
    businessType = models.ForeignKey(Sector, on_delete=models.CASCADE, help_text="Select what best describes this business.", verbose_name="Type of Business")

    # what kind of operation is it? Coffee, retail, restaurant, etc

    def get_absolute_url(self):
        if self.status:
            return reverse('teamMembers_addStoreInfo', kwargs={'pk': StoreInfo.objects.get(business=self).pk})
        else:
            return reverse('teamMembers_viewBusinesses')


class StoreInfo(AutoOneToOneModel(Business)):
    phoneNumber = PhoneField(null=True, E164_only=True, help_text='Store phone number.', verbose_name='Contact Number')
    # phone number of the business
    website = models.URLField(null=True, blank=True, verbose_name="Website", help_text="Store website.")
    # if the business has a website add the home screen here
    timeOpen = models.TimeField(null=True, help_text="What times does the store open?", verbose_name="Opening Time. In 24 hour time. Ex: 6:30 am is 06:30:00")
    # time the store opens
    timeClose = models.TimeField(null=True, help_text="What times does the store close?", verbose_name="Closing Time. In 24 hour time. Ex: 7:45 pm is 19:45:00")
    # time the store closes
    ordering = models.TextField(null=True, max_length=250, help_text="How can customers order products -i.e. online, phone, etc. 250 characters max",
                                verbose_name="How Can Customers Order")
    # types or ordering allowed
    inStorePickUp = models.BooleanField(null=True, help_text="Can customer pick up in store? (check for yes, leave blank for no).", verbose_name="In store pickup")
    # is in store pick up allowed
    deliveryOption = models.BooleanField(
        null=True,
        help_text="Can customers have items delivered via mail, driver, etc - i.e. someway the ordered item will arrive at their home (check for yes, leave blank for no).",
        verbose_name="Delivery Available")
    # is a delivery option available
    specialNotes = models.TextField(blank=True, null=True, max_length=250, verbose_name="Special Notes", help_text="Additional details people should know? 250 characters max.",
                                    default=None)
    # extra details people should know about
    ownerMessage = models.TextField(blank=True, null=True, max_length=250, help_text="If the owner wants to say something quote then here. 250 characters max.",
                                    verbose_name="Owner Message")
    # any extra that the owner would like to add about their business
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=None, blank=True, verbose_name="Entry created by", help_text="User that created this entry",
                                  related_name="Creating_User")
    # person who created this entry
    approvedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=None, blank=True, verbose_name="Entry approved by",
                                   help_text="Admin that approved for publishing", related_name="Approving_User")
    # admin who approved this info before going out
    lastUpdatedDate = models.DateTimeField(default=timezone.now, verbose_name="Last updated")
    # time of last update
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")

    # when this entry was first created

    def get_absolute_url(self):
        return reverse('teamMembers_viewBusinesses')

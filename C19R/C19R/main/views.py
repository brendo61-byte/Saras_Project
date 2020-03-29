from django.shortcuts import render
from teamMembers.models import Sector, Business, StoreInfo


def makeMenueContext():
    context = {
        "sectors": Sector.objects.all(),
        "businesses": [],
    }

    for sector in context.get("sectors"):
        tempBusinessDict = {"name": sector.name}

        businessList = Business.objects.filter(businessType=sector).order_by("name")  # order alphabetically

        tempStoreList = []

        for store in businessList:
            storeInfo = StoreInfo.objects.get(business=store)

            tempStoreList.append(storeInfo)

        tempBusinessDict.update({"stores": tempStoreList})

        context.get("businesses").append(tempBusinessDict)

    allBusinesses = Business.objects.all().order_by("name")

    context.update({"allBusinesses": allBusinesses})

    return context


def home(request):
    context = makeMenueContext()

    return render(request, 'main/homePage.html', context)

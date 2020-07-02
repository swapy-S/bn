from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import bankDetails
import pandas as pd
import os
from rest_framework.views import APIView
d=os.path.dirname(os.getcwd())
d=os.path.join(d,"app")
d=os.path.join(d,"banks")
os.chdir(d)
# Create your views here.
def test(request):
    df = pd.read_csv('bank_branches.csv', sep=',')
    products = []
    try:
        print(len(df))
        for i in range(len(df)):
            print(i)
            products.append(
                bankDetails(
                df.iloc[i][0]
                ,int(df.iloc[i][1])
                ,df.iloc[i][2]
                ,df.iloc[i][3]
                ,df.iloc[i][4]
                ,df.iloc[i][5]
                ,df.iloc[i][6]
                ,df.iloc[i][7]
                )
            )
        bankDetails.objects.bulk_create(products)
        # print(df.head())
        return JsonResponse({'test':'pass'},status=200)
    except Exception as e:
        return JsonResponse({'test':e},status=200)
class getBranchDetailsByIFSC(APIView):
    def get(self,request):
        ifsc_search=request.data['ifsc']
        print(ifsc_search)
        try:
            branchdetails=bankDetails.objects.all().filter(ifsc=ifsc_search)[0]
            d={'ifsc':branchdetails.ifsc,'bank_id':branchdetails.bank_id,'branch':branchdetails.branch,'address':branchdetails.address,'city':branchdetails.city,'district':branchdetails.district,'state':branchdetails.state,'bank_name':branchdetails.bank_name}
            # print(branchdetails)
            return JsonResponse({'result':d},status=200)
        except Exception as e:
            return JsonResponse({'result':e},status=500)
class getBranchDetailsByBankNameAndCity(APIView):
    def get(self,request):
        bank_search=request.data['bank_name']
        city_search=request.data['city']
        try:
            branchdetails1=bankDetails.objects.all().filter(bank_name=bank_search,city=city_search)
            print(branchdetails1)
            l=[]
            for branchdetails in branchdetails1:
                d={'ifsc':branchdetails.ifsc,'bank_id':branchdetails.bank_id,'branch':branchdetails.branch,'address':branchdetails.address,'city':branchdetails.city,'district':branchdetails.district,'state':branchdetails.state,'bank_name':branchdetails.bank_name}
                l.append(d)
            # print(branchdetails)
            return JsonResponse({'result':l},status=200)
        except Exception as e:
            return JsonResponse({'result':e},status=500)

from django.shortcuts import render
import json
import numpy as np
import tensorflow as tf
import joblib
from django.http import JsonResponse

# Create your views here.
def predict(request):
    # if Post method
    if request.POST is not None:

        var = json.loads(request.body)

        Administrative = float(var['Administrative'])
        Administrative_Duration = float(var['Administrative_Duration'])
        Informational = float(var['Informational'])
        Informational_Duration = float(var['Informational_Duration'])
        ProductRelated = float(var['ProductRelated'])
        ProductRelated_Duration = float(var['ProductRelated_Duration'])
        BounceRates = float(var['BounceRates'])
        ExitRates = float(var['ExitRates'])
        PageValues = float(var['PageValues'])
        SpecialDay = float(var['SpecialDay'])
        OperatingSystems = float(var['OperatingSystems'])
        Browser = float(var['Browser'])
        Region = float(var['Region'])
        TrafficType = float(var['TrafficType'])
        Dec = float(var['Dec'])
        Feb = float(var['Feb'])
        Jul = float(var['Jul'])
        June = float(var['June'])
        Mar = float(var['Mar'])
        May = float(var['May'])
        Nov = float(var['Nov'])
        Oct = float(var['Oct'])
        Sep = float(var['Sep'])
        Other = float(var['Other'])
        Returning_Visitor = float(var['Returning_Visitor'])
        Weekend = float(var['Weekend'])






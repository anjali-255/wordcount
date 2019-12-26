from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def count(request):
    anjali = request.GET['anjali']
    wordlist = anjali.split()

    worddictionary ={}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1
    """sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)"""
    return render(request, 'count.html', {'anjali': anjali, 'anjali': len(wordlist), 'worddictionary': worddictionary.items()})


def about(request):
    return render(request, 'about.html')
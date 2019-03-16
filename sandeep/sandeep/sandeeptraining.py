from django.http import HttpResponse
from django.shortcuts import render
def ram(request):
    return render(request,"countwords.html")
def count(request):
    mess=request.GET['message']
    wl=mess.split()
    wordlist={}
    for word in wl:
        if word in wordlist:
            wordlist[word]+=1
        else:
            wordlist[word]=1
    return render(request,"count.html",{"msg":mess,"length":len(wl),"abc":wordlist})
from django.shortcuts import render
from fetch import fetch_content
# Create your views here.
def home(request):
    return render(request, 'homepage.html')
def news(request):
    url = "http://www.aau.edu.et/"
    content_info_list = fetch_content(url)
    context = {'message':content_info_list }
    return render(request, 'show.html', context)

def announcements(request):
   announcements_url = "http://www.aau.edu.et/blog/category/announcements/"

   announcements_info_list = fetch_content(announcements_url)
   context = {'message': announcements_info_list }
   return render(request, 'show.html', context)


   
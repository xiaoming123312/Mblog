#coding=utf-8

from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime
from .models import Post
from django.http import HttpResponse
from django.shortcuts import redirect
import sys


# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now().strftime("%Y-%m-%d %H:%I:%S")
    html = template.render(locals())
    return HttpResponse(html)

    # posts = Post.objects.all()
    # post_lists = list()
    # for count,post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
    #     post_lists.append("<small>" + str(post.body.encode('utf-8').decode(sys.stdin.encoding))+"</small><br><br>")
    # return HttpResponse(post_lists)

def showpost(request ,slug ):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect("/")

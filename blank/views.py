# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from google.appengine.ext import ndb

from django import forms
from google.appengine.api import users

'''
Model 定義
本来は同じ階層にmodels.pyを定義して書く
今回は一覧性のため特別ベタ書き
'''
class MessageModel(ndb.Model):
  # 書いた人の名前
  user  = ndb.StringProperty(required=True)
  # メッセージタイトル
  title = ndb.StringProperty(required=True)
  # メッセージ本文
  body  = ndb.TextProperty(required=True)
  # 作成日時
  date  = ndb.DateTimeProperty(auto_now_add=True)

  @classmethod
  def getRecent(cls):
    return cls.query().order(-cls.date)

class MessageForm(forms.Form):
    title = forms.CharField(max_length=100)
    body  = forms.CharField(max_length=1024, widget=forms.Textarea)

def write(request):
    user = users.get_current_user()
    if not user:
        return HttpResponseRedirect(users.create_login_url(request.path))
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = MessageModel(
                user  = user.nickname(),
                title = form.cleaned_data['title'],
                body  = form.cleaned_data['body']
            )
            msg.put()
            return HttpResponseRedirect('/?write=success')
    else:
        form = MessageForm()

    return render_to_response('message_form.html', {
        'form': form,
    })

def index(request):
    messages = MessageModel.getRecent().fetch(10)
    context = {
        'messages': messages,
    }
    return render_to_response('index.html',context)

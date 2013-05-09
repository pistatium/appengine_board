# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from google.appengine.datastore.datastore_query import Cursor
from google.appengine.ext import ndb

from django import forms
from google.appengine.api import users

from libs.gae_paginator import GAEPaginator
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
    '''最近のメッセージを取得するクラスメソッド'''
    return cls.query().order(-cls.date)

'''
フォーム定義
定義をするとフォーム生成やバリデーションを
自動的に行なってくれる
'''
class MessageForm(forms.Form):
    title = forms.CharField(max_length=100)
    body  = forms.CharField(max_length=1024, widget=forms.Textarea)



#-Views-----------------------------------------------------------------
#-----------------------------------------------------------------------
    
def index(request,page_num="1"):
    '''
      トップページのView
      最近のメッセージを取得して表示
    '''
    PAGE_COUNT = 3
    messages= MessageModel.getRecent()
    msgs = GAEPaginator(messages, PAGE_COUNT)
    context = {
        'messages': msgs.page(int(page_num)),
    }
    return render_to_response('message/index.html',context)

    
def write(request):
    '''
      書き込みページのView
    '''
    #ログインチェック
    user = users.get_current_user()
    if not user:
        return HttpResponseRedirect(users.create_login_url(request.path))

    # POSTなら保存、GETならフォーム表示
    if request.method == 'POST':
        form = MessageForm(request.POST)
        # バリデーションチェック
        if form.is_valid():
            msg = MessageModel(
                user  = user.nickname(),
                title = form.cleaned_data['title'],
                body  = form.cleaned_data['body']
            )
            # DB保存
            msg.put()
            # リダイレクト
            return HttpResponseRedirect('/static/write_success.html')
          
    # GETの場合   
    else:
        # 表示するフォームを生成
        form = MessageForm()

    return render_to_response('message/write_form.html', {
        'user': user,
        'logout_url': users.create_logout_url(request.path),
        'form': form,
    })







































            

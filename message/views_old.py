# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import Context, loader

# Databaseを使うためのインポート
from google.appengine.ext import ndb

'''
Model 定義
本当は同じ階層にmodels.py を作ってそこに書く(import hogehoge.models)
今回は一覧性を高めるため特別にベタ書き
'''
class MessageModel(ndb.Model):
    # 書いた人
    name = ndb.StringProperty(require=True)
    # 本文
    body = ndb.TextProperty(require=True)
    # 日付
    date = ndb.DateTimeProperty(auto_now_add=True)
    
def index(request, message):
    context = Context({
        'message': message,
    })

    return HttpResponse(loader.get_template('index.html').render(context))
